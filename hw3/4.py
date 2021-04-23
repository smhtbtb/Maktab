class Bank:

    def __init__(self, name: str, money: int):
        self.name = name
        self.money = money
        self.you_can_spend = self.money - 10

    def vaariz(self, v):
        self.money += v
        return f'You, {self.name}, have {self.money} Rials'

    def bardasht(self, b):
        if self.__mojaaz(b, self.you_can_spend):
            return f'shoma ta saqfe *{self.you_can_spend} Rls* tavaanaaei e bardasht darid'
        else:
            return self.money - b

    def enteqal(self, to_name: str, how_much: int):
        if self.__mojaaz(how_much, self.you_can_spend):
            return f'shoma ta saqfe *{self.you_can_spend} Rls* tavaanaaei e bardasht darid'
        else:
            return f'Your friend, {to_name}, has +{how_much} Rials'

    def __mojaaz(self, bardasht, you_can_spend):
        if bardasht > self.you_can_spend:
            return f'shoma ta saqfe *{self.you_can_spend} Rls* tavaanaaei e bardasht darid'


p = Bank('ali rahmani', 52)
print(p.enteqal('jaavid', 25))
