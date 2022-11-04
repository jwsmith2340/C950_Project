import datetime

class Truck:
    def __init__(self,truck_number,packages,time,total_distance = 0):
        self.truck_number = truck_number
        self.packages = packages
        self.time = time
        self.total_distance = total_distance
    
    def get_total_distance(self):
        return self.total_distance
    
    def update_total_distance(self,distance):
        self.total_distance = distance

    def __str__(self):
        return self.packages, self.time

# Here, I'm manually loading each truck and setting the time, as in the time they 
# leave the hub, according to delayed packages or packages with address updates.

# Space-time complexity: O(1)
truck_one_time = datetime.timedelta(hours = 8, minutes = 0)
truck_one = Truck(1, [1,13,14,15,16,19,20,29,30,31,34,37,40], truck_one_time)

# Space-time complexity: O(1)
truck_two_time = datetime.timedelta(hours = 9, minutes = 5)
truck_two = Truck(2, [3,6,18,25,28,32,36,38,2,4,5,7,8,10,11,12,17], truck_two_time)

# Space-time complexity: O(1)
truck_three_time = datetime.timedelta(hours = 10, minutes = 20)
truck_three = Truck(3, [9,21,22,23,24,26,27,33,35,39], truck_three_time)