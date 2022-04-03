import csv
import numpy as np


with open('WGUPS Addresses.csv', encoding='utf-8-sig') as addresses:
    addReader = list(csv.reader(addresses, delimiter=','))

def fillDist(filename):
    with open(filename, encoding='utf-8-sig') as distances:
        distList = list(csv.reader(distances, delimiter=','))
        distArray = np.array(distList)
    return distArray


def calcDistance(array, current, prev):
    row = int(current)
    col = int(prev)
    dist = array[row][col]
    if dist is None or dist == '':
        dist = array[col][row]
    return dist





