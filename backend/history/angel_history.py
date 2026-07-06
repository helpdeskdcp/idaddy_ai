from datetime import datetime

from backend.history.base_history import BaseHistoryProvider
from backend.broker.angelone.auth import AngelAuth


class AngelHistoryProvider(BaseHistoryProvider):

    def __init__(self):
        self.auth = AngelAuth()

    def login(self):
        self.auth.login()

    def download(
        self,
        symbol: str,
        interval: str,
        start: datetime,
        end: datetime,
    ):
        """
        TODO:
        Angel One Historical API call.

        Returns:
            List[dict]
        """
        print(
            f"[AngelHistory] {symbol} {interval} "
            f"{start} -> {end}"
        )

        return []
