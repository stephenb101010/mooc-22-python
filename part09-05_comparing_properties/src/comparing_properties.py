class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compared_to:'RealProperty'):
        return self.square_metres > compared_to.square_metres

    def get_total_price(self):
        return self.square_metres*self.price_per_sqm

    def price_difference(self, compared_to:'RealProperty'):
        return abs(self.get_total_price() - compared_to.get_total_price())

    def more_expensive(self, compared_to:'RealProperty'):
        return self.get_total_price() > compared_to.get_total_price()