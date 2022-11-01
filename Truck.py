class Truck:

    def __init__(self,vehicle_num):
        self.vehicle_num = vehicle_num

    def __str__(self):
        return f"This is truck {self.vehicle_num}"