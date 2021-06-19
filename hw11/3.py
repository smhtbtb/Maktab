import psycopg2

conn = psycopg2.connect(database='lab', user='test', password='12345', port='5432', host='185.239.106.39')
cur = conn.cursor()

person = f"select * from lab.public.person;"
cur.execute(person)
# tt = cur.fetchall()
# n = ('id', 'role_id', 'national_date', 'birth_date', 'first_name', 'last_name', 'password', 'mobile')
# for c in range(len(n)):
#     print('|'+str(n[c]).center(22, '-'), end='')
# print()
# for i in range(len(tt)):
#     xx = tt[i]
#     for j in range(len(xx)):
#         print('|'+str(xx[j]).strip().center(22), end='')
#     print()
l11 = []
l22 = []
with open('person', 'w') as p:
    tt = cur.fetchall()
    n = ('id', 'role_id', 'national_date', 'birth_date', 'first_name', 'last_name', 'password', 'mobile')
    for c in range(len(n)):
        l1 = '|'+str(n[c]).center(22, '-')
        l11.append(''.join(list(l1)))
    for i in range(len(tt)):
        xx = tt[i]
        for j in range(len(xx)):
            l2 = '|'+str(xx[j]).strip().center(22)
            l22.append(''.join(list(l2)))
print(l11)
print(l22)




# role = f"select * from lab.public.role;"
# test = f"select * from lab.public.test;"
# test_answer = f"select * from lab.public.test_answer;"
# test_answer_list = f"select * from lab.public.test_answer_list;"
# test_price = f"select * from lab.public.test_price;"
