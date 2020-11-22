# coding: utf-8

"""
    Stencila Hub API

    # Authentication  Many endpoints in the Stencila Hub API require an authentication token. These tokens carry many privileges, so be sure to keep them secure. Do not place your tokens in publicly accessible areas such as client-side code. The API is only served over HTTPS to avoid exposing tokens and other data on the network.  To obtain a token, [`POST /api/tokens`](#operations-tokens-tokens_create) with either a `username` and `password` pair, or an [OpenID Connect](https://openid.net/connect/) token. Then use the token in the `Authorization` header of subsequent requests with the prefix `Token` e.g.      curl -H \"Authorization: Token 48866b1e38a2e9db0baada2140b2327937f4a3636dd5f2dfd8c212341c88d34\" https://hub.stenci.la/api/projects/  Alternatively, you can use `Basic` authentication with the token used as the username and no password. This can be more convenient when using command line tools such as [cURL](https://curl.haxx.se/) e.g.      curl -u 48866b1e38a2e9db0baada2140b2327937f4a3636dd5f2dfd8c212341c88d34: https://hub.stenci.la/api/projects/  Or, the less ubiquitous, but more accessible [httpie](https://httpie.org/):      http --auth 48866b1e38a2e9db0baada2140b2327937f4a3636dd5f2dfd8c212341c88d34: https://hub.stenci.la/api/projects/  In both examples above, the trailing colon is not required but avoids being asked for a password.  # Versioning  The Stencila Hub is released using semantic versioning. The current version is available from the [`GET /api/status`](/api/status) endpoint. Please see the [Github release page](https://github.com/stencila/hub/releases) and the [changelog](https://github.com/stencila/hub/blob/master/CHANGELOG.md) for details on each release. We currently do not provide versioning of the API but plan to do so soon (probably by using a `Accept: application/vnd.stencila.hub+json;version=1.0` request header). If you are using, or interested in using, the API please contact us and we may be able to expedite this.   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import stencila.hub
from stencila.hub.api.accounts_api import AccountsApi  # noqa: E501
from stencila.hub.rest import ApiException


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self):
        self.api = stencila.hub.api.accounts_api.AccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accounts_broker_list(self):
        """Test case for accounts_broker_list

        Connect to the job broker for the account.  # noqa: E501
        """
        pass

    def test_accounts_create(self):
        """Test case for accounts_create

        Create an object.  # noqa: E501
        """
        pass

    def test_accounts_list(self):
        """Test case for accounts_list

        List objects.  # noqa: E501
        """
        pass

    def test_accounts_partial_update(self):
        """Test case for accounts_partial_update

        Update an object.  # noqa: E501
        """
        pass

    def test_accounts_queues_list(self):
        """Test case for accounts_queues_list

        List objects.  # noqa: E501
        """
        pass

    def test_accounts_queues_read(self):
        """Test case for accounts_queues_read

        Retrieve an object.  # noqa: E501
        """
        pass

    def test_accounts_read(self):
        """Test case for accounts_read

        Retrieve an object.  # noqa: E501
        """
        pass

    def test_accounts_teams_create(self):
        """Test case for accounts_teams_create

        Create a team.  # noqa: E501
        """
        pass

    def test_accounts_teams_delete(self):
        """Test case for accounts_teams_delete

        Destroy a team.  # noqa: E501
        """
        pass

    def test_accounts_teams_list(self):
        """Test case for accounts_teams_list

        List teams.  # noqa: E501
        """
        pass

    def test_accounts_teams_members_create(self):
        """Test case for accounts_teams_members_create

        """
        pass

    def test_accounts_teams_members_delete(self):
        """Test case for accounts_teams_members_delete

        """
        pass

    def test_accounts_teams_partial_update(self):
        """Test case for accounts_teams_partial_update

        Update a team.  # noqa: E501
        """
        pass

    def test_accounts_teams_read(self):
        """Test case for accounts_teams_read

        Retrieve a team.  # noqa: E501
        """
        pass

    def test_accounts_update_plan(self):
        """Test case for accounts_update_plan

        """
        pass

    def test_accounts_users_create(self):
        """Test case for accounts_users_create

        Add an account user.  # noqa: E501
        """
        pass

    def test_accounts_users_delete(self):
        """Test case for accounts_users_delete

        Remove an account user.  # noqa: E501
        """
        pass

    def test_accounts_users_list(self):
        """Test case for accounts_users_list

        A view set for account users.  # noqa: E501
        """
        pass

    def test_accounts_users_partial_update(self):
        """Test case for accounts_users_partial_update

        A view set for account users.  # noqa: E501
        """
        pass

    def test_accounts_users_read(self):
        """Test case for accounts_users_read

        A view set for account users.  # noqa: E501
        """
        pass

    def test_accounts_workers_heartbeats_list(self):
        """Test case for accounts_workers_heartbeats_list

        List objects.  # noqa: E501
        """
        pass

    def test_accounts_workers_list(self):
        """Test case for accounts_workers_list

        List objects.  # noqa: E501
        """
        pass

    def test_accounts_workers_read(self):
        """Test case for accounts_workers_read

        Retrieve an object.  # noqa: E501
        """
        pass

    def test_accounts_zones_create(self):
        """Test case for accounts_zones_create

        Create an object.  # noqa: E501
        """
        pass

    def test_accounts_zones_delete(self):
        """Test case for accounts_zones_delete

        Destroy an object.  # noqa: E501
        """
        pass

    def test_accounts_zones_list(self):
        """Test case for accounts_zones_list

        List objects.  # noqa: E501
        """
        pass

    def test_accounts_zones_read(self):
        """Test case for accounts_zones_read

        Retrieve an object.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
