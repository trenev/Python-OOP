class Appliance:
    days_count = 30

    def __init__(self, cost: float):
        self.cost = cost

    def get_monthly_expense(self):
        return self.cost * Appliance.days_count
