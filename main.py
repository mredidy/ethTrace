import os
import requests
from fastapi import FastAPI

app = FastAPI()

ETHERSCAN_API = "https://api.etherscan.io/api"
ETHERSCAN_KEY = os.getenv("ETHERSCAN_API_KEY")

@app.get("/latest-tx")
def latest_tx():
    params = {
        "module": "account",
        "action": "txlist",
        "address": "0xdAC17F958D2ee523a2206206994597C13D831ec7",  # USDT Token
        "startblock": 0,
        "endblock": 99999999,
        "page": 1,
        "offset": 5,
        "sort": "desc",
        "apikey": ETHERSCAN_KEY,
    }
    response = requests.get(ETHERSCAN_API, params=params)
    return response.json()