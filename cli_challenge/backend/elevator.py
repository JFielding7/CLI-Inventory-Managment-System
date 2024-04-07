import numpy
from product import *
from bin import Bin


class Elevator:
    """The Elevator holds 15 bins, storing received shipments, and sending shipments"""
    NUM_BINS = 15  # Number of bins in the elevator
    def __init__(self):
        self.bins = numpy.array([Bin() for _ in range(self.NUM_BINS)])
        self.items = {}

    def receive(self, products: list[Product]) -> bool:
        curr = 0
        for product in products:
            copy = product.__copy__()
            if product.ID not in self.items:
                self.items[product.ID] = 0
            while copy.weight > 0:
                if curr >= self.NUM_BINS:
                    return False
                weight = self.bins[curr].add_item(copy)
                copy.weight -= weight
                self.items[product.ID] += weight
                if copy.weight > 0:
                    curr += 1
        return True

    #def export(self):