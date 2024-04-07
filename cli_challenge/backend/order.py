from enum import Enum

from product import Product
from rail_system import *

class Order:
    NOT_ORDERED = 0
    IN_BIN = 1
    ON_RAIL_CAR = 2
    ON_SHIP = 3
    DELIVERED = 4

    def __init__(self, items, date):
        self.items = items
        self.date = date
        self.state = Order.NOT_ORDERED
