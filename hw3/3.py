class Library:
    all_count = 0

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        self.how_many_books(self.count)

    @classmethod
    def how_many_books(cls, self):
        cls.all_count += n

    def __repr__(self):
        return '\self'.join([f"name: {self.name}, price: {self.price}, count of this book: {self.count}, count of all {self.all_count}\self"])


b = Library('a', 87, 9)
c = Library('b', 45, 12)
print(c, b)
