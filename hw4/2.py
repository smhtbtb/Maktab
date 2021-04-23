from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def rasm(self):
        pass

    @abstractmethod
    def mohit(self):
        pass

    @abstractmethod
    def masahat(self):
        pass

    @staticmethod
    def concat_area(n: list):
        res = 0
        for i in n:
            res += (i[0]) * (i[1])
        return res

    @staticmethod
    def draw_concat(m):
        for j in range(1, max(m) + 1):
            for i in m:
                if i >= j:
                    print(i * "*", end="")

                else:
                    print(i * " ", end="")
            print()


n = [(2, 3), (4, 8)]
print(Shape.concat_area(n))

m = [2, 5]
Shape.draw_concat(m)
