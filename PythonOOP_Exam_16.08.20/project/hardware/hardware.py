from project.software.software import Software
from typing import List


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if self.free_memory >= software.memory_consumption and self.free_capacity >= software.capacity_consumption:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

    @property
    def free_memory(self):
        return self.memory - self.used_memory

    @property
    def used_memory(self):
        return sum([s.memory_consumption for s in self.software_components])

    @property
    def free_capacity(self):
        return self.capacity - self.used_capacity

    @property
    def used_capacity(self):
        return sum([s.capacity_consumption for s in self.software_components])

    @property
    def names_of_all_software_components(self):
        return ", ".join(s.name for s in self.software_components)

    def __repr__(self):
        return f"Hardware Component - {self.name}\n" \
               f"Express Software Components: {len([s for s in self.software_components if s.type == 'Express'])}\n" \
               f"Light Software Components: {len([s for s in self.software_components if s.type == 'Light'])}\n" \
               f"Memory Usage: {self.used_memory} / {self.memory}\n" \
               f"Capacity Usage: {self.used_capacity} / {self.capacity}\n" \
               f"Type: {self.type}\n" \
               f"Software Components: {self.names_of_all_software_components}"
