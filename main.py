from HashMap import *
from Package import *
from Distance import *
from Truck import *

class Main:
    packMap = HashMap()
    packFile = "WGUPS Package File.csv"
    fillMap(packFile, packMap)

    distFile = "WGUPS Distance Table.csv"
    distArray = fillDist(distFile)

    truck = Truck()
    truck.loadTrucks(packMap.packages)


    print('Package Delivery System is now online')


    print(calcDistance(distArray, 7, 9))
    print(packMap.lookup(4).getAddress())





