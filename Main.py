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
from functools import total_ordering
from json.encoder import INFINITY
from HashMap import *
from Package import *
from Truck import *
from Adjacency import Vertex, Graph
import csv

with open('packages.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    packages_csv = list(csv_reader)

with open('addresses.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    addresses_csv = list(csv_reader)    

with open('distances.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    distances_csv = list(csv_reader) 

# print(packages_csv)
# print("**********************")
# print(addresses_csv)
# print("**********************")
# print(distances_csv)

adjacency_graph = Graph()

for idx, address in enumerate(addresses_csv):
    for index, matched_address in enumerate(addresses_csv):
        if idx != index:
            if distances_csv[idx][index]: 
                x_vertex = Vertex(address[2])
                y_vertex = Vertex(matched_address[2])
                # print(x_vertex.__str__())
                # print(y_vertex.__str__())
                # print("***")
                adjacency_graph.add_vertex(x_vertex)
                adjacency_graph.add_vertex(y_vertex)
                adjacency_graph.add_undirected_edge(x_vertex, y_vertex, distances_csv[idx][index])
                # print(adjacency_graph.edge_weights.__str__())
                # print(matched_address)
                # print(distances_csv[idx][index])
            # print(idx,index)
            # print(address)
            # print(matched_address)
            # print("*****")
# print(adjacency_graph.edge_weights)
# This is how I'm going to access my weight values between places
# print(adjacency_graph.edge_weights[("Wheeler Historic Farm", "City Center of Rock Springs")])

hashmap = HashMap(len(packages_csv))
#print(hashmap.map)

def populate_package_data(csv_list):
    # print("in function")
    # print(csv_list)
    # print("done with function")
    for each in csv_list:
        #print(each)
        new_package = Package(each[0],each[1],each[2],each[3],each[4],each[5],each[6],each[7])
        hashmap.add(int(each[0]), new_package)
        #new_package.print_all_values()

populate_package_data(packages_csv)

# These are all of the available hashmap methods that call the package methods to display values
# Get all values in a formatted string
# print(hashmap.get_all_values_by_id(20))
# Get the address value for a package, this is what will be used in the tuples for the edge weights
# print(hashmap.get_address_by_id(20))
# print(hashmap.get_city_by_id(20))
# print(hashmap.get_state_by_id(20))
# print(hashmap.get_zip_code_by_id(20))
# print(hashmap.get_deadline_by_id(20))
# print(hashmap.get_kilograms_by_id(20))
# print(hashmap.get_notes_by_id(20))


def get_hash_list(key_id):
    print(key_id)

# print(truck_one)
# print(truck_two)
# print(truck_three)

def deliverPackages(truck):
    print("truck", truck)

    

    shortest_distance = 1000000
    starting_len = len(truck)
    print(starting_len)
    hub_address = addresses_csv[0][2]
    print(hub_address)
    total_distance = 0
    while len(truck) > 0:
        print(truck)
        for idx,package_id in enumerate(truck):
            # print(package_id)

            # Solving a hashing issue, where 40 is hashed to index 0
            if package_id == 40:
                package_id = 0

            ###############
            # PICK UP HERE
            # Right now, we're only going through the first time to pick the shortest distance
            # The problem is, we keep deleting idx 2 if we set up a while loop. We need to set up
            # the shortest distance = 9999 somewhere outside of the for loop we're in now, so 
            # maybe before the for inside the while. Also need to clear the package_address each time a 
            # new loop is entered into as well. 
            ###############
            # This is printing off the correct packages, with the correct data, and the distance between the two
            package = hashmap.get_all_values_by_id(package_id)
            # print(package)
            package_address = hashmap.get_address_by_id(package_id)
            # print(adjacency_graph.edge_weights[(hub_address, package_address)])
            if hub_address == package_address:
                print('yup')
                shortest_distance = 0
                shortest_package = package
                shortest_package_index = idx
            elif float(adjacency_graph.edge_weights[(hub_address, package_address)]) < shortest_distance:
                shortest_distance = float(adjacency_graph.edge_weights[(hub_address, package_address)])
                shortest_package = package
                # print('index', idx)
                shortest_package_index = idx
                temp_package_address = package_address
            
        # What do I need? 
        # 1) I need to push the shortest package id into an new array
        # 2) I need to remove that package id from the original truck array
        # 3) I need to update my current location to be a new variable value, not hub_address
        # 4) I need to create a similar flow in my initial else clause, where I iterate through
        #       everything, popping and appending correctly
        # print("shortest_idx", shortest_package_index)
        print("shortest distance", shortest_distance)
        total_distance += shortest_distance
        print("shortest package", shortest_package)
        print("temp package address, will become next hub address here", temp_package_address)
        hub_address = temp_package_address
        print("shortest package index:", shortest_package_index)
        truck.pop(shortest_package_index)
        shortest_distance = 1000
        print("**********")
        # print(f"truck after the the {idx} index iteration", truck)
    
    print("total distance for this truck: ", total_distance)
        




# deliverPackages(truck_one) # 30.1 Miles
deliverPackages(truck_two) # 40.6 Miles 
# deliverPackages(truck_three) # 24.2 Miles


for each in range(0,40):
    print(hashmap.get_all_values_by_id(each))