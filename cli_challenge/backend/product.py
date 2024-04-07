class Product:
    """Represents a general product, which contains the product identifier, weight, and bushels per metric ton"""
    def __init__(self, bushels: float, ID: int, BPMT: float):
        self.weight = bushels/BPMT
        self.ID = ID
        self.BPMT = BPMT

    @staticmethod
    def get_BPMT(ID: int) -> float:
        match ID:
            case 0:
                return Barley.BPMT
            case 1:
                return Corn.BPMT
            case 2:
                return Wheat.BPMT
            case _:
                return -1

    @staticmethod
    def product_name(ID: int) -> str:
        return ["Barley", "Corn", "Wheat"][ID]



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
