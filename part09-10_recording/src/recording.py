class Recording:
    def __init__(self, length: int):
        if length < 0:
            raise ValueError('Length of recording cannot be below 0.')
        self.__length = length

    # A getter method
    @property
    def length(self):
        return self.__length

    # A setter method
    @length.setter
    def length(self, length: int):
        if length < 0:
            raise ValueError('Length of recording cannot be below 0.')
        self.__length = length