n1, n2 = input('2 int nums with space between them= ').split()


def gcd(x, y):
    gcd = 0
    if int(x) > int(y):
        for i in range(1, int(y) + 1):
            if int(x) % i == 0 and int(y) % i == 0:
                gcd = i
    else:
        for i in range(1, int(x) + 1):
            if int(x) % i == 0 and int(y) % i == 0:
                gcd = i

    return gcd


def lcm(x, y):
    return int(int(x) * int(y) / gcd(x, y))


print(gcd(n1, n2))
print(lcm(n1, n2))
