import numpy

from bin import Bin


class Elevator:
    """The Elevator holds 15 bins, storing received shipments, and sending shipments"""
    def __init__(self):
        self.bins = numpy.empty(15, dtype=Bin)


