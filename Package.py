import re


class Package:
    def __init__(self,id,address,city,state,zip_code,deadline,kilograms,notes,time_delivered = None,delivery_status = "At hub"):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.kilograms = kilograms
        self.notes = notes
        self.time_delivered = time_delivered
        self.delivery_status = delivery_status

        if self.notes:
            if 'Delayed' in self.notes:
                self.delivery_status = "Delayed"
        
    
    def update_delivery_status(self,delivery_status):
        self.delivery_status = delivery_status

    def update_address(self, address):
        self.address = address

    def update_city(self, city):
        self.city = city

    def update_zip(self, zip):
        self.zip = zip

    def print_all_values(self):
        return self.id, self.address, self.city, self.state, self.zip_code, self.deadline, self.kilograms, self.notes, self.time_delivered, self.delivery_status

    def get_id(self):
        return self.id

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip_code(self):
        return self.zip_code

    def get_deadline(self):
        return self.deadline

    def get_kilograms(self):
        return self.kilograms

    def get_notes(self):
        return self.notes
    
    def get_delivery_status(self):
        return self.delivery_status
    
    # def __str__(self):
    #     return f"Key:{self.id}, Address:{self.address}, City:{self.city}, State:{self.state}, Zip:{self.zip_code}, Deadline:{self.deadline}, Weight:{self.kilograms}, Notes:{self.notes}"