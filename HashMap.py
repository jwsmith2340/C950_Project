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

    def get_delivery_status_by_id(self,id):
        return self.map[id].get_delivery_status()

    def get_truck_number_by_id(self,id):
        return self.map[id].get_truck_number()
    
    def get_time_at_hub_by_id(self,id):
        return self.map[id].get_time_at_hub()

    def get_time_en_route_by_id(self,id):
        return self.map[id].get_time_en_route()
        
    def get_time_delivered_by_id(self,id):
        return self.map[id].get_time_delivered()

    def update_delivery_status_by_id(self,id,status):
        self.map[id].update_delivery_status(status)
    
    def update_truck_number_by_id(self,id,number):
        self.map[id].update_truck_number(number)  
    
    def update_time_at_hub_by_id(self,id,time):
        self.map[id].update_time_at_hub(time)

    def update_time_en_route_by_id(self,id,time):
        self.map[id].update_time_en_route(time)

    def update_time_delivered_by_id(self,id,time):
        self.map[id].update_time_delivered(time)
    
    def update_address_by_id(self,id,address):
        self.map[id].update_address(address)

    def update_city_by_id(self,id,city):
        self.map[id].update_city(city)

    def update_zip_by_id(self,id,zip):
        self.map[id].update_zip(zip)