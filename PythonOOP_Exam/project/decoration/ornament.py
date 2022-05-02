from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    initial_comfort = 1
    initial_price = 5

    def __init__(self):
        super().__init__(self.initial_comfort, self.initial_price)
