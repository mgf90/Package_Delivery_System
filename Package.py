import csv
from datetime import datetime


class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes

    def __str__(self):
        return "%s, %s, %s, %s, %s,%s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip,
                                                          self.deadline, self.weight, self.notes)


def fillMap(filename, hashmap):
    with open(filename) as file:
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

