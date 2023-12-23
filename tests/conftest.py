import pytest
from modules.tradingMod import v20_api


@pytest.fixture(scope="function", autouse=False)
def v20_user_acc_api_client():
    yield v20_api.UserAccounts()
