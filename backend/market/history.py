from datetime import datetime, timedelta

import pandas as pd

from backend.market.market_data import MarketDataService


class HistoryService:

    def __init__(self):
        self.market = MarketDataService()

    def get_history(
        self,
        exchange: str,
        symbol: str,
        token: str,
        interval: str = "ONE_MINUTE",
        days: int = 5,
    ):

        to_date = datetime.now()

        from_date = to_date - timedelta(days=days)

        params = {
            "exchange": exchange,
            "symboltoken": token,
            "interval": interval,
            "fromdate": from_date.strftime("%Y-%m-%d %H:%M"),
            "todate": to_date.strftime("%Y-%m-%d %H:%M"),
        }

        data = self.market.api.getCandleData(params)

        if not data["status"]:
            raise Exception(data.get("message", "History download failed"))

        df = pd.DataFrame(
            data["data"],
            columns=[
                "datetime",
                "open",
                "high",
                "low",
                "close",
                "volume",
            ],
        )

        df["datetime"] = pd.to_datetime(df["datetime"])

        return df
