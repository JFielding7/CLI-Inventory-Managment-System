from Product import Product


class Barley(Product):
    def __init__(self, weight, id=0, bpmt=45.9296):
        super().__init__(weight, id, bpmt)
