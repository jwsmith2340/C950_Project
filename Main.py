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
                x_vertex = Vertex(address[1])
                y_vertex = Vertex(matched_address[1])
                print(x_vertex.__str__())
                print(y_vertex.__str__())
                print("***")
                adjacency_graph.add_vertex(x_vertex)
                adjacency_graph.add_vertex(y_vertex)
                adjacency_graph.add_directed_edge(x_vertex, y_vertex, distances_csv[idx][index])
                # print(adjacency_graph.edge_weights.__str__())
                
                # print(matched_address)
                # print(distances_csv[idx][index])
            # print(idx,index)
            # print(address)
            # print(matched_address)
            # print("*****")

print(adjacency_graph.edge_weights[("Wheeler Historic Farm", "City Center of Rock Springs")])

hashmap = HashMap(len(packages_csv))
#print(hashmap.map)

hashmap.add(7,33)
hashmap.add(3,44)
# print(hashmap.map)

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

# print(hashmap.get_value_by_id(20))

def get_hash_list(key_id):
    print(key_id)

# print(truck_one)
# print(truck_two)
# print(truck_three)

