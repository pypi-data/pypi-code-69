# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.17
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cfbd.api_client import ApiClient


class RecruitingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_recruiting_groups(self, **kwargs):  # noqa: E501
        """Recruit position group ratings  # noqa: E501

        Gets a list of aggregated statistics by team and position grouping  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_recruiting_groups(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int start_year: Starting year
        :param int end_year: Ending year
        :param str team: Team filter
        :param str conference: conference filter
        :return: list[PositionGroupRecruitingRating]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_recruiting_groups_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_recruiting_groups_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_recruiting_groups_with_http_info(self, **kwargs):  # noqa: E501
        """Recruit position group ratings  # noqa: E501

        Gets a list of aggregated statistics by team and position grouping  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_recruiting_groups_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int start_year: Starting year
        :param int end_year: Ending year
        :param str team: Team filter
        :param str conference: conference filter
        :return: list[PositionGroupRecruitingRating]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_year', 'end_year', 'team', 'conference']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_recruiting_groups" % key
                )
            params[key] = val
        del params['kwargs']

        if 'start_year' in params and params['start_year'] < 2000:  # noqa: E501
            raise ValueError("Invalid value for parameter `start_year` when calling `get_recruiting_groups`, must be a value greater than or equal to `2000`")  # noqa: E501
        if 'end_year' in params and params['end_year'] < 2000:  # noqa: E501
            raise ValueError("Invalid value for parameter `end_year` when calling `get_recruiting_groups`, must be a value greater than or equal to `2000`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_year' in params:
            query_params.append(('startYear', params['start_year']))  # noqa: E501
        if 'end_year' in params:
            query_params.append(('endYear', params['end_year']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'conference' in params:
            query_params.append(('conference', params['conference']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/recruiting/groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PositionGroupRecruitingRating]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_recruiting_players(self, **kwargs):  # noqa: E501
        """Player recruiting ratings and rankings  # noqa: E501

        Get player recruiting rankings and data. Requires either a year or team to be specified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_recruiting_players(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Recruiting class year (required if team no specified)
        :param str classification: Type of recruit (HighSchool, JUCO, PrepSchool)
        :param str position: Position abbreviation filter
        :param str state: State or province abbreviation filter
        :param str team: Committed team filter (required if year not specified)
        :return: list[Recruit]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_recruiting_players_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_recruiting_players_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_recruiting_players_with_http_info(self, **kwargs):  # noqa: E501
        """Player recruiting ratings and rankings  # noqa: E501

        Get player recruiting rankings and data. Requires either a year or team to be specified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_recruiting_players_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Recruiting class year (required if team no specified)
        :param str classification: Type of recruit (HighSchool, JUCO, PrepSchool)
        :param str position: Position abbreviation filter
        :param str state: State or province abbreviation filter
        :param str team: Committed team filter (required if year not specified)
        :return: list[Recruit]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'classification', 'position', 'state', 'team']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_recruiting_players" % key
                )
            params[key] = val
        del params['kwargs']

        if 'year' in params and params['year'] < 2000:  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_recruiting_players`, must be a value greater than or equal to `2000`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'classification' in params:
            query_params.append(('classification', params['classification']))  # noqa: E501
        if 'position' in params:
            query_params.append(('position', params['position']))  # noqa: E501
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/recruiting/players', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Recruit]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_recruiting_teams(self, **kwargs):  # noqa: E501
        """Team recruiting rankings and ratings  # noqa: E501

        Team recruiting rankings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_recruiting_teams(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Recruiting class year
        :param str team: Team filter
        :return: list[TeamRecruitingRank]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_recruiting_teams_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_recruiting_teams_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_recruiting_teams_with_http_info(self, **kwargs):  # noqa: E501
        """Team recruiting rankings and ratings  # noqa: E501

        Team recruiting rankings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_recruiting_teams_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Recruiting class year
        :param str team: Team filter
        :return: list[TeamRecruitingRank]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'team']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_recruiting_teams" % key
                )
            params[key] = val
        del params['kwargs']

        if 'year' in params and params['year'] < 2000:  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_recruiting_teams`, must be a value greater than or equal to `2000`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/recruiting/teams', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TeamRecruitingRank]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
