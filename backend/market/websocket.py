from SmartApi.smartWebSocketV2 import SmartWebSocketV2

from backend.broker.angelone.auth import AngelAuth


class MarketWebSocket:

    def __init__(self):

        self.auth = AngelAuth()
        self.auth.login()

        self.ws = SmartWebSocketV2(
            self.auth.jwt_token,
            self.auth.ANGEL_API_KEY if hasattr(self.auth, "ANGEL_API_KEY") else self.auth.settings.ANGEL_API_KEY,
            self.auth.settings.ANGEL_CLIENT_ID,
            self.auth.feed_token,
        )

    def on_open(self, ws):
        print("WebSocket Connected")

    def on_data(self, ws, message):
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
