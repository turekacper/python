class Restaurant:
    """Klasa dotyczaca restauracji ale trzy przypadki"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name)

    def open_restaurant(self):
        print("the cuisine type of restaurant is " + self.cuisine_type)
        print(self.restaurant_name + " is open")


kfc = Restaurant('kfc', 'fastfood')
kfc.open_restaurant()
kfc.describe_restaurant()


pod_okoniem = Restaurant('pod_okoniem', 'rybna')
pod_okoniem.open_restaurant()
pod_okoniem.describe_restaurant()
