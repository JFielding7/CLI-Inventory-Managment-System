import numpy
from product import *
from bin import Bin
from order import Order


class Elevator:
    """The Elevator holds 15 bins, storing received shipments, and sending shipments"""
    NUM_BINS = 15  # Number of bins in the elevator

    def __init__(self):
        self.bins = numpy.array([Bin() for _ in range(self.NUM_BINS)])
        self.items = {}

    def receive(self, products: list[Product]) -> bool:
        curr = 0
        for product in products:
            if product.ID not in self.items:
                self.items[product.ID] = 0
            weight = product.weight
            while weight > 0:
                if curr >= self.NUM_BINS:
                    return False
                put = self.bins[curr].add(product.ID, weight)
                weight -= put
                self.items[product.ID] += put
                if weight > 0:
                    curr += 1
        return True

    def send(self, products: dict[int: float]):
        send = {}
        for ID in products:
            weight = products[ID] / Product.get_BPMT(ID)
            if self.items[ID] < weight:
                return None
            remaining = weight
            curr = 0
            while remaining > 0:
                remaining = self.bins[curr].remove(ID, remaining)
            send[ID] = weight
            self.items[ID] -= weight
            if self.items[ID] == 0:
                self.items.pop(ID)
        return send
