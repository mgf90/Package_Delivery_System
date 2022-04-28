from HashMap import *
from Distance import Distance
from Route import Route
from Truck import Truck
from Package import Package
import re


class main:

    pack1 = [1, 6, 16, 20, 25, 29, 30, 31, 32, 33, 40]
    pack2 = [3, 13, 14, 15, 17, 18, 19, 21, 34, 36, 37, 38, 39]
    pack3 = [2, 4, 5, 7, 8, 9, 10, 11, 12, 22, 23, 24, 26, 27, 28, 35]

    map = HashMap()
    truck = Truck()
    # truck.loadTrucks(map.packages)

    for i in pack1:
        truck.load_truck1(i, map)

    for i in pack2:
        truck.load_truck2(i, map)

    for i in pack3:
        truck.load_truck3(i, map)

    print("The trucks are loaded!")

    distance = Distance()
    route = Route(distance)
    dist_array = Distance.fill_dist(distance)

    print('Welcome to the Package Delivery System!\n')

    truck1 = route.organize(truck.truck1)
    truck2 = route.organize(truck.truck2)
    truck3 = route.organize(truck.truck3)
    all_trucks = truck1 + truck2 + truck3

    print(truck1[0])

    # print(all_trucks[0])

    leave_time1 = ['8:00:00']
    leave_time2 = ['8:00:00']
    leave_time3 = ['9:05:00']

    truck_time1 = route.truck_time(truck1, leave_time1)
    truck_time2 = route.truck_time(truck2, leave_time2)
    truck_time3 = route.truck_time(truck3, leave_time3)

    truck1_dist = distance.calc_total_distance(truck1)
    truck2_dist = distance.calc_total_distance(truck2)
    truck3_dist = distance.calc_total_distance(truck3)
    total_dist = round(truck1_dist + truck2_dist + truck3_dist)

    exit_program = False
    while not exit_program:

        print('Please enter the number associated with your desired action:')
        print('1. Lookup a package')
        print('2. Delivery status')
        print('3. Exit the program')
        choice = input()

        if (choice == '1'):
            print('Please enter your package ID:')
            p_ID = int(input())

            for p in all_trucks:
                if p == map.lookup(p_ID):
                    pk = p

            print(f'ID: {pk.get_id()} || {pk.get_address()}, {pk.get_city()}, {pk.get_state()} {pk.get_zip()} || '
                  f'{pk.get_weight()} pounds')

        elif (choice == '2'):


            print(truck1_dist,'\n',truck2_dist,'\n',truck3_dist,'\n',total_dist)

            print('Please enter a time in HH:MM:SS format:')
            time = input()

            route.get_report("truck1", truck1, truck_time1, time, truck1_dist)
            route.get_report("truck2", truck2, truck_time2, time, truck2_dist)
            route.get_report("truck3", truck3, truck_time3, time, truck3_dist)

        elif (choice == '3'):
            print('Exiting....\nGoodbye!')
            exit(0)
            exit_program = True

        else:
            print('Invalid input. Please try again\n')

