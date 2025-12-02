"""A simple attempt to represent a car."""
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles


            

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

class Battery:

    """A simple class to give information about battery of an electric car"""
    """class initializises battery size at 20"""

    def __init__(self, battery_size=20):
        self.battery_size = battery_size

    def get_range(self, car):
        """Print a statement about the range this battery provides."""
        range = self.battery_size * 50
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
    def upgrade_battery(self):
        if self.battery_size <= 80:
            self.battery_size = 80
        else:
            print(f"Your battery doesn't require recharging.")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range(my_tesla)
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range(my_tesla)

