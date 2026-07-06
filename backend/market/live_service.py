from backend.market.websocket import MarketWebSocket

# Singleton Live Market Service
ws = MarketWebSocket(debug=False)
