l2 = [-1, -1, 2, 5, 4]
l1 = [-1, 7, 9, 2, 1]
l3 = [0, 0, 0, 0, 0]

s = input('* or / or + or -: ')

if s == '+':
    for i in range(4, 0, -1):
        if l1[i] == -1:
            l1[i] = 0
        if l2[i] == -1:
            l2[i] = 0
        k = l1[i] + l2[i]
        if k < 10:
            l3[i] += k
        else:
            l3[i] += k - 10
            l3[i - 1] += 1
    print(l3)

if s == '-':
    for j in range(5):
        if l2[j] <= l1[j]:
            pass
        else:
            l1, l2 = l2, l1
            print('your num is negative')
            break
    for i in range(4, 0, -1):
        if l1[i] == -1:
            l1[i] = 0
        if l2[i] == -1:
            l2[i] = 0
        k = l1[i] - l2[i]
        if k >= 0:
            l3[i] += k
        else:
            l3[i] += l1[i] + 10 - l2[i]
            l1[i - 1] -= 1
    print(l3)



