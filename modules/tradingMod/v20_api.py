import os
import requests
from modules.tradingMod.endPoints import APITradingEndPoints
from settings import BASE_URL, ACTIVE_ACCOUNT

API_KEY = os.environ.get("OANDA_DEMO_API_KEY")


class TradingAPI:
    """
    OANDA v20 Trading API class
    """
    def __init__(self, base_url=BASE_URL, api_key=API_KEY):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        self.active_account = ACTIVE_ACCOUNT
        self.end_point = None
        self.response = None

    def set_headers(self):
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

    def send_request(self, end_point=None, method="GET", params=None, payload=None):
        # send the request to the server and return the resp
        url = f"{self.base_url}{end_point}"
        if method == "GET":
            response = requests.get(url=url, headers=self.headers)
        elif method == "POST":
            response = requests.post(url=url, headers=self.headers, json=payload)
        return response


class UserAccounts(TradingAPI):
    def __init__(self):
        super(UserAccounts, self).__init__()

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
    def __init__(
        self,
        order_type="LIMIT",
        instrument="GBP_USD",
        units=10,
        price=None,
        time_in_force="GTC",
        position_fill="DEFAULT",
    ):
        super(Orders, self).__init__()
        self.order_type = order_type
        self.instrument = instrument
        self.units = units
        self.price = price
        self.time_in_force = time_in_force
        self.position_fill = position_fill
        self.payload = None

    def build_payload(self):
        order_details = {}
        order_payload = {}
        order_details["type"] = self.order_type
        order_details["instrument"] = self.instrument
        order_details["units"] = self.units
        order_details["time_in_force"] = self.time_in_force
        order_details["position_fill"] = self.position_fill
        if self.order_type == "LIMIT":
            order_details["price"] = self.price
        order_payload["order"] = order_details
        self.payload = order_payload

    def submit_order(self):
        self.end_point = APITradingEndPoints.submit_order
        self.end_point = self.end_point.format(accountID=self.active_account)
        self.build_payload()
        self.response = self.send_request(
            end_point=self.end_point, method="POST", payload=self.payload
        )
        return self.response.json()

    def get_order_id(self):
        return self.response.json()["orderCreateTransaction"]["id"]

    def get_order_by_id(self, order_id):
        self.end_point = APITradingEndPoints.get_order
        self.end_point = self.end_point.format(accountID=self.active_account)
        self.end_point = self.end_point.format(orderSpecifier=order_id)
        response = self.send_request(end_point=self.end_point)
        return response.json()
