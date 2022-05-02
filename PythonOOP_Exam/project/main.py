from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.controller import Controller
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

r1 = FreshwaterFish("R1", "Fresh", 10)
r2 = SaltwaterFish("R2", "Salt", 5)
d1 = Plant()
d2 = Ornament()

qqqq = Controller()
# aqua = SaltwaterAquarium("water")
print(qqqq.add_aquarium("SaltwaterAquarium", "water"))
print(qqqq.add_aquarium("FreshwaterAquarium", "water2"))

print(qqqq.add_decoration("Plant"))
print(qqqq.add_decoration("Ornament"))
print(qqqq.insert_decoration("water", "Plant"))
print(qqqq.insert_decoration("water", "Ornament"))

print(qqqq.calculate_value("water"))

# print(aqua.add_fish(r1))
# print(aqua.add_fish(r2))
# print(aqua.fish)
print(qqqq.add_fish("water", "SaltwaterFish", "fname", "spec", 10))
print(qqqq.add_fish("water", "SaltwaterFish", "f2name", "spec", 5))
print(qqqq.feed_fish("water"))
print(qqqq.calculate_value("water"))
print(qqqq.report())

