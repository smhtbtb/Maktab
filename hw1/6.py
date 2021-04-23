string = input('Calculate this please: ').split()

# for i in string:
#     if not i.isnumeric():
#         b = int(i)
#         break
#
#
# for i in string:
#     if i.isnumeric():
#         a = int(i)
#     else:
#         if i == '*':
#             print(a * b)
#         elif i == '/':
#             print(a / b)
#         elif i == '+':
#             print(a + b)
#         elif i == '-':
#             print(a - b)

list1 = []
for i in string:
    list1.append(i)

a, b = float(list1[0]), float(list1[2])
x = list1[1]

if x == '*':
    print(a * b)
elif x == '/':
    print(a / b)
elif x == '+':
    print(a + b)
elif x == '-':
    print(a - b)

