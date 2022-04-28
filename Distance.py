import csv
import numpy as np


class Distance:

    with open('WGUPS Distance Table.csv') as distances:
        dist_reader = list(csv.reader(distances, delimiter=','))

    with open('WGUPS Addresses.csv', encoding='utf-8-sig') as addresses:
        add_reader = list(csv.reader(addresses, delimiter=','))

    def fill_dist(self):
        with open('WGUPS Distance Table.csv', encoding='utf-8-sig') as distances:
            dist_list = list(csv.reader(distances, delimiter=','))
            dist_array = np.array(dist_list)
        return dist_array

    def calc_distance(self, current, prev):
        row = int(current)
        col = int(prev)
        dist = self.dist_reader[row][col]
        if dist is None or dist == '':
            dist = self.dist_reader[col][row]
        return dist

    def get_location_num(self, location):
        for name in self.add_reader:
            if location == name[2]:
                return name[0]

    def calc_total_distance(self, truck):
        sum = 0
        for p in truck:
            num = self.get_location_num(p.get_address())
            if truck[0] == p:
                n = 0

            d = self.calc_distance(num, n)
            n = num
            sum += float(d)

        d = self.calc_distance(num, 0)
        sum += float(d)
        return round(sum, 2)
