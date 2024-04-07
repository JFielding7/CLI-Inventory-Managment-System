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

    def status_str(self) -> str:
        return ["Not ordered", "In elevator", "On rail car", "Shipping", "Delivered"][self.state]

    def profit(self):
        return self.revenue - self.cost

    def map_product_id_to_weight(self):
        return {product.ID: product.weight for product in self.items}

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

