#! /usr/bin/env python
#  -*- coding: utf-8 -*-

import argparse
import xml.etree.cElementTree as ET
import sys
import signal
from os import isatty, path

__version__ = "0.10"
"""Version of lib"""


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def is_pipe():
    """
    Return if stdin has a value

    :return: True, if there is a value on stdin
    """
    return not isatty(sys.stdin.fileno())


def main():
    """
    Main Method of lib
    """

    junit_xml_output = "yamllint-junit.xml"

    parser = argparse.ArgumentParser(
        usage="%(prog)s [options] input",
    )

    parser.add_argument('input', nargs='?', type=argparse.FileType('r'), default=("" if sys.stdin.isatty() else sys.stdin))
    parser.add_argument("-o", "--output", type=str, help="output XML to file", default=junit_xml_output)
    parser.add_argument("-v", "--verbose", action="store_true", help="print XML to console as command output", default=False)
    parser.add_argument("--version", action='version', version='%(prog)s ' + __version__)
    parser.add_argument("--test-name", type=str, help="testsuite name to report in the JUnit file", default='yamllint')

    args = parser.parse_args()

    lines = []
    if is_pipe():
        for line in sys.stdin:
            if len(line.strip()) > 0:
                lines.append(line.strip())

    if not is_pipe() and not path.isfile(args.input.name):
        parser.print_help()
        parser.error('You need to provide file with output or pipe data from "yamllint" command.')
        exit(1)

    if not is_pipe():
        lint_output = open(args.input.name, "r").read().split("\n")

        for line in lint_output:
            if len(line.strip()) > 0:
                lines.append(line.strip())

    testsuites = ET.Element("testsuites")

    errors_count = 0
    skipped_count = 0

    testsuite = ET.SubElement(testsuites, "testsuite", name=args.test_name, errors="0", skipped="0", failures="0", tests=str(len(lines)), time="0")

    if not lines:
        ET.SubElement(testsuite, "testcase", name="no_yamllint_errors")
        testsuite.attrib["tests"] = "1"
    else:
        parsed_lines = []
        for line in lines:
            parsed_line = line.split(":")

            line_data = {
                "filename": parsed_line[0],
                "line": int(parsed_line[1]),
                "error": {
                    "message": parsed_line[3].strip(),
                    "text": "[%s:%s] %s" % (parsed_line[1], parsed_line[2], parsed_line[3].strip())
                }
            }
            parsed_lines.append(line_data)

            testcase = ET.SubElement(testsuite, "testcase", name=line_data['filename'])
            if parsed_line[3].strip().startswith("[warning]"):
                test_result = "skipped"
                skipped_count += 1
            else:
                test_result = "failure"
                errors_count += 1
            ET.SubElement(
                testcase,
                test_result,
                file=line_data['filename'],
                line=str(line_data['line']),
                message=line_data['error']['text'],
                type="YAML Lint"
            ).text = line_data['error']['text']

    testsuite.attrib['errors'] = str(errors_count)
    testsuite.attrib['skipped'] = str(skipped_count)
    tree = ET.ElementTree(testsuites)
    tree.write(args.output, encoding='utf8', method='xml')

    if args.verbose:
        tree.write(sys.stdout.buffer, encoding='utf8', method='xml')
