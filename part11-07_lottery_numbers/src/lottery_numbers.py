class LotteryNumbers:
    def __init__(self, week: int, numbers: list):
        self.__week = week
        self.__numbers = numbers

    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.__numbers])

    def hits_in_place(self, numbers: list):
        return [number if number in self.__numbers else -1 for number in numbers]