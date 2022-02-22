class ListHelper:
    def __init__(self, my_list: list):
        self.__list = my_list

    @classmethod
    def greatest_frequency(cls, my_list: list):
        greatest_count = 1
        greatest_element = my_list[0]
        for element in my_list:
            if my_list.count(element) > greatest_count:
                greatest_count = my_list.count(element)
                greatest_element = element
        return greatest_element

    @classmethod
    def doubles(cls, my_list: list):
        my_set = set(my_list)
        count_double = 0
        for element in my_set:
            if my_list.count(element) >= 2:
                count_double += 1
        return count_double

"""
Model
    @classmethod
    def greatest_frequency(cls, my_list: list):
        # If there is no items at all, then there is no frequency
        if not my_list:
            return None

        max_frequency = 0
        max_item = None
        for item in my_list:
            frequency = my_list.count(item)
            if not max_item or frequency > max_frequency:
                max_frequency = frequency
                max_item = item
        return max_item

    @classmethod
    def doubles(cls, my_list: list):
        counts = {}
        for item in my_list:
            counts[item] = my_list.count(item)
        doubles = 0
        for value in counts.values():
            if value > 1:
                doubles += 1
        return doubles
"""