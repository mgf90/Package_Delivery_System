class Package:
    # constructor for Package object
    def __init__(self, id, address, city, state, zip, deadline, weight, status, notes):
        self.id = int(id)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = int(weight)
        self.status = status
        self.notes = notes

    # prints package info as a string
    def __str__(self):
        return "%s, %s, %s, %s, %s,%s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip,
                                                  self.deadline, self.weight, self.notes)

    # setters and getters for package info
    def get_id(self):
        return self.id

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip(self):
        return self.zip

    def get_deadline(self):
        return self.deadline

    def get_weight(self):
        return self.weight

    def get_status(self):
        return self.status

    def get_notes(self):
        return self.notes

    def set_address(self, address):
        self.address = address

    def set_city(self, city):
        self.city = city

    def set_zip(self, zip):
        self.zip = zip

    def set_status(self, status):
        self.status = status

