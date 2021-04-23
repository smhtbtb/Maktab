class Clock:
    def __init__(self, hour, minute):
        if hour > 23 or hour < 0 or minute > 59 or minute < 0:
            raise Exception('invalid value')
        else:
            self.hour = hour
            self.minute = minute

    def __repr__(self):
        return f'{self.hour}:{self.minute}'

    def __eq__(self, other: int):
        return (self.hour, self.minute) == (other.hour, other.minute)

    def __add__(self, minutes):
        if minutes + self.minute > 59:
            self.hour += (minutes + self.minute) // 60
            self.minute = (minutes + self.minute) % 60
            if self.hour > 23:
                self.hour -= 24
        else:
            self.minute += minutes

        return f'{self.hour}:{self.minute}'

    def __sub__(self, minutes):
        if self.minute - minutes < 0:
            if minutes < 61:
                self.minute = abs(self.minute - minutes) % 60
                self.hour -= (abs((self.minute - minutes) // 60)) % 24
                if self.hour < 0:
                    self.hour += 23
            else:
                self.minute = abs(self.minute - (minutes % 60)) % 60
                self.hour -= (abs((self.minute - minutes) // 60)) % 24
                if self.hour < 0:
                    self.hour += 23

        else:
            self.minute -= minutes

        return f'{self.hour}:{self.minute}'


c1 = Clock(12, 30)
print(c1 - 180)
