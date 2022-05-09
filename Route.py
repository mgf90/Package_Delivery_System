import datetime
from Distance import *


class Route:

    def __init__(self, distance):
        self.d = distance

    # Nearest neighbor algorithm
    # Time: O(n)
    # Space: O(n)
    def organize(self, truck):

        # initializes the route list
        route = []

        # sets the address to the hub
        prev = 0

        while len(truck) > 0:
            dist = 40

            # loops through every package in the truck and finds the shortest distance
            for t in truck:
                curr = self.d.get_location_num(t.get_address())
                miles = float(self.d.calc_distance(curr, prev))
                if miles <= dist:
                    dist = miles
                    p = t

            # adds package to the route list and removes it from the truck
            route.append(p)
            prev = self.d.get_location_num(p.get_address())
            truck.remove(p)

        return route

    # Time: O(n)
    # Space: O(n)
    # Calculates delivery time for truck
    def truck_time(self, truck, start):

        time_sum = []
        itinerary = start
        dist = Distance()

        for p in truck:
            if truck[0] == p:
                pl = 0
            address = p.get_address()
            add_num = dist.get_location_num(address)
            mileage = dist.calc_distance(add_num, pl)
            pl = add_num
            speed = float(mileage) / 18
            speed_format = '{0:02.0f}:{1:02.0f}:00'.format(*divmod(speed * 60, 60))
            itinerary.append(speed_format)
        total_time = datetime.timedelta()
        for p in itinerary:
            total_time += self.get_delta_time(p)
            time_sum.append(total_time)
        return time_sum

    # Time: O(1)
    # Space: O(1)
    # Converts time to delta time
    def get_delta_time(self, s):

        (h, m, s) = s.split(':')
        dt = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        return dt


    # Time: O(n)
    # Space: O(n)
    # Returns delivery time
    def get_delivery_time(self, truck, time, id):
        for i in truck:
            if i.get_id() == id:
                index = truck.index(i)
        return time[index + 1]

    # Time: O(1)
    # Space: O(1)
    # Gets delivery status of package
    def get_status(self, package, truck, time, name, id):
        delivery_time = self.get_delivery_time(truck, time, id)
        timestamp = self.get_delta_time(package)

        if name == 'Truck 1':
            truck_time = self.get_delta_time('8:00:00')
        if name == 'Truck 2':
            truck_time = self.get_delta_time('8:00:00')
        if name == 'Truck 3':
            truck_time = self.get_delta_time('10:00:00')
        if timestamp > delivery_time:
            return 'DELIVERED'
        if timestamp <= delivery_time:
            if timestamp < truck_time:
                return 'AT_HUB'
            else:
                return 'ON_TRUCK'

    # Time: O(n)
    # Space: O(n)
    # Prints full report of all packages
    def get_report(self, truck, name, distance, itinerary, time):

        print(f'\n{len(truck)} packages on {name}. Distance travelled is {distance} miles.\n')

        for p in truck:
            i = truck.index(p)
            id = p.get_id()
            address = p.get_address()
            deadline = p.get_deadline()
            status = self.get_status(time, truck, itinerary, name, id)
            report = f'Package ID: {id}   ||   Deadline: {deadline}   ||   Status: {status}   ||   Delivery Time: ' \
                     f'{itinerary[i + 1]}   ||   Address: {address}'
            print(report)



