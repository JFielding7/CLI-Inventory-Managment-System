from product import Product


class Bin:
    """Represents a bin in the elevator"""
    MAX_PRODUCTS = 15  # Maximum number of products per bin
    MAX_WEIGHT = 100  # Maximum weight per bin

    def __init__(self):
        self.weight = 0  # The current weight of the bin
        self.items = {}  # A mapping of items

    def add_item(self, product: Product) -> bool:
        """
        Adds an item to the bin, adding it to items if it is new. If it already exists, update the weight
        :param product: The product to add to the bin
        :return: True if the product is added/updated in the bin
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

    def remove_item(self, product: Product, amount: int) -> int:
        """
        Removes as much of an item from a bin as needed, without going below 0
        :param product: Try to remove the amount from the specified product
        :param amount: The amount to ask for
        :return: The amount removed
        """
        key = product.ID
        if key not in self.items:
            return 0

        # Get
        min_weight = min(self.items[key], product.weight)
        self.items[key] -= min_weight
        return min_weight
