from backend.market.token_search import TokenSearch
from backend.market.market_data import MarketDataService


class OptionChainService:

    def __init__(self):
        self.tokens = TokenSearch()
        self.market = MarketDataService()

    def atm_strike(self, symbol: str, step: int = 50):
        fut = self.market.get_future(symbol)

        ltp = self.market.get_ltp(
            fut["exch_seg"],
            fut["symbol"],
            fut["token"],
        )["data"]["ltp"]

        return int(round(ltp / step) * step)

    def options(self, symbol: str, strike: int):
        symbol = symbol.upper()

        ce = []
        pe = []

        for item in self.tokens.data:

            if item.get("instrumenttype") != "OPTIDX":
                continue

            if item.get("name", "").upper() != symbol:
                continue

            try:
                item_strike = int(float(item["strike"]) / 100)
            except Exception:
                continue

            if item_strike != strike:
                continue

            if item["symbol"].endswith("CE"):
                ce.append(item)

            elif item["symbol"].endswith("PE"):
                pe.append(item)

        return {
            "CE": sorted(ce, key=lambda x: x["expiry"]),
            "PE": sorted(pe, key=lambda x: x["expiry"]),
        }
