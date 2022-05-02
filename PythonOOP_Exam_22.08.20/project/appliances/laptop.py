from project.appliances.appliance import Appliance


class Laptop(Appliance):
    app_cost = 1.0

    def __init__(self):
        super().__init__(Laptop.app_cost)
