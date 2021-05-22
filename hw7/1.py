import num2words


def remainder(n: int):
    def inner1(func):
        def inner2(*args, **kwargs):
            x = func(*args, **kwargs)
            y = x % n
            return y

        return inner2

    return inner1


def string_p(func):
    def inner(*args, **kwargs):
        a = func(*args, **kwargs)
        return num2words.num2words(a)

    return inner


# @string_p
# @remainder(n=3)
class Multiple:

    # class string:
    #     @classmethod
    #     def string_p(cls, func):
    #         def inner(*args):
    #             a = func(*args)
    #             return a
    #
    #         return inner
    #

    def __init__(self, m, n):
        self.m = int(m)
        self.n = int(n)

    def multipling(self) -> int:
        if not self.is_primal(self.m) or not self.is_primal(self.n):
            raise Exception('give me primal number')
        elif self.is_primal(self.m) and self.is_primal(self.n):
            res = int(self.m * self.n)
            return res

    # @string.string_p
    @string_p
    def multipling_string_p(self) -> int:
        if not self.is_primal(self.m) or not self.is_primal(self.n):
            raise Exception('give me primal number')
        elif self.is_primal(self.m) and self.is_primal(self.n):
            res = int(self.m * self.n)
            return res

    @remainder(4)
    def multipling_remainder(self) -> int:
        if not self.is_primal(self.m) or not self.is_primal(self.n):
            raise Exception('give me primal number')
        elif self.is_primal(self.m) and self.is_primal(self.n):
            res = int(self.m * self.n)
            return res

    # def __call__(self, *args, **kwargs):
    #     return self.multipling

    # def __repr__(self):
    #     return self

    @staticmethod
    def is_primal(n: int):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


b = Multiple(3, 5)
print(b.multipling())
print(b.multipling_string_p())
print(b.multipling_remainder())
