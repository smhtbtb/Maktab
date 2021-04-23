sange_pa = input('please input with space: ').split()
list1 = list(map(int, sange_pa))


def is_primal(n):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False


def primals(n):
    listprimals = []
    for n in range(2, int(n)):
        if is_primal(n):
            listprimals.append(int(n))

    return listprimals


def prime_maqsoomalayh_list(n):
    maqsoomalayh_list = []
    for i in range(2, int(n)):
        if is_primal(i):
            if n % i == 0:
                maqsoomalayh_list.append(i)

    return maqsoomalayh_list


def gheymate_kol(_):
    list_gheymat_kol = []
    if list1[0] == len(list1) - 1:
        del list1[0]
        for i in list1:
            if is_primal(i):
                list_gheymat_kol.append(int(len(primals(i))))
            else:
                list_gheymat_kol.append(int(len(prime_maqsoomalayh_list(i))))

        summation = sum(list_gheymat_kol)
        if is_primal(summation):
            summation -= len(primals(summation))
        else:
            summation -= len(prime_maqsoomalayh_list(summation))

        return summation
    else:
        return False


print(gheymate_kol(sange_pa))
