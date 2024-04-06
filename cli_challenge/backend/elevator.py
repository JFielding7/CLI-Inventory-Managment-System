import numpy

from bin import Bin


class Elevator:
    """The Elevator holds 15 bins, storing received shipments, and sending shipments"""
    NUM_BINS = 15  # Number of bins in the elevator

    def __init__(self):
        self.MAX_WEIGHT = 100
        self.bins = numpy.empty(self.NUM_BINS, dtype=Bin)

