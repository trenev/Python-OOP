from calendar import month_name


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction " \
               f"{self.age_restriction}. Status: {self.check_is_rented()}"

    def check_is_rented(self):
        if self.is_rented:
            return "rented"
        return "not rented"

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        return cls(name, id, int(date[-4:]), month_name[int(date[3:5])], age_restriction)
