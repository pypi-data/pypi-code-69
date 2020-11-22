# encoding: utf-8
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Contact: Kyle Lahnakoski (kyle@lahnakoski.com)
#

from __future__ import absolute_import, division, unicode_literals

import json
import sys

PY3 = sys.version_info[0] == 3
PY2 = sys.version_info[0] == 2

PYPY = False
try:
    import __pypy__ as _

    PYPY = True
except Exception:
    PYPY = False


none_type = type(None)
boolean_type = type(True)

if PY3:
    try:
        STDOUT = sys.stdout.buffer
    except Exception as e:
        # WE HOPE WHATEVER REPLACED sys.stdout CAN HANDLE BYTES IN UTF8
        STDOUT = sys.stdout

    try:
        STDERR = sys.stderr.buffer
    except Exception as e:
        # WE HOPE WHATEVER REPLACED sys.stderr CAN HANDLE BYTES IN UTF8
        STDERR = sys.stderr

    import itertools
    from collections import OrderedDict, UserDict
    from collections.abc import Callable, Iterable, Mapping, Set, MutableMapping
    from functools import cmp_to_key, reduce, update_wrapper
    from configparser import ConfigParser
    from itertools import zip_longest
    import builtins as __builtin__
    from builtins import input

    try:
        from time import process_time
    except:
        from time import clock as process_time

    izip = zip
    zip_longest = itertools.zip_longest

    text = str
    text = str
    string_types = str
    binary_type = bytes
    integer_types = (int,)
    number_types = (int, float)
    long = int
    unichr = chr

    xrange = range

    def _gen():
        yield

    generator_types = (
        type(_gen()),
        type(filter(lambda x: True, [])),
        type({}.items()),
        type({}.values()),
        type(map(lambda: 0, iter([]))),
        type(reversed([])),
    )
    unichr = chr

    round = round
    from html.parser import HTMLParser
    from urllib.parse import urlparse
    from io import StringIO
    from io import BytesIO
    from _thread import allocate_lock, get_ident, start_new_thread, interrupt_main

    def items(d):
        return list(d.items())

    def iteritems(d):
        return d.items()

    def transpose(*args):
        return list(zip(*args))

    def get_function_name(func):
        return func.__name__

    def get_function_arguments(func):
        return func.__code__.co_varnames[: func.__code__.co_argcount]

    def get_function_code(func):
        return func.__code__

    def get_function_defaults(func):
        return func.__defaults__

    def sort_using_cmp(data, cmp):
        return sorted(data, key=cmp_to_key(cmp))

    def sort_using_key(data, key):
        return sorted(data, key=key)

    def first(values):
        try:
            return iter(values).__next__()
        except StopIteration:
            return None

    def NEXT(_iter):
        """
        RETURN next() FUNCTION, DO NOT CALL
        """
        return _iter.__next__

    def next(_iter):
        return _iter.__next__()

    def is_text(t):
        return t.__class__ is str

    def is_binary(b):
        return b.__class__ is bytes

    utf8_json_encoder = (
        json
        .JSONEncoder(
            skipkeys=False,
            ensure_ascii=False,  # DIFF FROM DEFAULTS
            check_circular=True,
            allow_nan=True,
            indent=None,
            separators=(",", ":"),
            default=None,
            sort_keys=True,  # <-- IMPORTANT!  sort_keys==True
        )
        .encode
    )


