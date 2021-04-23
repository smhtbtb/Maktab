from time import time, ctime
from datetime import datetime
import datetime


class BirthDay:

    def __init__(self, h: int, d: int, m: int, y: int):
        self.h = h
        self.d = d
        self.m = m
        self.y = y
        self.birthday = datetime.datetime(y, m, d, h)

    def age_in_year(self):
        from datetime import datetime

        dt = datetime.today()
        difference = dt.timestamp() - self.birthday.timestamp()
        years = difference / 60 / 60 / 24 / 365.25
        return f'years: {years:.04}'

    def age_in_hour(self):
        from datetime import datetime

        dt = datetime.today()
        difference = dt.timestamp() - self.birthday.timestamp()
        hours = difference / 60 / 60
        return f'hours: {hours:.10}'

    def how_long_to_birthday(self):
        from datetime import datetime

        dt = datetime.today()
        difference = abs(self.birthday.timestamp() - dt.timestamp())
        to_birthday = (difference % 3.154e+7) / 60 / 60 / 24
        return f'to birthday in days: {to_birthday:.04}'


t = BirthDay(16, 6, 3, 1999)
print(t.age_in_year())
print(t.age_in_hour())
print(t.how_long_to_birthday())
