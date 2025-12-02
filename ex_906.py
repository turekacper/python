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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.proposed_flavors = []

    def get_custom_flavors(self):
        print(
            f"give me the propositions of the flavors you would like to see in restaruant {self.restaurant_name}: "
        )
        arr = []
        i = 1
        while True:
            value = input(f"Give me {i}. the proposition of flavor: ")
            if value.lower() == "q":
                break
            else:
                i += 1
                arr.append(value)
        # creating  instance of flavors within class
        self.proposed_flavors = arr

    def flavors(self):
        print(
            f"the flavors of ice cream available in restaurant {self.restaurant_name} are: "
        )

        for flavor in self.proposed_flavors:
            print(flavor)


restauracja1 = IceCreamStand("polskie_jadlo", "polaska")
restauracja1.get_custom_flavors()
restauracja1.flavors()
