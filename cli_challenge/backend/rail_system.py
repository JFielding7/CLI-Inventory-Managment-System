import numpy

from random import sample
from math import ceil


class RailCarSection:
    def __init__(self, product_ID: int, weight: float):
        self.product_ID = product_ID
        self.weight = weight


class RailCar:

    MAX_PRODUCTS = 2
    MAX_WEIGHT = 100
    MAX_SECTION_WEIGHT = MAX_WEIGHT / MAX_PRODUCTS

    def __init__(self, num):
        self.num = num
        self.sections = numpy.empty(self.MAX_PRODUCTS, dtype=RailCarSection)
        self.curr_section = 0

    def load_product(self, product_ID: int, weight: float) -> float:
        while weight > 1e-6 and self.curr_section < self.MAX_PRODUCTS:
            self.sections[self.curr_section] = RailCarSection(product_ID, min(weight, self.MAX_SECTION_WEIGHT))
            weight -= self.MAX_SECTION_WEIGHT
            self.curr_section += 1
        return weight

    def is_full(self):
        return self.curr_section == self.MAX_PRODUCTS


class RailSystem:

    CARS = 100

    def __init__(self):
        self.available_cars = set()
        for i in range(1, RailSystem.CARS + 1):
            self.available_cars.add(RailCar(i))

    def load_order(self, items: dict[int, float]) -> list[RailCar] | None:
        cars_needed = ceil(sum(ceil(weight / RailCar.MAX_SECTION_WEIGHT) for weight in items.values()) / RailCar.MAX_PRODUCTS)
        if cars_needed > len(self.available_cars):
            return None
        cars = []
        curr_car = None
        for product_ID, weight in items.items():
            while weight > 1e-6:
                if curr_car is None or curr_car.is_full():
                    curr_car = sample(self.available_cars, 1)[0]
                    self.available_cars.remove(curr_car)
                    cars.append(curr_car)
                weight = curr_car.load_product(product_ID, weight)
        return cars

    def return_car(self, rail_car: RailCar):
        self.available_cars.add(rail_car)

