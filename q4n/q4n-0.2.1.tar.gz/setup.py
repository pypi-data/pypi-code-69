# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
name = "q4n",
version = "0.2.1",
keywords = ("pwn"),
description = "my pwntools",
license = "MIT Licence",

url = "https://github.com/Q4n/mypwn",
author = "Q4n",
author_email = "907659303@qq.com",

packages = find_packages(),
include_package_data = True,
platforms = "any",
python_requires='>=3',
install_requires = ["pwntools","pycrypto"]
)
