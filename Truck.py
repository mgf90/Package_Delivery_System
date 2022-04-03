import Package


class Truck:
    truck1 = []
    truck2 = []
    truck3 = []

    def loadTrucks(self, packages):

        for p in packages:
            address = p.getAddress()
            deadline = p.getDeadline()
            notes = p.getNotes()

            if 'truck 2' in notes:
                self.truck2.append(p)
            elif id == 13 or id == 14 or id == 15 or id == 17 or id == 19 or id == 21:
                self.truck1.append(p)
            elif 'Delayed on flight' in notes:
                self.truck3.append(p)
            elif 'Wrong address listed' in notes:
                p.setAddress('410 S State St')
                p.setZip('84111')
                self.truck3.append(p)
            elif deadline != 'EOD':
                self.truck2.append(p)
            else:
                if len(self.truck1) < 16:
                    self.truck1.append(p)
                elif len(self.truck2) < 16:
                    self.truck2.append(p)
                elif len(self.truck3) < 16:
                    self.truck3.append(p)
                else:
                    print('You messed up! The trucks are full')
