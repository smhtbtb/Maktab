r = int(input('r= '))
c = int(input('c= '))

if r < 1 or r > 10 or c < 1 or c > 20:
    print('invalid numbers')

if c < 11:
    print('Right', 11 - r, c)
else:
    print('Left', 11 - r, 21 - c)








