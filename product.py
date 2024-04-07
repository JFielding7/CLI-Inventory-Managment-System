class Product:
    def __init__(self, bushels: float, ID: int, BPMT: float):
        self.weight = bushels/BPMT
        self.ID = ID
        self.BPMT = BPMT

    def __copy__(self):
        return Product(self.BPMT*self.weight, self.ID, self.BPMT)

class Barley(Product):
    ID = 0
    BPMT = 45.9296

    def __init__(self, bushels: float, ID=ID, BPMT=BPMT):
        super().__init__(bushels, ID, BPMT)


class Corn(Product):
    ID = 1
    BPMT = 39.368

    def __init__(self, bushels: float, ID=ID, BPMT=BPMT):
        super().__init__(bushels, ID, BPMT)


class Wheat(Product):
    ID = 2
    BPMT = 36.7437

    def __init__(self, bushels: float, ID=ID, BPMT=BPMT):
        super().__init__(bushels, ID, BPMT)
