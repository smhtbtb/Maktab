class A:
    def do_job(self):
        print('I am walking ...')


class Z:
    def do_job(self, n):
        print(f'I am counting from 1 to {n}:  {list(range(1, n + 1))}')


class B(A):
    def _do_job(self, s):
        super().do_job()
        print(f'I am printing your string : "{s}"')


class C(A):
    def _do_job(self):
        super().do_job()
        print('I am jumping ...')


# class C1(Z):
#     def _do_job(self, n):
#         super().do_job(n)
#         print('I am jumping ...')


class D(B):
    def _do_job(self, s):
        super()._do_job(s)
        print('I am speaking ...')


class E:
    def do_job(self, s, n):
        print(f'I am counting from 1 to {n}:  {list(range(1, n + 1))}')
        print('I am walking ...')
        print('I am jumping ...')
        print(f'I am printing your string : "{s}"')
        print('I am speaking ...')
        print('I am laughing ...')


# class E1(C):
#     def _do_job(self):
#         super()._do_job()
#         print('I am laughing ...')


class F:
    def do_job(self, s, n):
        print('I am walking ...')
        print(f'I am printing your string : "{s}"')
        print(f'I am counting from 1 to {n}:  {list(range(1, n + 1))}')
        print('I am playing ...')


# class F1(B):
#     def _do_job(self, s):
#         super()._do_job(s)
#         print('I am playing ...')


obja = A()
obja.do_job()

print()
objz = Z()
objz.do_job(3)

print()
obje = E()
obje.do_job('python', 5)

print()
objf = F()
objf.do_job('Python', 6)
