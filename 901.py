class Restaurant:
    """Klasa z kursu dotyczaca restauracji"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name)

    def open_restaurant(self):
        print("the cuisine type of restaurant is " + self.cuisine_type)
        print(self.restaurant_name + " is open")

mcdonald = Restaurant('mcdonald', 'fastfood')

mcdonald.open_restaurant()
mcdonald.describe_restaurant()

