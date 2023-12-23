import logging
from modules.utilsMod import utils


def test_get_user_account(v20_user_acc_api_client):
    user_accounts = v20_user_acc_api_client.get_account_list()
    utils.assert_response_code(
        response=v20_user_acc_api_client.response, expected_code=200
    )
    logging.info(f"Accounts are {user_accounts}")
    assert len(user_accounts["accounts"]) >= 2


def test_get_user_account_details(v20_user_acc_api_client):
    account_details = v20_user_acc_api_client.get_account_details()
    utils.assert_response_code(
        response=v20_user_acc_api_client.response, expected_code=200
    )
    logging.info(f"Account details are {account_details}")
    assert account_details["account"]["id"] == v20_user_acc_api_client.active_account
    # TODO: A lot more fields can be asserted here ...


def test_get_user_account_details_with_invalid_account(v20_user_acc_api_client):
    v20_user_acc_api_client.active_account = "ABCD"
    account_details = v20_user_acc_api_client.get_account_details()
    utils.assert_response_code(
        response=v20_user_acc_api_client.response, expected_code=400
    )
    assert account_details["errorMessage"] == "Invalid value specified for 'accountID'"


def test_get_user_summary(v20_user_acc_api_client):
    account_summary = v20_user_acc_api_client.get_account_summary()
    utils.assert_response_code(
        response=v20_user_acc_api_client.response, expected_code=200
    )
    logging.info(f"Account details are {account_summary}")
    assert account_summary["account"]["id"] == v20_user_acc_api_client.active_account
    # TODO: A lot more fields can be asserted here ...
