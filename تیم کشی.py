s = input('six nums with space= ').split()
l = []
for i in s:
    l.append(int(i))

for i in l:
    if i < 1 or i > 100:
        print('error')
        break

    else:
        print(min(l[0], l[1]) + min(l[2], l[3]) + min(l[4], l[5]))
        break

