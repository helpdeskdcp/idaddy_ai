from backend.broker.angelone.auth import AngelAuth
from backend.market.token_search import TokenSearch


class MarketDataService:

    def __init__(self):
        self.auth = AngelAuth()
        self.auth.login()
        self.api = self.auth.api
        self.tokens = TokenSearch()

    def get_profile(self):
        return self.auth.get_profile()

    def get_token(self, symbol: str):
        return self.tokens.exact(symbol)

    def get_future(self, symbol: str):
        return self.tokens.nearest_future(symbol)

    def get_ltp(self, exchange: str, tradingsymbol: str, token: str):
        return self.api.ltpData(
            exchange,
            tradingsymbol,
            token
        )
