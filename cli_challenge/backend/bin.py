class Bin:
    """Represents a bin in the elevator"""
    MAX_PRODUCTS = 15  # Maximum number of products per bin
    MAX_WEIGHT = 100  # Maximum weight per bin

    def __init__(self):
        self.weight = 0  # The current weight of the bin
        self.items = {}  # A mapping of items

    def add(self, ID: int, weight: int) -> int:
        """
        Adds an item to the bin, adding it to items if it is new. If it already exists, update the weight
        :param ID: the ID of the product being added
        :param weight:  the weight of the product being added
        :return: The amount of weight inputted
        """
        if ID not in self.items:
            self.items[ID] = 0
        weight = min(self.MAX_WEIGHT - self.weight, weight)
        self.weight += weight
        self.items[ID] += weight
        return weight

    def remove(self, ID: int, weight: int) -> int:
        if ID not in self.items:
            return 0
        min_weight = min(self.items[ID], weight)
        self.weight -= min_weight
        self.items[ID] -= min_weight
        if self.items[ID] == 0:
            self.items.pop(ID)
        return min_weight
