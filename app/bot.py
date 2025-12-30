from binance import Client
from binance.exceptions import BinanceAPIException
from app.logger import get_logger
from app.config import BINANCE_TESTNET_URL

class BasicBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = BINANCE_TESTNET_URL
        self.logger = get_logger()
        self.logger.info("Bot initialized")

    def market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            self.logger.info(f"Market order placed: {order}")
            return order
        except BinanceAPIException as e:
            self.logger.error(f"Market order failed: {e}")
            return {"error": str(e)}

    def limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
            self.logger.info(f"Limit order placed: {order}")
            return order
        except BinanceAPIException as e:
            self.logger.error(f"Limit order failed: {e}")
            return {"error": str(e)}

    def stop_limit_order(self, symbol, side, quantity, stop_price, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                stopPrice=stop_price,
                price=price,
                timeInForce="GTC"
            )
            self.logger.info(f"Stop-limit order placed: {order}")
            return order
        except BinanceAPIException as e:
            self.logger.error(f"Stop-limit order failed: {e}")
            return {"error": str(e)}
