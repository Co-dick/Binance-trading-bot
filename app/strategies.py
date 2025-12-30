import time

class GridStrategy:
    def __init__(self, bot, symbol, lower, upper, grids, qty):
        step = (upper - lower) / grids
        self.orders = [
            (lower + i * step) for i in range(grids)
        ]
        for price in self.orders:
            bot.limit_order(symbol, "BUY", qty, round(price, 2))

class TWAPStrategy:
    def __init__(self, bot, symbol, side, total_qty, slices, delay):
        slice_qty = total_qty / slices
        for _ in range(slices):
            bot.market_order(symbol, side, slice_qty)
            time.sleep(delay)
