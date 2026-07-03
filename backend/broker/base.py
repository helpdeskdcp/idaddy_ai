from abc import ABC, abstractmethod
from typing import Any


class BrokerClient(ABC):
    """Abstract broker interface."""

    @abstractmethod
    def login(self) -> bool:
        pass

    @abstractmethod
    def logout(self) -> bool:
        pass

    @abstractmethod
    def get_profile(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_feed_token(self) -> str:
        pass

    @abstractmethod
    def get_ltp(
        self,
        exchange: str,
        tradingsymbol: str,
        symboltoken: str,
    ) -> dict[str, Any]:
        pass
