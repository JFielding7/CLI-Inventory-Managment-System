class Product:
    """Represents a general product, which contains the product identifier, weight, and bushels per metric ton"""
    def __init__(self, bushels: float, ID: int, BPMT: float):
        self.weight = bushels/BPMT
        self.ID = ID
        self.BPMT = BPMT

    @staticmethod
    def get_BPMT(ID: int) -> float:
        barley = 45.9296
        corn = 39.368
        wheat = 36.7437
        return [barley, corn, wheat][ID]

    @staticmethod
    def product_name(ID: int) -> str:
        return ["Barley", "Corn", "Wheat"][ID]
