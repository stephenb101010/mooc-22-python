class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    def __lt__(self, another: "SimpleDate"):
        if self.__year < another.__year:
            return True
        elif self.__year == another.__year:
            if self.__month < another.__month:
                return True
            elif self.__month == another.__month:
                if self.__day < another.__day:
                    return True

        return False

    def __gt__(self, another: "SimpleDate"):
        if self.__eq__(another) == False and self.__lt__(another) == False:
            return True
        return False

    def __eq__(self, another: "SimpleDate"):
        if self.__day == another.__day and \
            self.__month == another.__month and \
                self.__year == another.__year:
                return True
        return False

    def __ne__(self, another: "SimpleDate"):
        if self.__eq__(another) == False:
            return True
        return False

    def __convert_curr_date_to_days(self):
        return ((self.__year-1)*12*30) + ((self.__month-1)*30) + self.__day

    def __add__(self, days_to_add: int):
        days = self.__convert_curr_date_to_days()
        days += days_to_add
        year = (days//360)+1
        month = ((days//30)%12)+1
        day = days%30
        return SimpleDate(day, month, year)

    def __sub__(self, another: "SimpleDate"):
        curr_days = self.__convert_curr_date_to_days()
        another_days = another.__convert_curr_date_to_days()
        return abs(curr_days - another_days)

"""
class SimpleDate:
    def __init__(self, pv: int, month: int, year: int):
        self.__pv = pv
        self.__month = month
        self.__year = year

    def __str__(self):
        return f'{self.__pv}.{self.__month}.{self.__year}'

    # Comparisons are easier, when date is converted to days
    def __value(self):
        return self.__year * 360 + self.__month * 30 + self.__pv

    # Converts days back to date
    def __to_date(self, days: int):
        months = days // 30
        years = months // 12
        days -= months * 30
        months -= years * 12
        return SimpleDate(days, months, years)

    def __lt__(self, other: "SimpleDate"):
        return self.__value() < other.__value()

    def __gt__(self, other: "SimpleDate"):
        return self.__value() > other.__value()

    def __eq__(self, other: "SimpleDate"):
        return self.__value() == other.__value()
      
    def __ne__(self, other: "SimpleDate"):
        return self.__value() != other.__value()
 
    def __add__(self, days_to_add: int):
        return self.__to_date(self.__value() + days_to_add)

    def __sub__(self, other: "SimpleDate"):
        # abs(x) returns the absolute value of x
        return abs(self.__value() - other.__value())
"""