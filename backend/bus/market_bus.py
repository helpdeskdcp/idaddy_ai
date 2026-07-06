from collections import defaultdict
from typing import Callable


class MarketBus:

    def __init__(self):
        self.subscribers = defaultdict(list)

    def subscribe(self, event: str, callback: Callable):
        self.subscribers[event].append(callback)

    def publish(self, event: str, data):

        for callback in self.subscribers[event]:
            callback(data)


market_bus = MarketBus()
