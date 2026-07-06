from datetime import datetime

from backend.history.base_history import BaseHistoryProvider
from backend.broker.angelone.auth import AngelAuth
from backend.market.token_search import TokenSearch


class AngelHistoryProvider(BaseHistoryProvider):

    def __init__(self):
        self.auth = AngelAuth()
        self.tokens = TokenSearch()

    def login(self):
        self.auth.login()

    def download(
        self,
        symbol: str,
        interval: str,
        start: datetime,
        end: datetime,
    ):

        item = self.tokens.exact(symbol)

        if not item:
            raise Exception(f"Symbol not found: {symbol}")

        params = {
            "exchange": item["exch_seg"],
            "symboltoken": item["token"],
            "interval": interval,
            "fromdate": start.strftime("%Y-%m-%d %H:%M"),
            "todate": end.strftime("%Y-%m-%d %H:%M"),
        }

        api = self.auth.get_api()

        response = api.getCandleData(params)

        if not response.get("status"):
            raise Exception(response.get("message"))

        return response.get("data", [])
