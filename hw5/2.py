import re

with open('input-q-2.txt') as f:
    f = f.read().split('.[')
    txt1 = ''
    for i in range(len(f)):
        if i == 0:
            txt1 += (f[i] + '.\n')
        elif 0 < i < len(f) - 1:
            txt1 += ('[' + f[i] + '.\n')
        else:
            txt1 += ('[' + f[i] + '].')

with open('output-q-2-1.txt', 'a+') as res:
    res.write(txt1)

################################################################

with open('input-q-2.txt') as f:
    f = f.read().replace('[', ' ')
    f = f.replace(']', ' ')
    f = f.replace('.', ' ')
    f = f.replace(',', ' ')
    f = f.replace('(', ' ')
    f = f.replace(')', ' ')
    f = f.replace(']', ' ')
    f = f.replace('-', ' ')
    f = f.replace('\'', ' ')

txt2 = set(f.split())
num_list = []
words_list = []
num_count = 0
words_count = 0
for i in txt2:
    if i.isnumeric():
        num_list.append(i)
        num_count += 1
    elif i.isalpha():
        words_list.append(i)
        words_count += 1
# print(num_list)
# print(num_count)

with open('output-q-2-2.txt', 'a+') as res2:
    res2.write(str(words_list) + '\n')
    res2.write(str(words_count) + '\n')
    res2.write(str(num_list) + '\n')
    res2.write(str(num_count))

###############################################################################

with open('input-q-2.txt') as f:
    f = f.read().replace('[', ' ')
    f = f.replace(']', ' ')
    f = f.replace('.', ' ')
    f = f.replace(',', ' ')
    f = f.replace('(', ' ')
    f = f.replace(')', ' ')
    f = f.replace(']', ' ')
    f = f.replace('-', ' ')
    f = f.replace('\'', ' ')

txt3 = f.strip().split()
i = 0
r = re.findall('([A-Z][a-z]+)', str(txt3))
for i in txt3:
    if i.isupper():
        r.append(i)
print(str(r))

with open('output-q-2-3.txt', 'a+') as res3:
    res3.write(str(r))
