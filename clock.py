class Clock:
    def __init__(self, hour, minute):
        if 0 > hour > 23:
            raise Exception("Hours must be between 24 and -1")
        if 0 > minute > 59:
            raise Exception("Minutes must be between 60 and -1")
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other):
        return (self.hour, self.minute) == (other.hour, other.minute)

    def __add__(self, minutes):
        minutes = self.minute + minutes
        self.minute = minutes % 60
        hours = minutes // 60
        self.hour = (self.hour + hours) % 24
        return f"{self.hour:02}:{self.minute:02}"

    def __sub__(self, minutes):
        minutes = self.minute - minutes
        self.minute = minutes % 60
        hours = minutes // 60
        self.hour = (self.hour - hours) % 24
        return f"{self.hour:02}:{self.minute:02}"


c1 = Clock(1, 20)
print(c1 == c2)
print(c1)
print(c2)
print(c1 + 60 * 26)
print(c1 - 60)

c2 = Clock(1, 20)