else:  # PY2
    STDOUT = sys.stdout
    STDERR = sys.stderr

    from collections import (
        Callable,
        Iterable,
        Mapping,
        Set,
        MutableMapping,
        OrderedDict,
    )
    from functools import cmp_to_key, reduce, update_wrapper

    import __builtin__
    from types import GeneratorType
    from ConfigParser import ConfigParser
    from itertools import izip_longest as zip_longest
    from __builtin__ import zip as transpose
    from itertools import izip
    from __builtin__ import raw_input as input

    from time import clock as process_time

    reduce = __builtin__.reduce
    text = __builtin__.unicode
    text = __builtin__.unicode
    string_types = (str, unicode)
    binary_type = str
    integer_types = (int, long)
    number_types = (int, long, float)
    long = __builtin__.long
    unichr = __builtin__.unichr

    xrange = __builtin__.xrange
    generator_types = (GeneratorType, type(reversed([])))
    unichr = __builtin__.unichr

    round = __builtin__.round
    import HTMLParser
    from urlparse import urlparse
    from StringIO import StringIO
    from io import BytesIO
    from thread import allocate_lock, get_ident, start_new_thread, interrupt_main

    def items(d):
        return d.items()

    def iteritems(d):
        return d.iteritems()

    def get_function_name(func):
        return func.func_name

    def get_function_arguments(func):
        return func.func_code.co_varnames[: func.func_code.co_argcount]

    def get_function_code(func):
        return func.func_code

    def get_function_defaults(func):
        return func.func_defaults

    def sort_using_cmp(data, cmp):
        return sorted(data, cmp=cmp)

    def sort_using_key(data, key):
        return sorted(data, key=key)

    def first(values):
        try:
            return iter(values).next()
        except StopIteration:
            return None

    def NEXT(_iter):
        """
        RETURN next() FUNCTION, DO NOT CALL
        """
        return _iter.next

    def next(_iter):
        return _iter.next()

    def is_text(t):
        return t.__class__ is unicode

    def is_binary(b):
        return b.__class__ is str

    utf8_json_encoder = (
        json
        .JSONEncoder(
            skipkeys=False,
            ensure_ascii=False,  # DIFF FROM DEFAULTS
            check_circular=True,
            allow_nan=True,
            indent=None,
            separators=(",", ":"),
            encoding="utf-8",  # DIFF FROM DEFAULTS
            default=None,
            sort_keys=True,  # <-- IMPORTANT!  sort_keys==True
        )
        .encode
    )

    # COPIED FROM Python's collections.UserDict (copied July 2018)
    class UserDict(MutableMapping):

        # Start by filling-out the abstract methods
        def __init__(*args, **kwargs):
            if not args:
                raise TypeError(
                    "descriptor '__init__' of 'UserDict' object needs an argument"
                )
            self, args = args[0], args[1:]
            if len(args) > 1:
                raise TypeError("expected at most 1 arguments, got %d" % len(args))
            if args:
                dict = args[0]
            elif "dict" in kwargs:
                dict = kwargs.pop("dict")
                import warnings

                warnings.warn(
                    "Passing 'dict' as keyword argument is deprecated",
                    DeprecationWarning,
                    stacklevel=2,
                )
            else:
                dict = None
            self.data = {}
            if dict is not None:
                self.update(dict)
            if len(kwargs):
                self.update(kwargs)

        def __len__(self):
            return len(self.data)

        def __getitem__(self, key):
            if key in self.data:
                return self.data[key]
            if hasattr(self.__class__, "__missing__"):
                return self.__class__.__missing__(self, key)
            raise KeyError(key)

        def __setitem__(self, key, item):
            self.data[key] = item

        def __delitem__(self, key):
            del self.data[key]

        def __iter__(self):
            return iter(self.data)

        # Modify __contains__ to work correctly when __missing__ is present
        def __contains__(self, key):
            return key in self.data

        # Now, add the methods in dicts but not in MutableMapping
        def __repr__(self):
            return repr(self.data)

        def copy(self):
            if self.__class__ is UserDict:
                return UserDict(self.data.copy())
            import copy

            data = self.data
            try:
                self.data = {}
                c = copy.copy(self)
            finally:
                self.data = data
            c.update(self)
            return c

        @classmethod
        def fromkeys(cls, iterable, value=None):
            d = cls()
            for key in iterable:
                d[key] = value
            return d


function_type = (lambda: None).__class__


class decorate(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, caller):
        """
        :param caller: A METHOD THAT IS EXPECTED TO CALL func
        :return: caller, BUT WITH SIGNATURE OF  self.func
        """
        return update_wrapper(caller, self.func)


def flatten(items):
    return (vv for v in items for vv in v)


_keep_imports = (
    ConfigParser,
    zip_longest,
    reduce,
    transpose,
    izip,
    HTMLParser,
    urlparse,
    StringIO,
    BytesIO,
    allocate_lock,
    get_ident,
    start_new_thread,
    interrupt_main,
    process_time,
)
