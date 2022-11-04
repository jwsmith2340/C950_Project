import datetime

class Package:
    def __init__(self,id,address,city,state,zip_code,deadline,kilograms,notes,truck_number = None,time_at_hub = None, time_en_route = None, time_delivered = None,delivery_status = "At hub"):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.kilograms = kilograms
        self.notes = notes
        self.truck_number = truck_number
        self.time_en_route = time_en_route
        self.time_delivered = time_delivered
        self.delivery_status = delivery_status

        on_time = datetime.timedelta(hours = 8)
        self.time_at_hub = on_time
        # Setting the hub time based on whether the CSV file mentioned the package being delayed
        if self.notes:
            if 'Delayed' in self.notes:
                delayed_time = datetime.timedelta(hours = 9, minutes = 5)
                self.time_at_hub = delayed_time
                self.delivery_status = "Delayed"
        else:
            self.notes = "None"
      
    def update_delivery_status(self,delivery_status):
        self.delivery_status = delivery_status
    
    def update_truck_number(self,number):
        self.truck_number = number

    def update_time_at_hub(self,time_at_hub):
        self.time_at_hub = time_at_hub

    def update_time_en_route(self,time_en_route):
        self.time_en_route = time_en_route

    def update_time_delivered(self,time_delivered):
        self.time_delivered = time_delivered

    def update_address(self, address):
        self.address = address

    def update_city(self, city):
        self.city = city

    def update_zip(self, zip):
        self.zip = zip

    def print_all_values(self):
        return self.id, self.address, self.city, self.state, self.zip_code, self.deadline, self.kilograms, self.notes, self.time_at_hub, self.time_en_route, self.time_delivered, self.delivery_status

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

    def get_truck_number(self):
        return self.truck_number
    
    def get_delivery_status(self):
        return self.delivery_status
    
    def get_time_at_hub(self):
        return self.time_at_hub

    def get_time_en_route(self):
        return self.time_en_route

    def get_time_delivered(self):
        return self.time_delivered