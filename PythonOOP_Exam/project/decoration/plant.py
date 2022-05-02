from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    initial_comfort = 5
    initial_price = 10

    def __init__(self):
        super().__init__(self.initial_comfort, self.initial_price)
