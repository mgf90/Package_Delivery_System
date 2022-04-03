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

    def getID(self):
        return self.id

    def getAddress(self):
        return self.address

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def getZip(self):
        return self.zip

    def getDeadline(self):
        return self.deadline

    def getWeight(self):
        return self.weight

    def getNotes(self):
        return self.notes

    def setAddress(self, address):
        self.address = address

    def setCity(self, city):
        self.city = city

    def setZip(self, zip):
        self.zip = zip

