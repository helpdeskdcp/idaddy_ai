from collections import defaultdict
from datetime import datetime


class CandleEngine:

    def __init__(self):
        self.candles = defaultdict(dict)

    def update(self, symbol, ltp):

        now = datetime.now()

        minute = now.replace(
            second=0,
            microsecond=0,
        )

        candle = self.candles[symbol].get(minute)

        if candle is None:

            self.candles[symbol][minute] = {
                "time": minute.isoformat(),
                "open": ltp,
                "high": ltp,
                "low": ltp,
                "close": ltp,
            }

            return

        candle["high"] = max(candle["high"], ltp)
        candle["low"] = min(candle["low"], ltp)
        candle["close"] = ltp

    def latest(self, symbol):

        if symbol not in self.candles:
            return None

        keys = sorted(self.candles[symbol])

        if not keys:
            return None

        return self.candles[symbol][keys[-1]]
