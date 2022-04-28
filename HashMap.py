from Package import Package
import csv
import os

class Bucket:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap:
    def __init__(self, size=40):
        path = os.getcwd()
        file = "/WGUPS Package File.csv"
        self.packages = []
        for i in range(size):
            self.packages.append([])
        self.parse_csv(path, file)

    def get_hash(self, key):
        return key % 40

    def add(self, key, package):
        self.packages[key] = package

    def delete(self, p_ID):
        key = self.get_hash(p_ID)
        self.packages.remove(key)

    def insert(self, p_ID, address, city, state, zip, deadline, weight, status):
        p = Package(p_ID, address, city, state, zip, deadline, weight, status, '')
        key = self.get_hash(p_ID)
        self.packages[key] = p

    def lookup(self, p_ID):
        key = self.get_hash(p_ID)
        return self.packages[key]

    def parse_csv(self, path, file):
        with open(path + file, encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                p = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], "AT_HUB")
                key = self.get_hash(p.get_id())
                self.add(key, p)