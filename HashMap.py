# Going to insert into cells based on 1's place via Mod %

class HashMap:

    def __init__(self):
        self.size = 10
        self.map = [[],[],[],[],[],[],[],[],[],[]]

    def add(self, key, value):
        key_hash = self.get_hash(key)
        self.map[key_hash].append(value)

    def get_hash(self,key):
        return key % self.size

    # dumpster fire, come bsack to this, don't even know if it's needed
    def get_value_by_id(self,id):
        key = self.get_hash(id)
        print(type(key))
        print(key)
        print(self.map[key])
        for each in self.map[key]:
            if each == key:
                print('hooray')

hash = HashMap()
hash.add(1,25)
hash.add(11,35)
hash.add(21,45)

#print(hash.map)

hash.get_value_by_id(21)



