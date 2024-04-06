from product import Product


class Bin:
    def __init__(self):
        self.MAX_PRODUCTS = 15
        self.MAX_WEIGHT = 100
        self.weight = 0
        self.items = {}

    def add_item(self, product: Product) -> bool:
        not_added = product.ID not in self.items
        weight = self.weight + product.weight
        if weight > self.MAX_WEIGHT or (not_added and len(self.items) == self.MAX_PRODUCTS):
            return False
        if not_added:
            self.items[product.ID] = product.weight
        else:
            self.items[product.ID] += product.weight
        self.weight = weight
        return True

    def remove_item(self, product: Product) -> bool:
        key = product.ID
        if key not in self.items:
            return False
        weight = self.items[key]
        if product.weight > weight:
            return False
        self.items[key] -= product.weight
        self.weight -= product.weight
        return True


