from project.appliances.appliance import Appliance


class Stove(Appliance):
    app_cost = 0.7

    def __init__(self):
        super().__init__(Stove.app_cost)
