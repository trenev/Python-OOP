class Survivor:
    max_health = 100
    max_needs = 100

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.health = self.max_health
        self.needs = self.max_needs

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age not valid!")
        self._age = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Health not valid!")
        elif value > self.max_health:
            value = self.max_health
        self._health = value

    @property
    def needs(self):
        return self._needs

    @needs.setter
    def needs(self, value):
        if value < 0:
            raise ValueError("Needs not valid!")
        elif value > self.max_needs:
            value = self.max_needs
        self._needs = value

    @property
    def needs_sustenance(self):
        return self.needs < self.max_needs

    @property
    def needs_healing(self):
        return self.health < self.max_health
