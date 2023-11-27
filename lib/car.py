from vehicle import Vehicle

class Car(Vehicle):
    
        def __init__(self, wheel_size, wheel_number):
              self.wheel_number = wheel_number
              self.wheel_size = wheel_size
    
        def go(self):
            return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"