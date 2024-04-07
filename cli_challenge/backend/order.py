import mysql.connector

class Order:

    TOTAL_PROFIT = 0

    NOT_ORDERED = 0
    IN_BIN = 1
    ON_RAIL_CAR = 2
    ON_SHIP = 3
    DELIVERED = 4

    def __init__(self, date, order_id, cost, revenue, state=NOT_ORDERED):
        self.items = []
        self.date = date
        self.id = order_id
        self.state = state
        self.cost = cost
        self.revenue = revenue

    def status_str(self):
        match self.state:
            case 0:
                return "Not Ordered"
            case 1:
                return "In Bin"
            case 2:
                return "On Rail Car"
            case 3:
                return "On Ship"
            case 4:
                return "Delivered"

    def profit(self):
        return self.revenue - self.cost

class OrderManager:
    def __init__(self):
        pass