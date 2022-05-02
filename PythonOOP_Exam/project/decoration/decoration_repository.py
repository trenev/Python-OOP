class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration not in self.decorations:
            return False
        self.decorations.remove(decoration)
        return True

    def find_by_type(self, decoration_type: str):
        result = [decoration for decoration in self.decorations if decoration.__class__.__name__ == decoration_type]
        if len(result) == 0:
            return "None"
        return result[0]
