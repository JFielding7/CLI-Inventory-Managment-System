from product import Product


class Wheat(Product):
    def __init__(self, weight: float, ID=2, BPMT=36.7437):
        super().__init__(weight, ID, BPMT)
