from SmartApi.smartWebSocketV2 import SmartWebSocketV2
import threading

from backend.broker.angelone.auth import AngelAuth
from backend.market.token_search import TokenSearch


class MarketWebSocket:

    def __init__(self, debug=False):

        self.auth = AngelAuth()
        self.auth.login()
        self.tokens = TokenSearch()
        self.ticks = {}
        self.token_map = {}
        self.debug = debug

        self.ws = SmartWebSocketV2(
            self.auth.jwt_token,
            self.auth.ANGEL_API_KEY if hasattr(self.auth, "ANGEL_API_KEY") else self.auth.settings.ANGEL_API_KEY,
            self.auth.settings.ANGEL_CLIENT_ID,
            self.auth.feed_token,
        )

    def on_open(self, ws):
        print("WebSocket Connected")

        self.subscribe_symbols([
            "NIFTY",
            "BANKNIFTY",
            "FINNIFTY",
            "SENSEX",
        ])

    def on_data(self, ws, message):
        token = message.get("token")

        symbol = self.token_map.get(token)

        if symbol:
            self.ticks[symbol] = message
        else:
            self.ticks[token] = message

        if self.debug:
            print(message)

    def on_error(self, ws, error):
        print("ERROR:", error)

    def on_close(self, ws):
        print("WebSocket Closed")

    def connect(self):

        self.ws.on_open = self.on_open
        self.ws.on_data = self.on_data
        self.ws.on_error = self.on_error
        self.ws.on_close = self.on_close

        self.ws.connect()

    def subscribe(self, exchange_type: int, token: str):

        self.ws.subscribe(
            correlation_id="idaddy",
            mode=1,
            token_list=[
                {
                    "exchangeType": exchange_type,
                    "tokens": [token],
                }
            ],
        )

        print(f"Subscribed : {token}")


    def subscribe_symbol(self, symbol: str):

        item = self.tokens.exact(symbol)

        if not item:
            raise Exception(f"Symbol not found: {symbol}")

        exch_map = {
            "NSE": 1,
            "NFO": 2,
            "BSE": 3,
            "MCX": 5,
        }

        exch = exch_map.get(item["exch_seg"])

        if exch is None:
            raise Exception(
                f"Unsupported exchange: {item['exch_seg']}"
            )

        self.subscribe(
            exch,
            item["token"],
        )

        self.token_map[item["token"]] = symbol

        print(
            f"{symbol} -> {item['token']} ({item['exch_seg']})"
        )


    def get_tick(self, token):
        return self.ticks.get(token)


    def start(self):

        self.thread = threading.Thread(
            target=self.connect,
            daemon=True,
        )

        self.thread.start()


    def subscribe_symbols(self, symbols):

        for symbol in symbols:
            self.subscribe_symbol(symbol)

