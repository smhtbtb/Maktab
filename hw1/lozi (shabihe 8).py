n = int(input('give me a num: '))

if n == 1:
    print('*')

elif n > 1:
    for i in range(n + 1):
        print(' ' * (n - i), '*' * ((2 * i) - 1))
    for j in range(n - 1, 0, -1):
        print(' ' * (n - j), '*' * ((2 * j) - 1))
