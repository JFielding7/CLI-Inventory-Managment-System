from product import Product


class Bin:
    """Represents a bin in the elevator"""
    MAX_PRODUCTS = 15  # Maximum number of products per bin
    MAX_WEIGHT = 100  # Maximum weight per bin

    def __init__(self):
        self.weight = 0  # The current weight of the bin
        self.items = {}  # A mapping of items

    def add_item(self, product: Product) -> int:
        """
        Adds an item to the bin, adding it to items if it is new. If it already exists, update the weight
        :param product: The product to add to the bin
        :return: The amount of weight inputted
        """
        if product.ID not in self.items:
            self.items[product.ID] = 0
        weight = min(self.MAX_WEIGHT - self.weight, product.weight)
        self.weight += weight
        self.items[product.ID] += weight
        return weight

    def remove_item(self, product: Product) -> int:
        if product.ID not in self.items:
            return 0
        min_weight = min(self.items[product.ID], product.weight)
        self.items[product.ID] -= min_weight
        return min_weight
