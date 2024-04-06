from Product import Product


class Corn(Product):
    def __init__(self, weight, id=1, bpmt=39.368):
        super().__init__(weight, id, bpmt)
