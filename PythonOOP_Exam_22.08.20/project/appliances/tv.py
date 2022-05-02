from project.appliances.appliance import Appliance


class TV(Appliance):
    app_cost = 1.5

    def __init__(self):
        super().__init__(TV.app_cost)
