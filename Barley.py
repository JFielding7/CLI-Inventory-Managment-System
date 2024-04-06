from Product import Product


class Barley(Product):
    def __init__(self, name="Barley", bpmt=45.9296):
        super().__init__(name, bpmt)
