def sum_1toN(num: int):
    sum1 = 0
    for i in range(1, num + 1):
        sum1 = sum1 + i
    return sum1


def sum_1toN_list(num):
    list_goodnumbers = []
    for i in range(1, num + 1):
        list_goodnumbers.append(sum_1toN(i))

    return list_goodnumbers


# def is_primal(n):
#     if n > 1:
#         for i in range(2, int(n / 2) + 1):
#             if (n % i) == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False


def maqsoomalayh_list(n):
    maqsoomalayh_list1 = []
    for i in range(1, int(n) + 1):
        if n % i == 0:
            maqsoomalayh_list1.append(i)

    return maqsoomalayh_list1


def first_good_num(num):
    for i in sum_1toN_list(num*num):
        # print(i)
        if k == len(maqsoomalayh_list(i)):
            # print(maqsoomalayh_list(i))
            return maqsoomalayh_list(i)[-1]


k = int(input('k= '))
print(first_good_num(k))
