# import psycopg2
#
# conn = psycopg2.connect(database='lab', user='test', password='12345', port='5432', host='185.239.106.39')
# cur = conn.cursor()
#
# person = f"select * from lab.public.person;"
# # TODO: first way
# cur.execute(person)
# person_file = open('person', 'w')
# p0 = cur.fetchall()
# p1 = ('id', 'role_id', 'national_date', 'birth_date', 'first_name', 'last_name', 'password', 'mobile')
# for p2 in range(len(p1)):
#     print('|' + str(p1[p2]).center(22, '-'), end='', file=person_file)
# print(file=person_file)
# for p3 in range(len(p0)):
#     p4 = p0[p3]
#     for p5 in range(len(p4)):
#         print('|' + str(p4[p5]).strip().center(22), end='', file=person_file)
#     print(file=person_file)
# person_file.close()
# #
# #
# #
# # TODO: second way
# # l11 = []
# # l22 = []
# # p = open('person', 'w')
# # tt = cur.fetchall()
# # n = ('id', 'role_id', 'national_date', 'birth_date', 'first_name', 'last_name', 'password', 'mobile')
# # for c in range(len(n)):
# #     l1 = '|'+str(n[c]).center(22, '-')
# #     l11.append(''.join(list(l1)))
# # for i in range(len(tt)):
# #     xx = tt[i]
# #     for j in range(len(xx)):
# #         l2 = '|'+str(xx[j]).strip().center(22)
# #         l22.append(''.join(list(l2)))
# # print(''.join(l11), file=p)
# # for x in range(0, len(l22), 8):
# #     print(f'{l22[x]}{l22[x+1]}{l22[x+2]}{l22[x+3]}{l22[x+4]}{l22[x+5]}{l22[x+6]}{l22[x+7]}', file=p)
# # **********************************************************************************
#
# role = f"select * from lab.public.role;"
# cur.execute(role)
# role_file = open('role', 'w')
# r0 = cur.fetchall()
# r1 = ('id', 'name')
# for r2 in range(len(r1)):
#     print('|' + str(r1[r2]).center(22, '-'), end='', file=role_file)
# print(file=role_file)
# for r3 in range(len(r0)):
#     r4 = r0[r3]
#     for r5 in range(len(r4)):
#         print('|' + str(r4[r5]).strip().center(22), end='', file=role_file)
#     print(file=role_file)
# role_file.close()
# # **********************************************************************************
#
# test = f"select * from lab.public.test;"
# cur.execute(test)
# test_file = open('test', 'w')
# t0 = cur.fetchall()
# t1 = ('id', 'name', 'description', 'parent_id')
# for t2 in range(len(t1)):
#     print('|' + str(t1[t2]).center(22, '-'), end='', file=test_file)
# print(file=test_file)
# for t3 in range(len(t0)):
#     t4 = t0[t3]
#     for t5 in range(len(t4)):
#         print('|' + str(t4[t5]).strip().center(22), end='', file=test_file)
#     print(file=test_file)
# test_file.close()
# # **********************************************************************************
#
# test_answer = f"select * from lab.public.test_answer;"
# cur.execute(test_answer)
# test_answer_file = open('test_answer', 'w')
# ta0 = cur.fetchall()
# ta1 = ('id', 'person_id', 'request_date', 'answer_date')
# for ta2 in range(len(ta1)):
#     print('|' + str(ta1[ta2]).center(22, '-'), end='', file=test_answer_file)
# print(file=test_answer_file)
# for ta3 in range(len(ta0)):
#     ta4 = ta0[ta3]
#     for ta5 in range(len(ta4)):
#         print('|' + str(ta4[ta5]).strip().center(22), end='', file=test_answer_file)
#     print(file=test_answer_file)
# test_answer_file.close()
# # **********************************************************************************
#
# test_answer_list = f"select * from lab.public.test_answer_list;"
# cur.execute(test_answer_list)
# test_answer_list_file = open('test_answer_list', 'w')
# tal0 = cur.fetchall()
# tal1 = ('id', 'test_id', 'price', 'answer', 'test_answer_id')
# for tal2 in range(len(tal1)):
#     print('|' + str(tal1[tal2]).center(22, '-'), end='', file=test_answer_list_file)
# print(file=test_answer_list_file)
# for tal3 in range(len(tal0)):
#     tal4 = tal0[tal3]
#     for tal5 in range(len(tal4)):
#         print('|' + str(tal4[tal5]).strip().center(22), end='', file=test_answer_list_file)
#     print(file=test_answer_list_file)
# test_answer_list_file.close()
# # **********************************************************************************
#
# test_price = f"select * from lab.public.test_price;"
# cur.execute(test_price)
# test_price_file = open('test_price', 'w')
# tp0 = cur.fetchall()
# tp1 = ('id', 'test_id', 'price', 'start_date', 'end_date')
# for tp2 in range(len(tp1)):
#     print('|' + str(tp1[tp2]).center(22, '-'), end='', file=test_price_file)
# print(file=test_price_file)
# for tp3 in range(len(tp0)):
#     tp4 = tp0[tp3]
#     for tp5 in range(len(tp4)):
#         print('|' + str(tp4[tp5]).strip().center(22), end='', file=test_price_file)
#     print(file=test_price_file)
# test_price_file.close()
#
#
#
#
#
#
import psycopg2


def copy_table():
    conn = psycopg2.connect('host=localhost dbname=lab user=postgres password=1234567890 port=5432')
    cur = conn.cursor()

    conn2 = psycopg2.connect(database='lab', user='test', password='12345', port='5432', host='185.239.106.39')
    cur2 = conn2.cursor()

    l22 = []
    exe2 = f"select * from test_price"
    cur2.execute(exe2)
    print(len(cur2.fetchall()))
    for i in range(len(cur2.fetchall())):
        xx = cur2.fetchall()[i]
        for j in range(len(xx)):
            l2 = xx[j]
            l22.append(l2)
    for x in range(0, len(l22), 5):
        exe = f"insert into test_price values ({l22[x]},{l22[x + 1]},{l22[x + 2]},{l22[x + 3]},{l22[x + 4]})"
        cur.execute(exe)

        print(cur.fetchall())
    return 0


copy_table()
