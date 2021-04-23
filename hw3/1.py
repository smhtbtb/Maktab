class Triangle:

    def __init__(self, A: tuple, B: tuple, C: tuple):
        self.xa = int(A[0])
        self.ya = int(A[1])
        self.xb = int(B[0])
        self.yb = int(B[1])
        self.xc = int(C[0])
        self.yc = int(C[1])

    def area(self): return 0.5 * abs(
        self.xa * (self.yb - self.yc) + self.xb * (self.yc - self.ya) + self.xc * (self.ya - self.yb)
    )

    def sides(self):
        xa = self.xa
        ya = self.ya
        xb = self.xb
        yb = self.yb
        xc = self.xc
        yc = self.yc
        a = ((xb - xc)**2 + (yb - yc)**2)**0.5
        b = ((xa - xc)**2 + (ya - yc)**2)**0.5
        c = ((xb - xa)**2 + (yb - ya)**2)**0.5
        return f'a= {a}, b= {b}, c= {c}'

    def perimeter(self):
        xa = self.xa
        ya = self.ya
        xb = self.xb
        yb = self.yb
        xc = self.xc
        yc = self.yc
        a = ((xb - xc) ** 2 + (yb - yc) ** 2) ** 0.5
        b = ((xa - xc) ** 2 + (ya - yc) ** 2) ** 0.5
        c = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
        return f'perimeter= {a + b + c}'

    def center(self):
        xa = self.xa
        ya = self.ya
        xb = self.xb
        yb = self.yb
        xc = self.xc
        yc = self.yc
        ox = (xa + xb + xc) / 3
        oy = (ya + yb + yc) / 3
        return f'ox= {ox} and oy= {oy}'

    def type(self):
        xa = self.xa
        ya = self.ya
        xb = self.xb
        yb = self.yb
        xc = self.xc
        yc = self.yc
        a = ((xb - xc) ** 2 + (yb - yc) ** 2) ** 0.5
        b = ((xa - xc) ** 2 + (ya - yc) ** 2) ** 0.5
        c = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5

        if a == b and a == c:
            return f'equilateral triangle'

        elif (a == b and a != c) or (a == c and a != b) or (c == b and c != a):
            return f'isosceles triangle'

        elif (a ** 2) == (b**2 + c**2) or (b**2) == (a**2 + c**2) or (c**2) == (a**2 + b**2):
            return f'right triangle'


s = Triangle((0, 0), (2, 2), (3, 0))
print(s.center())
