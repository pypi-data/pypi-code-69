from setuptools import setup, find_packages

long_description = """# unitrail

Simple CLI utility to connect your automated tests with [TestRail](https://www.gurock.com/testrail)

## Abstract

Unitrail is utility, which allows to push results of tests execution to
Testrail server. It reads jUnit XML reports, supported by most of the automated
testing frameworks, parses results and maps them to cases listed in your
Testrail project.

It requires you to create a simple `mapping.json` file to describe how do you
want to map tests results to cases.

## Installation

### Requirements

- Python3+

### From source code

Checkout sources and run `python setup.py install`

### Using pip

```bash
$ pip install unitrail
```

## CLI interface
```
usage: unitrail [-h] -r REPORTS [REPORTS ...] [-v] [-s SERVER] -u USERNAME -p
                PASSWORD -m MAPPING [-t TESTRUN] [-O] [-C]
                [-D DEFINES [DEFINES ...]]

Fill test run in Testrail using xUnit XML report generated by automated tests

optional arguments:
  -h, --help            show this help message and exit
  -r REPORTS [REPORTS ...], --reports REPORTS [REPORTS ...]
                        xUnit reports to handle
  -v, --verbose         Make logs verbose
  -s SERVER, --server SERVER
                        Set TestRail server address (default is
                        http://testrail/index.php?/api/v2/)
  -u USERNAME, --username USERNAME
                        Username to authenticate in TestRail
  -p PASSWORD, --password PASSWORD
                        Password or API key to authenticate in TestRail
  -m MAPPING, --mapping MAPPING
                        JSON file with mapping of the testcases in report to
                        scenarios in testrail
  -t TESTRUN, --testrun TESTRUN
                        Existing testrun ID, if not exists - new one will be
                        created
  -O, --leaveopen       Do not close test run after execution. Defaults to
                        false
  -C, --forceclose      Close test run in the end, nevermind of tests
                        execution results. Defaults to false
  -D DEFINES [DEFINES ...], --defines DEFINES [DEFINES ...]
                        Define mapping parameters in dynamic from commandline
```

## Basic usage

Create a project in Testrail and fill it with sections and cases as you would like to.

Run your tests and generate jUnit XML report. Let's assume it will generate report file `/tmp/report.xml`

Let's say you have a case in testrail with name 'My first unitrail test'.

Let's also suggest you have a test named 'My first unitrail test' in your automated tests.

In this case we could map test to case directly by name, and we can easily do that with `mapping.json` file like follows:

```
{
  "project": "1",
  "testrun": {
    "name": "Test of parser script",
    "description": "Create a flexible filler for testrail"
  },
  "mapping": [
    "case2test"
  ]
}

```

Here you can see that all we have inside of the mapping is a basic description of testrun we will create and project ID set.
`project` field of mapping is a project ID - value you see in URL, when navigate to your project in testrail (like this - http://testrail/index.php?/projects/overview/11)
`testrun` is a basic description of testrun
`mapping` is a set of rules to map your tests to cases in testrun. By default - only direct match of names (test and case names) counts as a match.

Now we are all set to create a first testrun in testrail, filled from JUNIT report. Let's run:

```bash
$ unitrail -u <user> -p <password> -m mapping.json -r /tmp/report.xml
```

It will go all the way through, generating you a testrun and filling it.
If all tests pushed to testrail will be passed - it will close testrun automatically.

If you want to use already created testrun - you can provide it's ID over commandline:

```bash
$ unitrail -u <user> -p <password> -m mapping.json -r /tmp/report.xml -t <TESTRUN ID>
```

## Narrowing the focus

Let's say you have a more real life scenario - you have 1000 tests and only 20 of them are automated now.
We could use `Type` of test to filter them out, or move them to separate section in project, or something else.
All this is done by `filters` field of mapping file:

```
....
  "filters": {
    "section": {
      "name": "Component A"
    },
    "case": {
      "type_id": 1
    }
  },
....
```

For example this mapping will use only tests from 'Component A' section with `type_id` 1 to create new testrun.
You can use any `section` or `case` fields as a filter parameters. Reference [Testrail API docs](http://docs.gurock.com/testrail-api2), to see all available fields.

## Optimizing the mapping

There are also cases when several tests refer to the same case. Or some similar tests reference same case.

You can map multiple cases to multiple tests with simple lists of regexps in `mapping` field:

```
....
  "mapping": [
    "case2test",
    {
      "matcher": "any",
      "case": "Successfull download .*",
      "tests": [".*download.*", ".*get data.*"]
    },
  ]
....
```

Or in a different way - you can match one or several tests to one or several cases

```
....
  "mapping": [
    "case2test",
    {
      "matcher": "any",
      "case": [ "Download with europe proxy", "Download with american proxy", "Download with asia proxy"],
      "tests": [".*download with .* proxy"]
    },
  ]
....
```

`case2test` is a basic matcher for direct match of case and test name.

## Dynamic configuration

There is a case when you would like to take all the cases from project and map them directly to tests results.

In this case you can use a basic predefined mapping (show below), but you still
want to set project id and testrun description and name dynamically.

In this case you can use -D flag to define any mapping field from commandline.

For example this mapping

```
{
  "filters": {
    "case": {
      "type_id": 1
    }
  }
  "mapping": [
    "case2test"
  ]
}
```

can be used to create a testrun for project with ID 666 using this commandline:

```bash
$ unitrail -u <user> -p <password> -m mapping.json -r /tmp/report.xml \
    -Dproject=666
    -Dtestrun.name="CLI defined testrun name"
    -Dtestrun.description="Description from CLI with $VARIABLE"
```
"""

setup(
    name='unitrail',
    version='0.0.5',
    description='CLI for autotests connection with Testrail',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mettizik/unitrail',
    author='Mokych Andrey',
    author_email='mokych.andrey@apriorit.com',
    keywords='testrail junit autotests report',
    packages=find_packages(exclude=['.vscode', '.sonarlint', 'docs', 'tests']),
    python_requires='>=3.0',
    install_requires=['junitparser', 'requests'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'unitrail=unitrail.__main__:main',
        ],
    }
)
