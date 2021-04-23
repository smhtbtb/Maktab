class answer:

    def __int__(self, k):
        self.k = k

    def sum_1toN(self: int):
        sum1 = 0
        for i in range(1, self + 1):
            sum1 = sum1 + i
        return sum1

    def sum_1toN_list(self: int):
        list_goodnumbers = []
        for i in range(1, int(self) + 1):
            list_goodnumbers.append(self.sum_1toN(i))

        return list_goodnumbers

    def maqsoomalayh_list(self: int):
        maqsoomalayh_list1 = []
        for i in range(1, int(self) + 1):
            if self % i == 0:
                maqsoomalayh_list1.append(i)

        return maqsoomalayh_list1

    def first_good_num(self: int):
        for i in self.sum_1toN_list(self * self):
            print(i)
            if k == len(self.maqsoomalayh_list(i)):
                print(self.maqsoomalayh_list(i))
                return self.maqsoomalayh_list(i)[-1]


k = int(input('k= '))
print(k)
