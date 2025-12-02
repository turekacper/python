class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.read_odometer()

    def read_odometer(self):
        self.odometer = str(input("give me the odometer's value: "))

    def present_car(self):
        print(f"The car is {self.make}. The model is {self.model}. The year of production is {self.year}.")

car1 = Car('japanese', 'toyota', '1999')
print(car1.odometer)
