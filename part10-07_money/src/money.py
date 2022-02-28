class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __money_total(self):
        return self.__euros + (self.__cents/100)
    
    def __eq__(self, another: "Money"):
        return self.__money_total() == another.__money_total()

    def __lt__(self, another: "Money"):
        return self.__money_total() < another.__money_total()

    def __gt__(self, another: "Money"):
        return self.__money_total() > another.__money_total()

    def __ne__(self, another: "Money"):
        return self.__money_total() != another.__money_total()

    def __add__(self, another: "Money"):
        total_euros = self.__euros + another.__euros
        total_cents = self.__cents + another.__cents
        if total_cents >= 100:
            total_euros += 1
        total_cents = total_cents % 100
        newTotal = Money(total_euros, total_cents)
        return newTotal

    def __sub__(self, another: "Money"):
        if (self.__money_total() < another.__money_total()):
            raise ValueError("a negative result is not allowed")
        total_euros = self.__euros - another.__euros
        if self.__cents >= another.__cents:
            total_cents = self.__cents - another.__cents
        else:
            total_euros -= 1
            total_cents = self.__cents + (100-another.__cents)
        newTotal = Money(total_euros, total_cents)
        return newTotal

"""
    # Another helper method which converts cents to value
    def __set_value(self, cents: int):
        self.__euros = cents // 100
        self.__cents = cents - self.__euros * 100

    def __add__(self, other: "Money"):
        msum = Money(0,0)
        msum.__set_value(self.__value() + other.__value())
        return msum

    def __sub__(self, other: "Money"):
        difference = self.__value() - other.__value()
        if difference < 0:
            raise ValueError("a negative result is not allowed")
        dmoney = Money(0,0)
        dmoney.__set_value(self.__value() - other.__value())
        return dmoney
"""