class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Transmission:
    def __init__(self, type):
        self.type = type

class Car(Engine, Transmission):
    def __init__(self, horsepower, type, brand):
        Engine.__init__(self, horsepower)
        Transmission.__init__(self, type)
        self.brand = brand

class SportsCar(Car):
    def __init__(self, horsepower, type, brand, top_speed):
        super().__init__(horsepower, type, brand)
        self.top_speed = top_speed

    def get_sports_car_info(self):
        return f"{self.brand} sports car with {self.horsepower} HP, {self.type} transmission, top speed {self.top_speed} mph"
