from app.bot import BasicBot
from app.config import API_KEY, API_SECRET

bot = BasicBot(API_KEY, API_SECRET)

symbol = input("Symbol (BTCUSDT): ").upper()
side = input("Side (BUY/SELL): ").upper()
order_type = input("Order Type (MARKET/LIMIT/STOP): ").upper()
qty = float(input("Quantity: "))

if order_type == "MARKET":
    print(bot.market_order(symbol, side, qty))
elif order_type == "LIMIT":
    price = float(input("Price: "))
    print(bot.limit_order(symbol, side, qty, price))
elif order_type == "STOP":
    stop = float(input("Stop Price: "))
    price = float(input("Limit Price: "))
    print(bot.stop_limit_order(symbol, side, qty, stop, price))
