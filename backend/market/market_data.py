from SmartApi import SmartConnect

from backend.broker.angelone.auth import AngelAuth
from backend.core.logger import logger


class MarketDataService:
    def __init__(self):
        self.auth = AngelAuth()
        self.session = self.auth.login()
        self.client: SmartConnect = self.auth.client

    def get_ltp(self, exchange: str, tradingsymbol: str, symboltoken: str):
        try:
            data = self.client.ltpData(
                exchange=exchange,
                tradingsymbol=tradingsymbol,
                symboltoken=symboltoken,
            )

            logger.info(
                f"LTP {tradingsymbol} : {data['data']['ltp']}"
            )

            return data

        except Exception as e:
            logger.exception(e)
            return None
