from abc import ABC, abstractmethod
from datetime import datetime


class BaseHistoryProvider(ABC):
    """
    Base interface for all historical data providers.
    """

    @abstractmethod
    def login(self):
        """Authenticate with broker."""
        raise NotImplementedError

    @abstractmethod
    def download(
        self,
        symbol: str,
        interval: str,
        start: datetime,
        end: datetime,
    ):
        """
        Return historical candles.

        Expected format:
        [
            {
                "time": "...",
                "open": 0.0,
                "high": 0.0,
                "low": 0.0,
                "close": 0.0,
                "volume": 0
            }
        ]
        """
        raise NotImplementedError
