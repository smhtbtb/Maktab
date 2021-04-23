n = int(input())


def fibo(num: int):
    l = [1, 1]

    if num == 1:
        return [1]

    else:
        while len(l) != n:
            l.append(l[-1] + l[-2])
        return l


print(fibo(n))
