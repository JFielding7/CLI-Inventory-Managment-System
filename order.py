from product import Product
import datetime


class Order:
    def __init__(self, items: list[Product], date: datetime):
        self.items = items
        self.date = date
