"""
Utility functions
"""

import pytest


def assert_response_code(response=None, expected_code=200):
    assert response.status_code == expected_code


def assert_order_details(created_order=None, fetched_order=None):
    assert created_order["orderCreateTransaction"]["id"] == fetched_order["order"]["id"]
    assert (
        created_order["orderCreateTransaction"]["instrument"]
        == fetched_order["order"]["instrument"]
    )
    assert (
        created_order["orderCreateTransaction"]["units"]
        == fetched_order["order"]["units"]
    )
    if created_order["orderCreateTransaction"]["type"] != "MARKET_ORDER":
        assert (
            created_order["orderCreateTransaction"]["price"]
            == fetched_order["order"]["price"]
        )
    assert (
        created_order["orderCreateTransaction"]["timeInForce"]
        == fetched_order["order"]["timeInForce"]
    )


