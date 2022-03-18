from HashMap import *



class Main:
    print('Package Delivery System is now online')

    mp = HashMap()
    mp.insert(4, 'box')
    print(mp.lookup(4))

    mp.delete(4)
    print(mp.lookup(4))


