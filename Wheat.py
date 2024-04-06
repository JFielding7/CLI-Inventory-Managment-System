from Product import Product


class Wheat(Product):
    def __init__(self, weight, id=2, bpmt=36.7437):
        super().__init__(weight, id, bpmt)
