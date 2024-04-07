import mysql.connector

class Order:
    NOT_ORDERED = 0
    IN_BIN = 1
    ON_RAIL_CAR = 2
    ON_SHIP = 3
    DELIVERED = 4

    def __init__(self, items, date, num):
        self.items = items
        self.date = date
        self.num = num
        self.state = Order.NOT_ORDERED

class OrderManager:
    def __init__(self):
        pass