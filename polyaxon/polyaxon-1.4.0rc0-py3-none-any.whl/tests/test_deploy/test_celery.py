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

from marshmallow import ValidationError

from polyaxon.deploy.schemas.celery import CeleryConfig
from tests.utils import BaseTestCase


class TestCeleryConfig(BaseTestCase):
    def test_celery_config(self):
        config_dict = {
            "confirmPublish": 12,
            "workerPrefetchMultiplier": "foo",
            "workerMaxTasksPerChild": 123,
            "workerMaxMemoryPerChild": 123,
        }
        with self.assertRaises(ValidationError):
            CeleryConfig.from_dict(config_dict)

        config_dict = {
            "taskTrackStarted": True,
            "brokerPoolLimit": 123,
            "confirmPublish": True,
            "workerPrefetchMultiplier": 4,
            "workerMaxTasksPerChild": 123,
            "workerMaxMemoryPerChild": 123,
        }
        config = CeleryConfig.from_dict(config_dict)
        assert config.to_light_dict() == config_dict

        config_dict = {"confirmPublish": True, "workerMaxMemoryPerChild": 123}
        config = CeleryConfig.from_dict(config_dict)
        assert config.to_light_dict() == config_dict
