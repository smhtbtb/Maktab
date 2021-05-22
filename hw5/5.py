import pickle

import dill


class User:
    def __init__(self, id, first_name, last_name, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def __repr__(self):
        return f"{self.id}: {self.first_name} {self.last_name} <{self.phone}>"


def from_file(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)


####################################################################################
dictionary = {}

txt1 = from_file('users.pickled')
# print(txt)
lst = []
for i in range(len(txt1)):
    # print(str(txt[i]))
    for j in str(txt1[i]).split(': '):
        # print(j)
        if j.isnumeric():
            k = int(j)
            lst.append(k)
        else:
            v = str(j)

            dictionary[k] = v

# print(sorted(lst))
# print(dictionary)
lst_res1 = []
for i in sorted(lst):
    res = f'{i}: {dictionary[i]}'
    lst_res1.append(res)
# pickled = pickle.dumps(lst_res)

with open('output-q-5-1.txt', 'wb') as f:
    pickle.dump(lst_res1, f)

###################################################################################
txt2 = from_file('users.pickled')
lst_res2 = []
for i in range(len(txt1)):
    s = str(txt2[i])
    # print(s)
    if '919' in s:
        lst_res2.append(str(s))

with open('output-q-5-2.txt', 'wb') as g:
    pickle.dump(lst_res2, g)

###################################################################################
txt3 = from_file('users.pickled')
lst_res3 = []
dictionary1 = {}
for i in range(len(txt3)):
    s = str(txt3[i])
    # print(s)
    for l in str(txt1[i]).split(': '):
        # print(l)
        if not l.isnumeric():
            k1 = str(l)
            lst_res3.append(' '.join(k1.split()[0:2]))

# print(lst_res3)
with open('output-q-5-3.txt', 'wb') as o:
    asd = dill.dump(lst_res3, o)

with open('output-q-5-3.txt', 'rb') as v:
    print(dill.load('output-q-5-3.txt'))
