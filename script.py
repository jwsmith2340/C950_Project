import datetime
from Truck import *
nine = datetime.time(9,0,0)
ten = datetime.time(10,0,22)
print(nine)
print(ten)

if nine > ten:
    print("WRONG")
elif ten > nine:
    print("correct time logic")
else:
    print("wtf why am i in the else")

truck_one = Truck([1,13,14,15,16,19,20,29,30,31,34,37,40], nine)

print(truck_one.__str__())