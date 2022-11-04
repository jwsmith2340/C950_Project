# James Smith 010649376
from HashMap import *
from Package import *
from Truck import *
from Adjacency import Vertex, Matrix
import csv

# Reading in data from csv files to populate packages, 
# address, and distances csv variables
with open('packages.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    packages_csv = list(csv_reader)

with open('addresses.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    addresses_csv = list(csv_reader)    

with open('distances.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    distances_csv = list(csv_reader) 

# An instance of the Matrix class is assigned
adjacency_matrix = Matrix()

# Space-time complexity: O(N^2)
# This iterates through the addresses_csv data to populate the
# adjacency matrix. The outer loop iterates through each address, 
# while the inner loop matches up every address, thereby creating
# each vertex of the matrix. The edge is also populated once the 
# vertices are created, and an undirected edge is created. 
for idx, address in enumerate(addresses_csv):
    for index, matched_address in enumerate(addresses_csv):
        if idx != index:
            if distances_csv[idx][index]: 
                x_vertex = Vertex(address[2])
                y_vertex = Vertex(matched_address[2])
                
                adjacency_matrix.add_vertex(x_vertex)
                adjacency_matrix.add_vertex(y_vertex)
                adjacency_matrix.add_undirected_edge(x_vertex, y_vertex, distances_csv[idx][index])

# An instance of the Hashmap is created. The length of the packages
# csv is passed in to determine how large the hash list will be                
hashmap = HashMap(len(packages_csv))

# Space-time complexity: O(N)
# Each package instance is created via the package class and the available values. 
# Those packages are then loaded into the hash map by id number. 
def populate_package_data(csv_list):
    for each in csv_list:
        new_package = Package(each[0],each[1],each[2],each[3],each[4],each[5],each[6],each[7])
        hashmap.add(int(each[0]), new_package)

populate_package_data(packages_csv)

# Space-time complexity: O(N^2)
# This is the Nearest Neighbor algorithm that delivers the packages.
def deliverPackages(truck):
    # Everything is based on the truck.time for retrieving package status later.
    truck_time = truck.time
    # Shortest distance assigned an impossibly large value.
    shortest_distance = 1000000
    # The hub address is the starting point for every package.
    hub_address = addresses_csv[0][2]
    # Declaring total_distance to keep track of distance traveled by each truck.
    total_distance = 0

    # The delayed package is on truck 3. Truck 3 leaves the hub at 10:20, right when
    # the package address needs to be updated. The truck.time for 
    # truck 3 is 10:20:00, so the address is updated when this truck
    # leaves the station. 
    if truck.truck_number == 3:
        hashmap.update_address_by_id(9,"410 S State St")
        hashmap.update_city_by_id(9,"Salt Lake City")
        hashmap.update_zip_by_id(9,"84111")
    
    # Updating every package's time en route to populate values in the user CLI correctly
    for package_id in truck.packages:
        # Solving a hashing issue, where 40 is hashed to index 0        
        if package_id == 40:
            package_id = 0
        hashmap.update_delivery_status_by_id(package_id, "en route")
        hashmap.update_time_en_route_by_id(package_id,truck_time)
    
    # While loop counts the truck packages, which are popped from the list as they are delivered
    while len(truck.packages) > 0:
        
        # Enumerate is used to grab the index of each package. That index value is used to pop
        # packages from the truck by index, which is faster than iterating through to find the id location
        for idx,package_id in enumerate(truck.packages):
            # Solving a hashing issue, where 40 is hashed to index 0
            if package_id == 40:
                package_id = 0

            # The package data and package address values are grabbed from the hash map
            package = hashmap.get_all_values_by_id(package_id)
            package_address = hashmap.get_address_by_id(package_id)
            hashmap.update_truck_number_by_id(package_id,truck.truck_number)

            # If a package is being delivered to the same place, the delivery time is not increased, 
            # and the mileage remains the same. 
            if hub_address == package_address:
                shortest_distance = 0
                shortest_package = package
                shortest_package_index = idx

            # Else, the adjacency matrix is checked for the nearest neighbor. Once a 'better' shortest 
            # distance is found, the value replaces any previous shortest distance value, and the current 
            # package becomes the shortest distance package. 
            elif float(adjacency_matrix.edge_weights[(hub_address, package_address)]) < shortest_distance:
                shortest_distance = float(adjacency_matrix.edge_weights[(hub_address, package_address)])
                shortest_package = package
                shortest_package_index = idx
                temp_package_address = package_address

        # Total distance is incremented by distance to each package address
        total_distance += shortest_distance
        # A new starting point is assigned each iteration based on which package will be delivered
        hub_address = temp_package_address
        # Truck time is calculated based on the shortest distance and the truck going 18mph
        truck.time += datetime.timedelta(minutes = (shortest_distance / (18 * (1 / 60))))

        # This block updates the delivery status of the package and updates the delivery time
        # Solving a hashing issue, where 40 is hashed to index 0        
        if int(shortest_package[0]) == 40:
            hashmap.update_delivery_status_by_id(0, "delivered")
            hashmap.update_time_delivered_by_id(0,truck.time)
        else:
            hashmap.update_delivery_status_by_id(int(shortest_package[0]), "delivered")
            hashmap.update_time_delivered_by_id(int(shortest_package[0]),truck.time)
        
        # The delivered package is removed from the list, and the shortest distance is 
        # again assigned an impossibly large value
        truck.packages.pop(shortest_package_index)
        shortest_distance = 1000000
    
    # Updating each truck with the total distance
    truck.update_total_distance(total_distance)

# Starting each delivery
deliverPackages(truck_one) # 30.1 Miles
deliverPackages(truck_two) # 40.6 Miles 
deliverPackages(truck_three) # 24.2 Miles

# Space-time complexity: O(1)
def command_line_interface():

    user_prompt = int(input("Enter 1 to check an individual package, 2 to check all packages  "))

    if user_prompt > 0 and user_prompt < 3:

        # Gathering and parsing the user's time to make comparisons of timedelta values
        user_time = input("Input the time you want to check in HH:MM:SS format between 08:00:00 and 20:00:00  ")
        user_time_hours = int(user_time.split(":")[0])
        user_time_minutes = int(user_time.split(":")[1])
        user_time_seconds = int(user_time.split(":")[2])

        user_time_delta = datetime.timedelta(hours = user_time_hours, minutes = user_time_minutes, seconds = user_time_seconds)

        # Setting boundaries for user input
        lower_limit_time = datetime.timedelta(hours = 8)
        upper_limit_time = datetime.timedelta(hours = 20)

        # If the user selected a valid time, proceed
        if user_time_delta <= upper_limit_time and user_time_delta >= lower_limit_time:
            if user_prompt == 1:
                user_package = int(input("Enter the package ID you want to check  "))
                package_address = hashmap.get_address_by_id(user_package)
                package_city = hashmap.get_city_by_id(user_package)
                package_state = hashmap.get_state_by_id(user_package)
                package_zip = hashmap.get_zip_code_by_id(user_package)
                full_package_address = f"{package_address}, {package_city}, {package_state}, {package_zip}"
                package_deadline = hashmap.get_deadline_by_id(user_package)
                package_note = hashmap.get_notes_by_id(user_package)
                print(f"Package ID:  {user_package}\nPackage Address:  {full_package_address}\nDeadline:  {package_deadline}\nNote:  {package_note}")

            elif user_prompt == 2:
                for package_id in range(1,41):
                    # Assigning a package's times at the hub, en route, and delivered to be used in logical statment
                    if package_id == 40:
                        package_id = 0  
                    time_at_hub = hashmap.get_time_at_hub_by_id(package_id)
                    time_en_route = hashmap.get_time_en_route_by_id(package_id)
                    time_delivered = hashmap.get_time_delivered_by_id(package_id)
                    truck_number = hashmap.get_truck_number_by_id(package_id)

                    if package_id == 0:
                        package_id = 40   
                    # This if/else statement checks to see if a package has been delivered based on the time_delivered value.
                    # If it has no, it checks to see when the package was en route. If the package was not en route, it checks
                    # to see when the package arrived at the hub. If it never did, it means the package was delayed. Depending
                    # on the logic route, the appropriate message is delivered to the user regarding the status of their specified
                    # package at the specified time. 
                    if time_delivered != None and time_delivered <= user_time_delta:
                        print(f"Package {package_id}    Status at {user_time_delta}: Delivered by Truck {truck_number}")
                    elif time_en_route != None and time_en_route <= user_time_delta:
                        print(f"Package {package_id}    Status at {user_time_delta}: En Route on Truck {truck_number}")
                    elif time_at_hub != None and time_at_hub <= user_time_delta:
                        print(f"Package {package_id}    Status at {user_time_delta}: At the Hub")
                    else:
                        print(f"Package {package_id}    Status at {user_time_delta}: Delayed")

            print("\nScheduled miles and delivery times for each truck:")
            print(f"Truck {truck_one.truck_number} traveled {truck_one.total_distance} total miles and delivered its final package at {truck_one.time}.")
            print(f"Truck {truck_two.truck_number} traveled {truck_two.total_distance} total miles and delivered its final package at {truck_two.time}.")
            print(f"Truck {truck_three.truck_number} traveled {truck_three.total_distance} total miles and delivered its final package at {truck_three.time}.")
            print(f"The total distance traveled was {truck_one.total_distance + truck_two.total_distance + truck_three.total_distance} miles")

        else:
            print("Time given was out of bounds.")

    else: 
        print("User input did not match prompt.")

    # This concludes the CLI prompts and ends the program. 
    print("Thank you for using the WGUPS package tracking system. Goodbye.")
    
command_line_interface()

# Overall space-time complexity= O(N^2)