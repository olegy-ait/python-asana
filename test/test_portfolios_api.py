# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import asana
from asana.api.portfolios_api import PortfoliosApi  # noqa: E501
from asana.rest import ApiException


class TestPortfoliosApi(unittest.TestCase):
    """PortfoliosApi unit test stubs"""

    def setUp(self):
        self.api = PortfoliosApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_custom_field_setting_for_portfolio(self):
        """Test case for add_custom_field_setting_for_portfolio

        Add a custom field to a portfolio  # noqa: E501
        """
        pass

    def test_add_item_for_portfolio(self):
        """Test case for add_item_for_portfolio

        Add a portfolio item  # noqa: E501
        """
        pass

    def test_add_members_for_portfolio(self):
        """Test case for add_members_for_portfolio

        Add users to a portfolio  # noqa: E501
        """
        pass

    def test_create_portfolio(self):
        """Test case for create_portfolio

        Create a portfolio  # noqa: E501
        """
        pass

    def test_delete_portfolio(self):
        """Test case for delete_portfolio

        Delete a portfolio  # noqa: E501
        """
        pass

    def test_get_items_for_portfolio(self):
        """Test case for get_items_for_portfolio

        Get portfolio items  # noqa: E501
        """
        pass

    def test_get_portfolio(self):
        """Test case for get_portfolio

        Get a portfolio  # noqa: E501
        """
        pass

    def test_get_portfolios(self):
        """Test case for get_portfolios

        Get multiple portfolios  # noqa: E501
        """
        pass

    def test_remove_custom_field_setting_for_portfolio(self):
        """Test case for remove_custom_field_setting_for_portfolio

        Remove a custom field from a portfolio  # noqa: E501
        """
        pass

    def test_remove_item_for_portfolio(self):
        """Test case for remove_item_for_portfolio

        Remove a portfolio item  # noqa: E501
        """
        pass

    def test_remove_members_for_portfolio(self):
        """Test case for remove_members_for_portfolio

        Remove users from a portfolio  # noqa: E501
        """
        pass

    def test_update_portfolio(self):
        """Test case for update_portfolio

        Update a portfolio  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()