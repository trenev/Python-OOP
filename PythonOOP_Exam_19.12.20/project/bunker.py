from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        result = self.supplies_by_type("FoodSupply")
        if len(result) == 0:
            raise IndexError("There are no food supplies left!")
        return result

    @property
    def water(self):
        result = self.supplies_by_type("WaterSupply")
        if len(result) == 0:
            raise IndexError("There are no water supplies left!")
        return result

    @property
    def painkillers(self):
        result = self.medicine_by_type("Painkiller")
        if len(result) == 0:
            raise IndexError("There are no painkillers left!")
        return result

    @property
    def salves(self):
        result = self.medicine_by_type("Painkiller")
        if len(result) == 0:
            raise IndexError("There are no salves left!")
        return result

    def supplies_by_type(self, supply_type):
        return [supply for supply in self.supplies if supply.__class__.__name__ == supply_type]

    def medicine_by_type(self, medicine_type):
        return [medicine for medicine in self.medicine if medicine.__class__.__name__ == medicine_type]

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            for medicine in self.medicine[::-1]:
                if medicine.__class__.__name__ == medicine_type:
                    medicine.apply(survivor)
                    self.medicine.pop(self.medicine.index(medicine))
                    return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            for supply in self.supplies[::-1]:
                if supply.__class__.__name__ == sustenance_type:
                    supply.apply(survivor)
                    self.supplies.pop(self.supplies.index(supply))
                    return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")


a = Bunker()
v = 1