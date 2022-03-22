from HashMap import *
from Package import *



class Main:
    mp = HashMap()
    filename = "WGUPS Package File.csv"
    fillMap(filename, mp)

    print('Package Delivery System is now online')
    print(mp.lookup(40))

    print(3 % 40)





