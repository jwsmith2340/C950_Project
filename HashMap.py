# Going to insert into cells based on 1's place via Mod %
from Package import *

class HashMap:

    def __init__(self,size):
        self.size = size
        self.map = [None] * size 

    def add(self, key, value):
        key_hash = self.get_hash(key)
        self.map[key_hash] = value

    def get_hash(self,key):
        return key % self.size

    def get_value_by_id(self,id):
        return self.map[id]

# hash = HashMap()
# hash.add(25,25)
# hash.add(35,35)
# hash.add(45,45)

# #print(hash.map)

# hash.get_value_by_id(35)



