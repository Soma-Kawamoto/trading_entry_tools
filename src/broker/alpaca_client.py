import alpaca_trade_api as tradeapi
import os

class AlpacaClient:
    def __init__(self):
        self.api = tradeapi.REST(
            os.getenv("ALPACA_API_KEY"),
            os.getenv("ALPACA_SECRET_KEY"),
            base_url="https://paper-api.alpaca.markets" # Paper Trading
        )

    def submit_order(self, symbol, qty, side):
        return self.api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type='market',
            time_in_force='gtc'
        )