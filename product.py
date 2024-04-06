class Product:
    def __init__(self, weight: float, ID: int, BPMT: float):
        self.weight = weight
        self.ID = ID
        self.BPMT = BPMT

    def receive(self, weight: float, MAX: int) -> bool:
        if self.weight + weight > MAX:
            return False
        self.weight += weight
        return True

    def ship(self, weight: float) -> bool:
        if self.weight < weight:
            return False
        self.weight -= weight
        return True
