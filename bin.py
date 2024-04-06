from product import Product


class Bin:
    """Represents a bin in the elevator"""
    def __init__(self):
        self.MAX_PRODUCTS = 15  # There can only be 15 products in a bin
        self.MAX_WEIGHT = 100  # The bin cannot exceed 100 MT
        self.weight = 0  # The current weight of the bin
        self.items = {}  # A mapping of items

    def add_item(self, product: Product) -> bool:
        """
        Adds an item to the bin, adding it to items if it is new. If it already exists, update the weight
        :param product: The product to add to the bin
        :return: True if the product is able to added to the bin
        """
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


