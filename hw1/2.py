sentence = input('Write your sentence: ')

vowels = 0
for i in sentence.lower():
    if i == 'a' or i == 'i' or i == 'o' or i == 'e' or i == 'u':
        vowels += 1
print('vowels= ', vowels)


Digits = 0
for i in sentence.lower():
    if i.isdigit():
        Digits += 1

print('Digits= ', Digits)


sum_of_digits = 0
for i in sentence.lower():
    if i.isdigit():
        sum_of_digits += int(i)

print('sum of digits= ', sum_of_digits)


for i in sentence.lower():
    x = 0
    for j in sentence.lower():

        if i == j:
            x += 1

    if x > 1:
        print('\'', i, '\':', x, end = ' ,')
        sentence = sentence.replace(i, '')
