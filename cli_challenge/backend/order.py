# Represents an order from the Customer
class Order:
    # total profit made form all Orders
    TOTAL_PROFIT = 0

    # Statues of the order
    NOT_ORDERED = 0
    IN_BIN = 1
    ON_RAIL_CAR = 2
    ON_SHIP = 3
    DELIVERED = 4

    # Initializes an order
    def __init__(self, date, order_id, cost, revenue, state=NOT_ORDERED):
        self.items = []
        self.date = date
        self.id = order_id
        self.state = state
        self.cost = cost
        self.revenue = revenue

    # Gets the string representing the status of the order
    def status_str(self) -> str:
        return ["Not ordered", "In elevator", "On rail car", "Shipping", "Delivered"][self.state]

    # Gets the profit made form the order
    def profit(self):
        return self.revenue - self.cost

    # Maps the products requested in this order to their weight quantities
    def map_product_id_to_weight(self):
        return {product.ID: product.weight for product in self.items}

    # Advances the order next state
    def advance_state(self, window):
        if self.state == self.DELIVERED:
            return False
        if self.state == self.NOT_ORDERED:
            window.elevator.receive(self.items)
            window.update_tree(window.elevator.bins)
        elif self.state == self.IN_BIN:
            window.rail_system.load_order(window.elevator.send(self.map_product_id_to_weight()))
        self.state += 1
        if self.state == Order.DELIVERED:
            Order.TOTAL_PROFIT += self.profit()
        return self.state <= self.DELIVERED

