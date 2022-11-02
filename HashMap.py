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

    def get_all_values_by_id(self,id):
        return self.map[id].print_all_values()
    
    def get_address_by_id(self,id):
        return self.map[id].get_address()

    def get_city_by_id(self,id):
        return self.map[id].get_city()
    
    def get_state_by_id(self,id):
        return self.map[id].get_state()
    
    def get_zip_code_by_id(self,id):
        return self.map[id].get_zip_code()
   
    def get_deadline_by_id(self,id):
        return self.map[id].get_deadline()
    
    def get_kilograms_by_id(self,id):
        return self.map[id].get_kilograms()
    
    def get_notes_by_id(self,id):
        return self.map[id].get_notes()
