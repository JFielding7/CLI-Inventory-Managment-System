import mysql.connector

class Order:
    NOT_ORDERED = 0
    IN_BIN = 1
    ON_RAIL_CAR = 2
    ON_SHIP = 3
    DELIVERED = 4

    def __init__(self, date, order_id, state=NOT_ORDERED):
        self.items = []
        self.date = date
        self.id = order_id
        self.state = state

class OrderManager:
    def __init__(self):
        pass