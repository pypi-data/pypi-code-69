# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.17
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.api.rankings_api import RankingsApi  # noqa: E501
from cfbd.rest import ApiException


class TestRankingsApi(unittest.TestCase):
    """RankingsApi unit test stubs"""

    def setUp(self):
        self.api = cfbd.api.rankings_api.RankingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_rankings(self):
        """Test case for get_rankings

        Historical polls and rankings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
