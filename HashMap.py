import csv
import os
from Package import Package


class Bucket:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap:
    # constructor for HashMap object
    def __init__(self, size=40):
        path = os.getcwd()
        file = "/WGUPS Package File.csv"
        self.packages = []
        for i in range(size):
            self.packages.append([])
        self.read_package_data(path, file)

    # returns hash key
    def get_hash(self, key):
        return key % 40

    # inserts package into HashMap
    def add(self, key, package):
        self.packages[key] = package

    # deletes package from HashMap
    def delete(self, p_ID):
        key = self.get_hash(p_ID)
        self.packages.remove(key)

    # searches HashMap for particular package
    def search(self, p_ID):
        key = self.get_hash(p_ID)
        return self.packages[key]

    # Time: O(n)
    # Space: O(n)
    # reads data from csv file into HashMap
    def read_package_data(self, path, file):
        with open(path + file, encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                p = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], "AT_HUB")
                key = self.get_hash(p.get_id())
                self.add(key, p)
