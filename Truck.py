from Package import Package
from HashMap import HashMap


class Truck:
    truck1 = []
    truck2 = []
    truck3 = []

    def load_truck1(self, p_id, map):
        package = map.lookup(p_id)
        self.truck1.append(package)

    def load_truck2(self, p_id, map):
        package = map.lookup(p_id)
        self.truck2.append(package)

    def load_truck3(self, p_id, map):
        package = map.lookup(p_id)
        self.truck3.append(package)