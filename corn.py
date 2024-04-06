from product import Product


class Corn(Product):
    def __init__(self, name="Corn", bpmt=39.368):
        super().__init__(name, bpmt)
