[yamllint-junit](https://github.com/adrienverge/yamllint) to JUnit converter
---

### Installation
via pip;
```shell
pip install yamllint-junit
```
### Updating
via pip;
```shell
pip install yamllint-junit --upgrade
```

### Usage:
1. run `yamllint-junit` and pass `yamllint` (with `-f parsable` option) output to it
  ```shell
  yamllint -f parsable test.yaml | yamllint-junit -o yamllint-junit.xml
  ```

### Output
* if there are any lint errors, full JUnit XML will be created
* if there are no errors, empty JUnit XML will be created, this is for i.e. [Bamboo](https://www.atlassian.com/software/bamboo) JUnit parser plugin compatibility.
It will break build if XML is missing or incorrect, and there is really no way of generating XML with *"PASSED"* tests in case of linter.
