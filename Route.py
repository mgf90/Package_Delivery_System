import datetime

from Package import *
from Distance import *


class Route:

    def __init__(self, distance):
        self.d = distance

    def organize(self, truck):

        route = []
        prev = 0

        while len(truck) > 0:
            weight = 50.0
            existing_address = []
            for a in route:
                existing_address.append(a.get_address())
            for t in truck:
                if t.get_address in existing_address:
                    temp_package = t
                else:
                    new_location = self.d.get_location_num(t.get_address())
                    p_miles = float(self.d.calc_distance(new_location, prev))
                    if p_miles <= weight:
                        weight = p_miles
                        temp_package = t
            route.append(temp_package)
            prev = self.d.get_location_num(temp_package.get_address())
            truck.remove(temp_package)

        return route

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

    # def time_to_sec(self, time):
    #     h, m, s = map(int, time.split(':'))
    #     return h * 3600 + m * 60 + s

    def get_delta_time(self, s):
        try:
            (h, m, s) = s.split(':')
            dt = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            return dt
        except:
            print("Error converting to Time Delta")

    def get_delivery_time(self, truck, truck_time, id):
        for i in truck:
            if i.get_id() == id:
                index = truck.index(i)
        return truck_time[index + 1]

    def get_status(self, package, truck, time, name, id):
        delivery_time = self.get_delivery_time(truck, time, id)
        timestamp = self.get_delta_time(package)
        if name == 'truck1':
            truck_time = self.get_delta_time('8:00:00')
        if name == 'truck2':
            truck_time = self.get_delta_time('10:00:00')
        if name == 'truck3':
            truck_time = self.get_delta_time('9:05:00')
        if timestamp > delivery_time:
            return 'DELIVERED'
        if timestamp <= delivery_time:
            if timestamp < truck_time:
                return 'AT_HUB'
            else:
                return 'ON_TRUCK'

    def get_report(self, name, truck, truck_timeline, time, distance):
        print('\n{} || # of packages: {} || Total Distance: {} miles\n'.format(name, len(truck), distance))
        if time == '':
            timestamp = '23:00:00'
        else:
            timestamp = time
        for t in truck:
            i = truck.index(t)
            id = t.get_id()
            ds = self.get_status(timestamp, truck, truck_timeline, name, id)
            s = 'ID: {:>2} -- Deadline: {:>6} -- Status: {:>6} -- Expected Delivery: {}'
            formatted_string = s.format(id, t.get_deadline(), ds, truck_timeline[i + 1])
            print(formatted_string)

    # def get_status(self, seconds, truck):
    #     for p in truck:
    #         if seconds < p.get_


