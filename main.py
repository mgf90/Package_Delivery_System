# Moses Farmer
# ID: 001539795

from HashMap import *
from Distance import Distance
from Route import Route
from Truck import Truck


class main:

    # these are the lists for loading the trucks
    pack1 = [1, 6, 16, 20, 25, 29, 30, 31, 32, 33, 40]
    pack2 = [3, 13, 14, 15, 17, 18, 19, 21, 34, 36, 37, 38, 39]
    pack3 = [2, 4, 5, 7, 8, 9, 10, 11, 12, 22, 23, 24, 26, 27, 28, 35]

    map = HashMap()
    truck = Truck()

    # each loop is O(n)
    # each loop loads the three trucks
    for i in pack1:
        truck.load_truck1(i, map)

    for i in pack2:
        truck.load_truck2(i, map)

    for i in pack3:
        truck.load_truck3(i, map)

    print("The trucks are loaded!")

    distance = Distance()
    route = Route(distance)

    print('Welcome to the Package Delivery System!\n')

    # initializes each truck
    truck1 = route.organize(truck.truck1)
    truck2 = route.organize(truck.truck2)
    truck3 = route.organize(truck.truck3)

    all_trucks = truck1 + truck2 + truck3

    # sets the time each truck will leave
    leave_time1 = ['8:00:00']
    leave_time2 = ['8:00:00']
    leave_time3 = ['10:00:00']

    # calculates time for each truck's route
    truck_time1 = route.truck_time(truck1, leave_time1)
    truck_time2 = route.truck_time(truck2, leave_time2)
    truck_time3 = route.truck_time(truck3, leave_time3)

    # calculates distance for each truck
    truck1_dist = distance.calc_total_distance(truck1)
    truck2_dist = distance.calc_total_distance(truck2)
    truck3_dist = distance.calc_total_distance(truck3)
    total_dist = round(truck1_dist + truck2_dist + truck3_dist)

    # begins the command line interface
    exit_program = False
    while not exit_program:

        print('Please enter the number associated with your desired action:')
        print('1. Lookup a package')
        print('2. Delivery status')
        print('3. Exit the program')
        choice = input()

        # lookup a package by id number
        if (choice == '1'):
            print('Please enter your package ID:')
            p_ID = int(input())

            # Time: O(n)
            # Space: O(n)
            # searches every package for the matching id
            for p in all_trucks:
                if p == map.search(p_ID):
                    pk = p

            print(f'ID: {pk.get_id()} || {pk.get_address()}, {pk.get_city()}, {pk.get_state()} {pk.get_zip()} || '
                  f'{pk.get_weight()} pounds')

        # displays the status of all packages by time
        elif (choice == '2'):

            print('Please enter a time in HH:MM:SS format:')
            time = input()

            route.get_report(truck1, "Truck 1", truck1_dist, truck_time1, time)
            route.get_report(truck2, "Truck 2", truck2_dist, truck_time2, time)
            route.get_report(truck3, "Truck 3", truck3_dist, truck_time3, time)
            print(f'\nTotal distance travelled is {total_dist} miles.\n')

        # exits the program
        elif (choice == '3'):
            print('Exiting....\nGoodbye!')
            exit(0)
            exit_program = True

        else:
            print('Invalid input. Please try again\n')

