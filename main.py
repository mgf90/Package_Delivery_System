from HashMap import *
from Distance import Distance
from Route import Route
from Truck import Truck
from Package import Package
import re


class main:

    map = HashMap()
    distance = Distance()
    route = Route(distance)
    dist_array = Distance.fill_dist(distance)
    truck = Truck()

    print('Welcome to the Package Delivery System!\n')

    truck.loadTrucks(map.packages)
    truck1 = route.organize(truck.truck1)
    truck2 = route.organize(truck.truck2)
    truck3 = route.organize(truck.truck3)
    all_trucks = truck1 + truck2 + truck3

    # print(all_trucks[0])

    leave_time1 = ['8:00:00']
    leave_time2 = ['10:00:00']
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
            sec_time = route.time_to_sec(time)

            route.get_report("truck1", truck1, truck_time1, '', truck1_dist)
            route.get_report("truck2", truck2, truck_time2, '', truck2_dist)
            route.get_report("truck3", truck3, truck_time3, '', truck3_dist)

        elif (choice == '3'):
            print('Exiting....\nGoodbye!')
            exit(0)
            exit_program = True

        else:
            print('Invalid input. Please try again\n')

