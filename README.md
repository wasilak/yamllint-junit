[yamllint-junit](https://github.com/adrienverge/yamllint) to JUnit converter [![Build Status](https://travis-ci.com/wasilak/yamllint-junit.svg?branch=master)](https://travis-ci.com/wasilak/yamllint-junit)
---

### Installation
via pip:
```shell
pip install yamllint-junit
```
### Updating
via pip:
```shell
pip install yamllint-junit --upgrade
```

### Usage:
run `yamllint-junit` and pass `yamllint` (with `-f parsable` option) output to it
```shell
yamllint -f parsable test.yaml | yamllint-junit -o yamllint-junit.xml
```

### Output
* If there are any lint errors, JUnit XML will be created specifying the detailed description of each error as reported by yamllint 
* If there are no lint errors, JUnit XML will be created denoting one successful testcase named 'no\_yamllint\_errors'. This is to maintain compatibility with JUnit parsers such as [Bamboo](https://www.atlassian.com/software/bamboo) which require that a properly formed JUnit file containing a minimum of one testcase be recorded in order to not fail builds.
