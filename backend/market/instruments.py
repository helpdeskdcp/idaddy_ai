import json
from pathlib import Path

import requests

INSTRUMENT_URL = (
    "https://margincalculator.angelbroking.com/"
    "OpenAPI_File/files/OpenAPIScripMaster.json"
)


class InstrumentManager:
    def __init__(self):
        self.data_dir = Path("data")
        self.data_dir.mkdir(exist_ok=True)

        self.file = self.data_dir / "OpenAPIScripMaster.json"

    def download(self):

        response = requests.get(INSTRUMENT_URL, timeout=60)
        response.raise_for_status()

        self.file.write_text(response.text)

        return self.file

    def load(self):

        with open(self.file, "r") as f:
            return json.load(f)
