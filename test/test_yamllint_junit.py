#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
import io
import mock
import yamllint_junit_bootstrap.bootstrap as yamllint_junit


def test_with_input(monkeypatch):
    # Prepare
    stdin = u"""\
first.yaml:7:1: [error] trailing spaces (trailing-spaces)
first.yaml:16:1: [error] trailing spaces (trailing-spaces)
second.yaml:22:1: [error] trailing spaces (trailing-spaces)"""
    monkeypatch.setattr('sys.stdin', io.StringIO(stdin))
    # It's terrible to mock sys.stdin.fileno() in a test, so I extracted it in an extra method
    yamllint_junit.is_pipe = mock.MagicMock(return_value=True)
    yamllint_junit.ET.ElementTree.write = mock.MagicMock()

    # Execute
    yamllint_junit.main()

    # Test
    yamllint_junit.ET.ElementTree.write.assert_any_call("yamllint-junit.xml", encoding='utf8', method='xml')
