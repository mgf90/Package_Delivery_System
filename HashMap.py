import csv

import Package


class Bucket:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:
    def __init__(self, size=40):
        self.packages = []
        for i in range(size):
            self.packages.append([])

    def get_hash(self, key):
        return key % 40

    def insert(self, key, value):
        hashkey = self.get_hash(key)
        kv = [key, value]

        if self.packages[hashkey] is None:
            self.packages[hashkey] = list([kv])
            return True
        else:
            for pair in self.packages[hashkey]:
                if pair[0] == key:
                    pair[1] == value
                    return True
            self.packages[hashkey].append(kv)
            return True

    def lookup(self, key):
        hashkey = self.get_hash(key)
        if self.packages[hashkey] is not None:
            for pair in self.packages[hashkey]:
                if pair[0] == key:
                    return pair[1]
        return 'The package does not exist'

    def delete(self, key):
        hashkey = self.get_hash(key)

        if self.packages[hashkey] is None:
            return False
        for i in range(0, len(self.packages[hashkey])):
            if self.packages[hashkey][i][0] == key:
                self.packages[hashkey].pop(i)
                return True

    def print(self):
        for package in self.packages:
            if package is not None:
                print(str(package))

    def fillMap(filename, hashmap):
        with open(filename, encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for package in reader:
                id = int(package[0])
                address = package[1]
                city = package[2]
                state = package[3]
                zip = package[4]
                deadline = package[5]
                weight = package[6]
                notes = package[7]

                p = Package(id, address, city, state, zip, deadline, weight, notes)
                hashmap.insert(p.id, p)
