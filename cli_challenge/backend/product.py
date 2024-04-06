class Product:
    """Represents a general product, which contains the product identifier, weight, and bushels per metric ton"""
    def __init__(self, bushels: float, ID: int, BPMT: float):
        self.weight = bushels/BPMT
        self.ID = ID
        self.BPMT = BPMT


class Barley(Product):
    """Holds the product values for barley"""
    def __init__(self, bushels: float, ID=0, BPMT=45.9296):
        super().__init__(bushels, ID, BPMT)


class Corn(Product):
    """Holds the product values for corn"""
    def __init__(self, bushels: float, ID=1, BPMT=39.368):
        super().__init__(bushels, ID, BPMT)


class Wheat(Product):
    """Holds the product values for wheat"""
    def __init__(self, bushels: float, ID=2, BPMT=36.7437):
        super().__init__(bushels, ID, BPMT)
