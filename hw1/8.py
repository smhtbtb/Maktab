n = int(input('give me a num: '))

if n == 1:
    print('*')

elif n > 1:
    for i in range(n + 1):
        print('*' * i)
    for j in range(n - 1, 0, -1):
        print('*' * j)
