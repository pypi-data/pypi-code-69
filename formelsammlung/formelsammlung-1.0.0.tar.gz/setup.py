# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['formelsammlung']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>1.6'],
 'docs': ['sphinx>=3.2,<4.0',
          'sphinx-rtd-theme>=0.5,<0.6',
          'sphinx-autodoc-typehints>=1.11.0,<2.0.0',
          'sphinxcontrib-apidoc>=0.3.0,<0.4.0'],
 'flask': ['flask>=1.1.2,<2.0.0'],
 'pre-commit': ['pre-commit>=2.7,<3.0', 'mypy==0.782', 'pylint>=2.6.0,<3.0.0'],
 'testing': ['pytest>=6,<7',
             'pytest-xdist>=1.34,<2.0',
             'pytest-cov>=2.10,<3.0',
             'coverage[toml]>=5.2.1,<6.0.0',
             'pytest-sugar>=0.9.4,<0.10.0',
             'pytest-randomly>=3.4,<4.0',
             'pytest-flask>=1.0,<2.0']}

entry_points = \
{'console_scripts': ['env_exe_runner = '
                     'formelsammlung.env_exe_runner:cli_caller']}

setup_kwargs = {
    'name': 'formelsammlung',
    'version': '1.0.0',
    'description': 'Collection of different functions',
    'long_description': "==============\nformelsammlung\n==============\n\n+---------------+----------------------------------------------------------------------+\n| **General**   | |maintenance| |license| |black| |rtd|                                |\n+---------------+----------------------------------------------------------------------+\n| **Pipeline**  | |azure_pipeline| |azure_coverage|                                    |\n+---------------+----------------------------------------------------------------------+\n| **Tools**     | |poetry| |tox| |pytest| |sphinx|                                     |\n+---------------+----------------------------------------------------------------------+\n| **VC**        | |vcs| |gpg| |semver| |pre-commit|                                    |\n+---------------+----------------------------------------------------------------------+\n| **Github**    | |gh_release| |gh_commits_since| |gh_last_commit|                     |\n|               +----------------------------------------------------------------------+\n|               | |gh_stars| |gh_forks| |gh_contributors| |gh_watchers|                |\n+---------------+----------------------------------------------------------------------+\n| **PyPI**      | |pypi_release| |pypi_py_versions| |pypi_implementations|             |\n|               +----------------------------------------------------------------------+\n|               | |pypi_status| |pypi_format| |pypi_downloads|                         |\n+---------------+----------------------------------------------------------------------+\n\n\n**Collection of different multipurpose functions.**\n\nThis library is a collection of different functions I developed which I use in different\nprojects so I put them here.\n\n\nFunctionality\n=============\n\n- ``getenv_typed()``: is a wrapper around ``os.getenv`` returning the value of the environment variable in the correct python type.\n- ``calculate_string()``: takes an arithmetic expression as a string and calculates it.\n- ``SphinxDocServer``: is a flask plugin to serve the repository's docs build as HTML (by sphinx). Needs ``flask`` extra to be also installed to work.\n- ``env_exe_runner()``: is a function to call a given ``tool`` from the first tox/nox environments that has it installed in a list of tox/nox environments.\n\n\nPrerequisites\n=============\n\n*Works only with python version >= 3.6*\n\nA new version of ``pip`` that supports PEP-517/PEP-518 is required.\nWhen the setup fails try updating ``pip``.\n\n\nDisclaimer\n==========\n\nNo active maintenance is intended for this project.\nYou may leave an issue if you have a questions, bug report or feature request,\nbut I cannot promise a quick response time.\n\n\n.. .############################### LINKS ###############################\n\n\n.. General\n.. |maintenance| image:: https://img.shields.io/badge/No%20Maintenance%20Intended-X-red.svg?style=flat-square\n    :target: http://unmaintained.tech/\n    :alt: Maintenance - not intended\n\n.. |license| image:: https://img.shields.io/github/license/Cielquan/formelsammlung.svg?style=flat-square&label=License\n    :alt: License\n    :target: https://github.com/Cielquan/formelsammlung/blob/master/LICENSE.txt\n\n.. |black| image:: https://img.shields.io/badge/Code%20Style-black-000000.svg?style=flat-square\n    :alt: Code Style - Black\n    :target: https://github.com/psf/black\n\n.. |rtd| image:: https://img.shields.io/readthedocs/formelsammlung/latest.svg?style=flat-square&logo=read-the-docs&logoColor=white&label=Read%20the%20Docs\n    :alt: Read the Docs - Build Status (latest)\n    :target: https://formelsammlung.readthedocs.io/en/latest/\n\n\n.. Pipeline\n.. |azure_pipeline| image:: https://img.shields.io/azure-devops/build/cielquan/05507266-5d2e-4862-80f9-9f2b439814c8/8?style=flat-square&logo=azure-pipelines&label=Azure%20Pipelines\n    :target: https://dev.azure.com/cielquan/formelsammlung/_build/latest?definitionId=8&branchName=master\n    :alt: Azure DevOps builds\n\n.. |azure_coverage| image:: https://img.shields.io/azure-devops/coverage/cielquan/formelsammlung/8?style=flat-square&logo=azure-pipelines&label=Coverage\n    :target: https://dev.azure.com/cielquan/formelsammlung/_build/latest?definitionId=8&branchName=master\n    :alt: Azure DevOps Coverage\n\n\n.. Tools\n.. |poetry| image:: https://img.shields.io/badge/Packaging-poetry-brightgreen.svg?style=flat-square\n    :target: https://python-poetry.org/\n    :alt: Poetry\n\n.. |tox| image:: https://img.shields.io/badge/Automation-tox-brightgreen.svg?style=flat-square\n    :target: https://tox.readthedocs.io/en/latest/\n    :alt: tox\n\n.. |pytest| image:: https://img.shields.io/badge/Test%20framework-pytest-brightgreen.svg?style=flat-square\n    :target: https://docs.pytest.org/en/latest/\n    :alt: Pytest\n\n.. |sphinx| image:: https://img.shields.io/badge/Doc%20builder-sphinx-brightgreen.svg?style=flat-square\n    :target: https://www.sphinx-doc.org/\n    :alt: Sphinx\n\n\n.. VC\n.. |vcs| image:: https://img.shields.io/badge/VCS-git-orange.svg?style=flat-square&logo=git\n    :target: https://git-scm.com/\n    :alt: VCS\n\n.. |gpg| image:: https://img.shields.io/badge/GPG-signed-blue.svg?style=flat-square&logo=gnu-privacy-guard\n    :target: https://gnupg.org/\n    :alt: Website\n\n.. |semver| image:: https://img.shields.io/badge/Versioning-semantic-brightgreen.svg?style=flat-square\n    :alt: Versioning - semantic\n    :target: https://semver.org/\n\n.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=flat-square&logo=pre-commit&logoColor=yellow\n    :target: https://github.com/pre-commit/pre-commit\n    :alt: pre-commit\n\n\n.. Github\n.. |gh_release| image:: https://img.shields.io/github/v/release/Cielquan/formelsammlung.svg?style=flat-square&logo=github\n    :alt: Github - Latest Release\n    :target: https://github.com/Cielquan/formelsammlung/releases/latest\n\n.. |gh_commits_since| image:: https://img.shields.io/github/commits-since/Cielquan/formelsammlung/latest.svg?style=flat-square&logo=github\n    :alt: Github - Commits since latest release\n    :target: https://github.com/Cielquan/formelsammlung/commits/master\n\n.. |gh_last_commit| image:: https://img.shields.io/github/last-commit/Cielquan/formelsammlung.svg?style=flat-square&logo=github\n    :alt: Github - Last Commit\n    :target: https://github.com/Cielquan/formelsammlung/commits/master\n\n.. |gh_stars| image:: https://img.shields.io/github/stars/Cielquan/formelsammlung.svg?style=flat-square&logo=github\n    :alt: Github - Stars\n    :target: https://github.com/Cielquan/formelsammlung/stargazers\n\n.. |gh_forks| image:: https://img.shields.io/github/forks/Cielquan/formelsammlung.svg?style=flat-square&logo=github\n    :alt: Github - Forks\n    :target: https://github.com/Cielquan/formelsammlung/network/members\n\n.. |gh_contributors| image:: https://img.shields.io/github/contributors/Cielquan/formelsammlung.svg?style=flat-square&logo=github\n    :alt: Github - Contributors\n    :target: https://github.com/Cielquan/formelsammlung/graphs/contributors\n\n.. |gh_watchers| image:: https://img.shields.io/github/watchers/Cielquan/formelsammlung.svg?style=flat-square&logo=github\n    :alt: Github - Watchers\n    :target: https://github.com/Cielquan/formelsammlung/watchers\n\n\n.. PyPI\n.. |pypi_release| image:: https://img.shields.io/pypi/v/formelsammlung.svg?style=flat-square&logo=pypi&logoColor=FBE072\n    :alt: PyPI - Package latest release\n    :target: https://pypi.org/project/formelsammlung/\n\n.. |pypi_py_versions| image:: https://img.shields.io/pypi/pyversions/formelsammlung.svg?style=flat-square&logo=python&logoColor=FBE072\n    :alt: PyPI - Supported Python Versions\n    :target: https://pypi.org/project/formelsammlung/\n\n.. |pypi_implementations| image:: https://img.shields.io/pypi/implementation/formelsammlung.svg?style=flat-square&logo=python&logoColor=FBE072\n    :alt: PyPI - Supported Implementations\n    :target: https://pypi.org/project/formelsammlung/\n\n.. |pypi_status| image:: https://img.shields.io/pypi/status/formelsammlung.svg?style=flat-square&logo=pypi&logoColor=FBE072\n    :alt: PyPI - Stability\n    :target: https://pypi.org/project/formelsammlung/\n\n.. |pypi_format| image:: https://img.shields.io/pypi/format/formelsammlung.svg?style=flat-square&logo=pypi&logoColor=FBE072\n    :alt: PyPI - Format\n    :target: https://pypi.org/project/formelsammlung/\n\n.. |pypi_downloads| image:: https://img.shields.io/pypi/dm/formelsammlung.svg?style=flat-square&logo=pypi&logoColor=FBE072\n    :target: https://pypi.org/project/formelsammlung/\n    :alt: PyPI - Monthly downloads\n",
    'author': 'Cielquan',
    'author_email': 'cielquan@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Cielquan/formelsammlung',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
