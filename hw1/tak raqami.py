n = input()


def sum1(num):
    l = map(int, [i for i in num])
    return sum(l)


def last_sum(num):
    while sum1(num) > 9:
        l = map(int, [i for i in str(sum1(num))])
        return sum(l)


print(last_sum(n))

