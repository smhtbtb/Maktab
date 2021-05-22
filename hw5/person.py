import logging

logging.basicConfig(level=logging.DEBUG)
# logging.FileHandler('person.log', mode='a', encoding=None, delay=False)


class Person:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        logging.warning("Person created! {} {}".format(self.name, self.family))

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
        else:
            logging.critical("Invalid age!")
        self._age = 0

    logger = logging.getLogger('person.py')
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler("person.log")
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s-%(name)-10s-%(levelname)-16s-%(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)

