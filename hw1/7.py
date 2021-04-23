sentence = input('Write the string: ').lower()

for i in sentence:
    x = 0
    for j in sentence:

        if i == j:
            x += 1

    if x > 0:
        print(i, ':', x)
        sentence = sentence.replace(i, '')


