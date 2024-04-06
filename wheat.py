from product import Product


class Wheat(Product):
    def __init__(self, name="Wheat", bpmt=36.7437):
        super().__init__(name, bpmt)
