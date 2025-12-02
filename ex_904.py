class Restaurant:
    """Klasa z kursu dotyczaca restauracji"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.number_served = 0
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name)

    def open_restaurant(self):
        print("the cuisine type of restaurant is " + self.cuisine_type)
        print(self.restaurant_name + " is open")

    def how_many_customers(self):
        print(f"the restaurant {self.restaurant_name} has served {self.number_served}")

    def set_number_served(self):
        while True:
            try:
                value  = int(input("Give me the number of served customers: "))
                if value >= 0:
                    self.number_served = value
                    break
                elif value < 0:
                    print("the number of customer served can't be negative ")
            except ValueError:
                print(f"give me the whole number")


mcdonald = Restaurant('mcdonald', 'fastfood')
mcdonald.how_many_customers()

mcdonald.set_number_served()

mcdonald.how_many_customers()
