class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def is_enough_budget(self, amount: int):
        return amount <= self.__budget

    def is_enough_space_for_animals(self):
        return len(self.animals) < self.__animal_capacity

    def is_enough_space_for_workers(self):
        return len(self.workers) < self.__workers_capacity

    def add_animal(self, animal, price: int):
        if self.is_enough_budget(price) and self.is_enough_space_for_animals():
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if not self.is_enough_budget(price) and self.is_enough_space_for_animals():
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if not self.is_enough_space_for_workers():
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        worker = [f for f in self.workers if f.name == worker_name]
        if not worker:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker[0])
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        workers_salaries = sum([w.salary for w in self.workers])
        if not self.is_enough_budget(workers_salaries):
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= workers_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed_money = sum([a.get_needs() for a in self.animals])
        if not self.is_enough_budget(needed_money):
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= needed_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]
        result = f"You have {len(self.animals)} animals\n----- {len(lions)} Lions:"
        for l in lions:
            result += f"\n{l}"
        result += f"\n----- {len(tigers)} Tigers:"
        for t in tigers:
            result += f"\n{t}"
        result += f"\n----- {len(cheetahs)} Cheetahs:"
        for c in cheetahs:
            result += f"\n{c}"
        return result

    def workers_status(self):
        keepers = [a for a in self.workers if a.__class__.__name__ == "Keeper"]
        caretakers = [a for a in self.workers if a.__class__.__name__ == "Caretaker"]
        vets = [a for a in self.workers if a.__class__.__name__ == "Vet"]
        result = f"You have {len(self.workers)} workers\n----- {len(keepers)} Keepers:"
        for l in keepers:
            result += f"\n{l}"
        result += f"\n----- {len(caretakers)} Caretakers:"
        for t in caretakers:
            result += f"\n{t}"
        result += f"\n----- {len(vets)} Vets:"
        for c in vets:
            result += f"\n{c}"
        return result

