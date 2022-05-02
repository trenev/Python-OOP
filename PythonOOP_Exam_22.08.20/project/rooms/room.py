class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.appliances = []
        self.expenses = 0

    def __repr__(self):
        result = [f"{self.family_name} with {self.members_count} members. "
                  f"Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$"]
        for child in self.children:
            result.append(f"--- Child {self.children.index(child)+1} monthly cost: {child.get_monthly_expense():.2f}$")
        result.append(f"--- Appliances monthly cost: {self.appliances_monthly_cost:.2f}$")
        return "\n".join(result)

    def calculate_expenses(self, *args):
        result = 0
        for element in args:
            for el in element:
                result += el.get_monthly_expense()
        self.expenses = result

    @property
    def expenses(self):
        return self._expenses
    
    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = value

    @property
    def appliances_monthly_cost(self):
        return sum(app.get_monthly_expense() for app in self.appliances)

