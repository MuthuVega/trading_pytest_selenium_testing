import pytest
from modules.tradingMod import v20_api
from modules.utilsMod import utils


@pytest.fixture(scope="function", autouse=False)
def api_client_with_invalid_api_key():
    api_client = v20_api.UserAccounts()
    api_client.api_key = "ABCD"
    api_client.set_headers()
    return api_client


class TestTradingAPI:
    """
    Test class to test OANDA v20 trading API's
    """
    user_acc_api_client = v20_api.UserAccounts()

    def test_get_user_accounts(self):
        acc_list = self.user_acc_api_client.get_account_list()
        utils.assert_response_code(
            response=self.user_acc_api_client.response, expected_code=200
        )

    def test_get_user_accounts_invalid_api_key(self, api_client_with_invalid_api_key):
        acc_list = api_client_with_invalid_api_key.get_account_list()
        utils.assert_response_code(
            response=api_client_with_invalid_api_key.response, expected_code=401
        )

    def test_get_account_details_valid_account(self):
        account_details = self.user_acc_api_client.get_account_details()
        utils.assert_response_code(
            response=self.user_acc_api_client.response, expected_code=200
        )
        assert (
            account_details["account"]["id"] == self.user_acc_api_client.active_account
        )

    def test_submit_limit_order(self):
        limit_order = v20_api.Orders(price=1.1)
        order_created = limit_order.submit_order()
        utils.assert_response_code(response=limit_order.response, expected_code=201)
        order_id = limit_order.get_order_id()
        order_details = limit_order.get_order_by_id(order_id=order_id)
        utils.assert_order_details(
            created_order=order_created, fetched_order=order_details
        )

    def test_submit_market_order(self):
        market_order = v20_api.Orders(
            order_type="MARKET", instrument="GBP_USD", units=15, time_in_force="FOK"
        )
        order_created = market_order.submit_order()
        utils.assert_response_code(response=market_order.response, expected_code=201)
        order_id = market_order.get_order_id()
        order_details = market_order.get_order_by_id(order_id=order_id)
        utils.assert_order_details(
            created_order=order_created, fetched_order=order_details
        )
