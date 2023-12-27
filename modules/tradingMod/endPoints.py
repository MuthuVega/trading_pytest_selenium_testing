class APITradingEndPoints:
    """
    Class to store the OANDA v20 API end point details
    """

    accounts_list = "/v3/accounts"
    acc_details = "/v3/accounts/{accountID}"
    acc_summary = "/v3/accounts/{accountID}/summary"
    submit_order = "/v3/accounts/{accountID}/orders"
    get_order = "/v3/accounts/{accountID}/orders/{{orderSpecifier}}"
