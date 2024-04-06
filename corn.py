from product import Product


class Corn(Product):
    def __init__(self, weight: float, ID=1, BPMT=39.368):
        super().__init__(weight, ID, BPMT)
