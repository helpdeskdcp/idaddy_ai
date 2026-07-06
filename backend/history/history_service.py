from datetime import datetime

from backend.history.angel_history import AngelHistoryProvider


class HistoryService:

    def __init__(self):
        self.provider = AngelHistoryProvider()
        self.provider.login()

    def download(
        self,
        symbol: str,
        interval: str,
        start: datetime,
        end: datetime,
    ):

        rows = self.provider.download(
            symbol,
            interval,
            start,
            end,
        )

        print(
            f"[HistoryService] Downloaded {len(rows)} rows"
        )

        return rows


history_service = HistoryService()
