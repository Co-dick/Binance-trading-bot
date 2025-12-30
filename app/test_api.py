from binance import Client
from config import API_KEY, API_SECRET

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

print(client.futures_account())
