class Car:
    def __repr__(self):
        return self.__class__.__name__


class Peugeot(Car):
    def __repr__(self):
        return self.__class__.__name__


if __name__ == '__main__':
    print('Hello from models.py module')
