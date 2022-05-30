class Truck:

    # lists for three different trucks
    truck1 = []
    truck2 = []
    truck3 = []

    # loads truck 1 by package id
    def load_truck1(self, p_id, map):
        package = map.search(p_id)
        self.truck1.append(package)

    # loads truck 2 by package id
    def load_truck2(self, p_id, map):
        package = map.search(p_id)
        self.truck2.append(package)

    # loads truck 3 by package id
    def load_truck3(self, p_id, map):
        package = map.search(p_id)
        self.truck3.append(package)