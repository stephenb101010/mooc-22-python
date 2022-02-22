class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.initial_value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        self.value = self.value - 1 if self.value > 0 else 0

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.initial_value