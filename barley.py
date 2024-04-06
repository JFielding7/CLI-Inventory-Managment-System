from product import Product


class Barley(Product):
    def __init__(self, weight: float, ID=0, BPMT=45.9296):
        super().__init__(weight, ID, BPMT)
