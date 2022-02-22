class Present:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
    
    def __str__(self):
        return f"{self.name} ({self.weight} kg)"

class Box:
    def __init__(self):
        self.presents = []
    
    def add_present(self, present: Present):
        self.presents.append(present)
    
    def total_weight(self):
        total_weight = 0
        for present in self.presents:
            total_weight += present.weight
        return total_weight