from fastapi import FastAPI
from app.bot import BasicBot
from app.config import API_KEY, API_SECRET

app = FastAPI()
bot = BasicBot(API_KEY, API_SECRET)

@app.post("/order/market")
def market(symbol: str, side: str, qty: float):
    return bot.market_order(symbol, side, qty)

@app.post("/order/limit")
def limit(symbol: str, side: str, qty: float, price: float):
    return bot.limit_order(symbol, side, qty, price)
