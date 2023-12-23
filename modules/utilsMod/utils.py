import pytest


def assert_response_code(response=None, expected_code=200):
    assert response.status_code == expected_code
