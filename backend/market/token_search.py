import json
from pathlib import Path
from datetime import datetime


class TokenSearch:

    def __init__(self):
        self.file = Path("data/OpenAPIScripMaster.json")

        if not self.file.exists():
            raise FileNotFoundError(
                "Instrument file not found. Run InstrumentManager.download() first."
            )

        with open(self.file, "r") as f:
            self.data = json.load(f)

    def search(self, symbol: str):
        symbol = symbol.upper()

        return [
            item
            for item in self.data
            if symbol in item.get("symbol", "").upper()
        ]

    def exact(self, symbol: str):
        symbol = symbol.upper()

        for item in self.data:
            if item.get("symbol", "").upper() == symbol:
                return item

        return None

    def futures(self, name: str):
        """
        Return all FUT contracts sorted by expiry.
        """
        name = name.upper()

        data = [
            item
            for item in self.data
            if item.get("name", "").upper() == name
            and item.get("instrumenttype", "").upper().startswith("FUT")
        ]

        def expiry_key(x):
            try:
                return datetime.strptime(x.get("expiry", ""), "%d%b%Y")
            except Exception:
                return datetime.max

        return sorted(data, key=expiry_key)

    def nearest_future(self, name: str):
        """
        Return nearest non-expired future contract.
        """
        today = datetime.today()

        contracts = []

        for item in self.futures(name):
            try:
                exp = datetime.strptime(item["expiry"], "%d%b%Y")
            except Exception:
                continue

            if exp >= today:
                contracts.append((exp, item))

        if not contracts:
            return None

        contracts.sort(key=lambda x: x[0])

        return contracts[0][1]
