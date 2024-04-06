class Product:
    def __init__(self, weight, id, bpmt):
        self.weight = weight
        self.name = id
        self.bpmt = bpmt

    def receive(self, weight):
        self.weight += weight

    def ship(self, weight):
        if self.weight < weight:
            return 0
        self.weight -= weight
        return 1
