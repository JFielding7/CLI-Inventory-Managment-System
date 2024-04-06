class Product:
    def __init__(self, bushels: float, ID: int, BPMT: float):
        self.weight = bushels/BPMT
        self.ID = ID
        self.BPMT = BPMT


class Barley(Product):
    def __init__(self, bushels: float, ID=0, BPMT=45.9296):
        super().__init__(bushels, ID, BPMT)


class Corn(Product):
    def __init__(self, bushels: float, ID=1, BPMT=39.368):
        super().__init__(bushels, ID, BPMT)


class Wheat(Product):
    def __init__(self, bushels: float, ID=2, BPMT=36.7437):
        super().__init__(bushels, ID, BPMT)
