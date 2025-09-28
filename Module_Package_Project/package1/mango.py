class Apple:
    def __init__(self, number_of_apples):
        self.name = "Apple"
        self.number_of_apples = number_of_apples

    def get_name(self):
        return self.name


class Banana:
    def __init__(self, number_of_bananas):
        self.number_of_bananas = number_of_bananas
        self.name = "Banana"

    def get_name(self):
        return self.name
