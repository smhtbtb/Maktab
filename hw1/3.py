marks = input('give me students\' marks with space between them: ')


Maximum = 0
for i in marks.split():
    if float(i) > Maximum:
        Maximum = float(i)

print('Maximum= ', Maximum)


Minimum = 20
for i in marks.split():
    if float(i) < Minimum:
        Minimum = float(i)

print('Minimum= ', Minimum)


Sum = 0
for i in marks.split():
    Sum += float(i)

Average = Sum / len(marks.split())
print('Average= ', '{:.2f}'.format(Average))




