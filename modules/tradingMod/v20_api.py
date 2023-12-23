import os
import requests
from modules.tradingMod.endPoints import APITradingEndPoints
from settings import BASE_URL, ACTIVE_ACCOUNT

API_KEY = os.environ.get("OANDA_DEMO_API_KEY")


class TradingAPI:
    def __init__(self, base_url=BASE_URL, api_key=API_KEY):
        self.base_url = base_url
        self.headers = headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }
        self.active_account = ACTIVE_ACCOUNT

    def set_headers(self):
        self.headers = {}

    def send_request(self, end_point=None, method="GET", params=None, payload=None):
        # send the request to the server and return the resp
        url = f"{self.base_url}{end_point}"
        response = requests.get(url=url, headers=self.headers)
        return response


class UserAccounts(TradingAPI):
    def __init__(self):
        super(UserAccounts, self).__init__()
        self.end_point = None
        self.response = None

    def get_account_list(self):
        self.end_point = APITradingEndPoints.accounts_list
        self.response = self.send_request(end_point=self.end_point)
        return self.response.json()

    def get_account_details(self):
        self.end_point = APITradingEndPoints.acc_details
        self.end_point = self.end_point.format(accountID=self.active_account)
        self.response = self.send_request(end_point=self.end_point)
        return self.response.json()

    def get_account_summary(self):
        self.end_point = APITradingEndPoints.acc_summary
        self.end_point = self.end_point.format(accountID=self.active_account)
        self.response = self.send_request(end_point=self.end_point)
        return self.response.json()


class Orders(TradingAPI):
    pass


class LimitOrders(Orders):
    pass


class MarKetOrders(Orders):
    pass
