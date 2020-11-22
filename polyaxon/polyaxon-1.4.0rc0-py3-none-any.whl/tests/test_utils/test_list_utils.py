#!/usr/bin/python
#
# Copyright 2018-2020 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from polyaxon.utils.list_utils import to_list
from tests.utils import BaseTestCase


class ToListTest(BaseTestCase):
    def test_to_list(self):
        assert to_list(None) == [None]
        assert to_list(None, check_none=True) == []
        assert to_list([]) == []
        assert to_list(()) == []
        assert to_list([1, 3]) == [1, 3]
        assert to_list((1, 3)) == [1, 3]
        assert to_list(1) == [1]
        assert to_list("foo") == ["foo"]
