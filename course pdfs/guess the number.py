n = input('num= ')
a = 0
b = 10000
i = 1

guess = (a + b) // 2
print(f'{guess} < {n}?')
x = input('yes or no: ')

while i < 21:
    if b - a > 5:

        if x == 'yes':
            a = guess
            guess = (a + b) // 2
            print(f'{guess} < {n}?')
            x = input('yes or no: ')
            i += 1

        elif x == 'no':
            b = guess
            guess = (a + b) // 2
            print(f'{guess} < {n}?')
            x = input('yes or no: ')
            i += 1

    else:
        for _ in range(5):
            print(f'{guess} = {n}?')
            x = input('yes or no: ')
            _ += 1
            if x == 'yes':
                print('eyval', i + _)
                i = 30
                _ = 30
                break
            else:
                guess = a + 1
