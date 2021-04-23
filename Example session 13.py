class User:
    def __init__(self):
        pass


class Register:
    def __init__(self, name: str, phone: str, pswd: str, email=None):
        self.name = self.setter_name(name)
        self.phone = self.setter_phone(phone)
        self.__pswd = self.setter_pswd(pswd)
        self.email = self.setter_email(email)
        with open('Users.txt', 'a') as f:
            f.write(f'{self.name}, {self.phone}, {self.__pswd}, {self.email}\n')

    @staticmethod
    def setter_name(n):
        return n

    @staticmethod
    def setter_phone(p):
        user_phone = p[-11:]

        if len(p) == 11:
            raise Exception(user_phone, 'user_phone')
        elif not p.isnumeric():
            raise Exception("Phone number is NOT numeric.", 'user_phone', user_phone)
        elif not p.startswith('09'):
            raise Exception("Phone number does NOT start with '09'.", 'user_phone', user_phone)

        return p

    @staticmethod
    def setter_pswd(pas):
        return pas

    @staticmethod
    def setter_email(e):
        return e


class Login:
    pass


def main():
    print('user manager')
    n = int(input('1 for Register.\n2 for Login\n'))
    while n == 1:
        name = input('name')
        phone = input('phone')
        pswd = input('password')
        email = input('email')
        try:
            user_1 = Register(name, phone, pswd, email)
            break
        except:
            continue
    print('register successfully')

    while n == 2:
        pass



user1 = Register('mohammad hosein', '0932121312', '4545as', 'mks@yahoo.com')


# main()
