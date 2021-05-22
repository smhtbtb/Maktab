def hsg(n):
    print(n)
    while n > 1:
        # print(n)
        if n % 2 == 0:
            # print(n)
            n = n/2
            yield int(n)

        else:
            n = 3 * n + 1
            # print(n)
            yield int(n)


for i in hsg(3):
    print(i)


# def is_primal(n: int):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# def primals_gen(n: int):
#     for i in range(2, n + 1):
#         if is_primal(i):
#             yield i
#
#
# for i in primals_gen(100000):
#     print(i, end=', ')
