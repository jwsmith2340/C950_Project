
# length = 15
# 0900a - 15
# 1030a - 1,13,14,16,20,25,29,30,31,34,37,40
# item 15 has to be delivered by 9a, everything else after that, so probably start there
# 13,14,15,19 - must be delivered together
truck_one = [1,13,14,15,16,19,20,29,30,31,34,37,40]
# print(len(truck_one))

# length = 
# 3,18,36,38 - only on truck 2
# 6,25,28,32 - delayed, arrives at 905a
# 6 has a 1030 deadline, you have to start the deliveries with 6, 25 also deadline
truck_two = [3,6,18,25,28,32,36,38,2,4,5,7,8,10,11,12,17]
# print(len(truck_two))

# length = 
# 9 - wrong address listed
truck_three = [9,21,22,23,24,26,27,33,35,39]
# print(len(truck_three))


loaded = [1,3,6,13,14,15,16,18,19,20,25,28,29,30,31,32,34,36,37,38,40]
not_loaded = [2,4,5,7,8,10,11,12,17,21,22,23,24,26,27,33,35,39]
# 2,4,5,7,8,10,11,12,17 loaded on truck 2 for development, not optimal
# 21,22,23,24,26,27,33,35,39 loaded on truck 3 for development, not optimal

# print(len(loaded))
#print(len(not_loaded))