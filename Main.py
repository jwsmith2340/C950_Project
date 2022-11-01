# Three Trucks, Two Drivers
# 40 Packages each day
# 140 miles or less per requirements
# Need to be able to look up truck/package status by package_id

# ASSUMPTIONS
# Each truck can carry MAX 16 packages
# Trucks drive an average 18mph, no crashes, no fuel concerns
# Drivers don't hop trucks in the middle of a route, they stay with hte truck through completion
# Loading time is instant
# Drivers leave the hub at 8am or later
# Distances in the distance table are equal regardless of distance traveled(?)
# The day ends when all the packages are delivered
from HashMap import *
from Package import *
from Truck import *
import csv

hashmap = HashMap()
#print(hashmap.map)

hashmap.add(3,33)
hashmap.add(3,44)
print(hashmap.map)



with open('packages.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    list_of_csv = list(csv_reader)

def populate_package_data(csv_list):
    # print("in function")
    # print(csv_list)
    # print("done with function")
    for each in csv_list:
        #print(each)
        new_package = Package(each[0],each[1],each[2],each[3],each[4],each[5],each[6],each[7])
        hashmap.add(int(each[0]), new_package)
        #new_package.print_all_values()

populate_package_data(list_of_csv)

print(hashmap.map[0])

print(truck_one)