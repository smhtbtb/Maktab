# a = int(input('seconds: '))
# h = a//(60*60)
# m = (a//60) % 60
# s = a % 60
#
# print(f'{h}:{m}:{s}')


#
# errno = 50159747054
# name = 'Bob'
#
# print('Hello, %s' % name)
#
# print('%x' % errno)
#
# print('Hey %s, there is a 0x%x error!' % (name, errno))
#


# txt = "banana"
#
# x = txt.rjust(15)
#
# print(x, "is my favorite fruit.")


# n = int(input('num= '))
#
# for i in range(2, n):
#     if n % i == 0:
#         print(f'{n} is not primal')
#         break
#     else:
#         print(f'{n} is primal')
#         break


# def my_func(arg1, arg2, arg3):
#     print('> Start of function')
#     print(arg1, arg2, arg3)
#     return arg1, arg2, arg3
#     print('> End of function')
#
# res = my_func('Akbar', 111, False)
# print(res, res[0], res[1], res[2])
# print(type(res))

#
# def primal(n):
#     for i in range(1, n+1):
#         for j in range(2, i):
#             if i % j == 0:
#                 return False
#
#             else:
#                 print(i)
#
#
#
# print(primal(16))


#
# string = 'geeks for geeks'
#
# # returns index value
# result = string.find('for')
# print("Substring for:", result)
#
# result = string.find('best')
# print("Substring best:", result)


# n = input('num= ')
#
# l = [i for i in n]
# l1 = map(int, l)
#
# a = sum(l1)
#
# while a > 10:
#     a = str(a)
#     l = [i for i in a]
#     l1 = map(int, l)
#     a = sum(a)
#
# print(a)


# print("The octal representation of 23 is " + oct(23))

# print("The octal representation of the"
#       " ascii value of 'z' is " + oct(ord('z')))
#
# print("The octal representation of the binary"
#       " of 23 is " + oct(0b10111))
#
# print("The octal representation of the binary"
#       " of 23 is " + oct(0x17))

# print(int(0x17))


# d = {
#     'akbar' : 'sara',
#     12 : 21
# }
#
#
# print(d.get('mashti'), 12365)


# s = "Hello akbar11, date: 1399/12/10, time: 12:05:2"
# d = {}
# for _ in s:
#     d[_] = d.get(_, 0) + 1
# # Dict Comprehension
# print({key: value for key, value in d.items() if value > 1})


# class Triangle:
#
#     def __init__(self, xa, ya, xb, yb, xc, yc):
#         self.xa = xa
#         self.ya = ya
#         self.xb = xb
#         self.yb = yb
#         self.xc = xc
#         self.yc = yc
#
#     def area(self): return 0.5 * abs(
#         self.xa * (self.yb - self.yc) + self.xb * (self.yc - self.ya) + self.xc * (self.ya - self.yb))
#
#
# s = Triangle(0, 0, 2, 2, 3, 0)
# print(s.area())

# n = 10
# for i in range(1, n+1):
# print(*[i*j for j in range(1, n+1)], sep='\t')


# class User:
#     def __init__(self, *args): self._father_name = 'akbar'
#
#
# class Student(User):
#     def some_method(self):
#         print(f'{self._father_name=}')
#
#
# u = User()
# s = Student()
# s.some_method()
# print(u._father_name)  # ???print(s._father_name)  # ???


# class MyParentClass:
#     def __init__(self, name):
#         print("(ParentClass > __init__)")
#         self._name = name
#
#     def welcome(self):
#         print("(ParentClass > some_method)")
#         return f'Hello {self._name}!'
#
#
# print('Parent Instantiation:')
# parent_ins = MyParentClass('Reza')
# print('\nParent Welcoming:')
# print(parent_ins.welcome())
#
#
# class MyChildClass(MyParentClass):
#     def __init__(self, name='Akbar'):
#         super().__init__('Mr. ' + name)
#         print("(ChildClass > __init__)")
#
#     def welcome(self):
#         print("(ChildClass > some_method)")
#         return super().welcome()
#
#
# print('Child Instantiation:')
# child_ins = MyChildClass()
# print('\nChild Welcoming:')
# print(child_ins.welcome())


# import datetime
# x = datetime.datetime(2020, 5, 17, 16)
# print(x)


# from datetime import datetime
#
# dt = datetime.today()
# seconds = dt.timestamp()
# print(dt)
#
# import datetime
#
# x = datetime.datetime(1999, 4, 7, 12)
# print(x)
# print(dt - x)


# class Base:
#     def method(self):
#         return f'base'
#
#
# class Father(Base):
#     def method(self):
#         return super().method() + 'father'
#
#
# class Mother(Base):
#     def method(self):
#         return super().method() + 'mother'
#
#
# class Child(Father, Mother):
#     pass
#
#
# c = Child()
# print(c.method())


# f = open('example.txt', 'w')
#
# f.write('Test test.py:\nhello world\ndate:4/14\ntime:8:40')
# f.close()
# f = open('example.txt')
# print(f.readline())
# print(f.readline(7))
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readlines(10))
# print(f.readlines())

# class User:
#     def __init__(self, id, name, phone):
#         self.id = id
#         self.name = name
#         self.phone = phone
#
#     def save(self):
#         file_name = f'{self.name}.user'
#         with open(file_name, 'w') as f:
#             f.write(f'{self.id=}\n{self.name=}\n{self.phone=}')
#         return file_name
#
#     @classmethod
#     def from_file(cls, file_path):
#         self = User.__new__(User)
#         with open(file_path, 'r') as f:
#             file_content = f.read()
#         exec(file_content)
#         return self
#
#
# u = User(1, 'akbar', '9129000111')
# file_name = u.save()
# print(file_name)


# s = 'salam salam akbar 1 11 2223 1'
# print(s.split())
#
# print(list(set(s.split())))

# data = [
#  {
#  'key1': 1,
#  'key2': 2,
#  'key-name': 'akbar',
#  },
#  (1, 2, 3, 4),
#  'A String!'
# ]
#
#
# import pickle
# pickled = pickle.dumps(data)
# print('PICKLED:', pickled)
# unpickled = pickle.loads(pickled)
# print('UN-PICKLED:', unpickled)

# import pickle
#
#
# class User:
#     def __init__(self, id, name, phone):
#         self.id = id
#         self.name = name
#         self.phone = phone
#
#
# u = User(1, 'akbar', '09123456789')
# pickled = pickle.dumps(u)
# print('PICKLED user:', pickled)
# unpickled = pickle.loads(pickled)
# print('UN-PICKLED user:', unpickled)


# class NormalizerError(Exception):
#     pass
#
#
# class PhoneNumError(NormalizerError):
#     phone_number: str
#
#     def __init__(self, phone_number, *args):
#         super().__init__(*args)
#         self.phone_number = phone_number
#
#
# def normalize_phone(phone_num: str, prefix_num='+98'):
#     # Get last 10 digits of phone number (must starts with '9')
#     phone_num = phone_num[-10:]
#     if len(phone_num) < 10:
#         raise PhoneNumError(phone_num, "Phone number Length must be >= 10 .")
#     if not phone_num.isnumeric():
#         raise PhoneNumError(phone_num, "Phone number is NOT numeric.")
#     if not phone_num.startswith('9'):
#         raise PhoneNumError(phone_num, "Phone number does NOT start with '9'.")
#     return prefix_num + phone_num  # Also may raises `TypeError `
#
#
# normalize_phone('09379880665')  # OK
# # normalize_phone('379880665') # PhoneNumError : Length
# # normalize_phone('0937988o665') # PhoneNumError : Numeric
# # normalize_phone('0379880665') # PhoneNumError : Doesn't start with 9
# # normalize_phone('9379880665', 0) # TypeError: str + int


# def division(a: float, b: float):
#     assert b, "Division by Zero"
#     return a / b
#
#
# print(division(5, 0))
#
# import logging
# import os
#
#
# # ----------------------------------------------------------------------
# def log(path, multipleLocs=False):
#     """
#     Log to multiple locations if multipleLocs is True
#     """
#     fname = os.path.splitext(path)[0]
#     logger = logging.getLogger("Test_logger_%s" % fname)
#     logger.setLevel(logging.INFO)
#     fh = logging.FileHandler(path)
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
#     fh.setFormatter(formatter)
#     logger.addHandler(fh)
#
#     if multipleLocs:
#         console = logging.StreamHandler()
#         console.setLevel(logging.INFO)
#         console.setFormatter(formatter)
#         logger.addHandler(console)
#
#     logger.info("This is an informational message")
#     try:
#         1 / 0
#     except ZeroDivisionError:
#         logger.exception("You can't do that!")
#
#     logger.critical("THIS IS A SHOW STOPPER!!!")
#
#
# if __name__ == "__main__":
#     log("sample.log")  # log only to file
#     log("sample2.log", multipleLocs=True)  # log to file AND console!

#
#
#
#
#
#
#
#
#
#
# import pickle
#
#
# class User:
#     def __init__(self, id, name, phone):
#         self.id = id
#         self.name = name
#         self.phone = phone
#
#     def save(self):
#         file_name = f'{self.id}.user'
#         with open(file_name, 'wb') as f:
#             pickle.dump(self, f)
#         return file_name
#
#     @classmethod
#     def from_file(cls, file_path):
#         with open(file_path, 'rb') as f:
#             return pickle.load(f)
#
#
# u = User(1, 'akbar', '9129000111')
# file_name = u.save()
# print(file_name)
#
# other_u = User.from_file(file_name)
# print(other_u.id, other_u.name, other_u.phone)

#
#
#
#
#
#
#
# import time
# from datetime import datetime
#
# class ProcessTimer:
#     def __enter__(self):
#         self.start = datetime.now()
#
#     def elapsed_time(self):
#         return self.end - self.start
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.end = datetime.now()
#
# p_timer = ProcessTimer()
# with p_timer:
#     time.sleep(2)
# print(p_timer.elapsed_time())
#
#
#
#
#
#
#
#
# from typing import Generator, Iterator
#
#
# def generator(n):
#     for i in range(n):
#         yield i ** 2
#
#
# g1 = generator(100)
# g2 = (i ** 2 for i in range(100))  # Generator comprehensions!
# print(isinstance(g1, Generator))
# print(isinstance(g2, Generator))
# print(isinstance(g1, Iterator))
# print(isinstance(g2, Iterator))
# # print(list(g1))
# print(list(g1) == list(g2))
#
#
#
#
#
#
#
#
#
#
# def is_primal(n: int):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# def primals_func(n: int):
#     res = []
#     for i in range(2, n + 1):
#         if is_primal(i):
#             res.append(i)
#     return res
#
#
# for i in primals_func(100):
#     print(i, end=', ')
# print("\nTry it with a bigger number:")
# for i in primals_func(100000):
#     print(i, end=', ')
#
#
# def primals_gen(n: int):
#     for i in range(2, n + 1):
#         if is_primal(i):
#             yield i
#
#
# for i in primals_gen(100):
#     print(i, end=', ')
# print("\nTry it with a bigger number:")
# for i in primals_gen(100000):
#     print(i, end=', ')
#
#
#
#
#
#
#
#
#

#
# import logging
# from datetime import datetime
# import typing
#
# logging.basicConfig(level=logging.INFO)
#
#
# def process_time(func):
#
#     def inner_func(*args, **kwargs):
#         start = datetime.now()
#         a = func(*args, **kwargs)
#         end = datetime.now()
#         res = end - start
#         logging.info(f'running time= {res}')
#         return a
#
#     return inner_func
#
#
# def is_primal(n: int):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# @process_time
# def primals_func(n: int):
#     res = []
#     for i in range(2, n + 1):
#         if is_primal(i):
#             res.append(i)
#     return res
#
#
# n = 100
# # g = process_time(primals_func, n)
# print(primals_func(n))
#
#
#
#
#
#
#
# from typing import Literal
# import os
#
#
# def convert_unit(unit: Literal['B', 'KB', 'MB', 'GB']):
#     "Decorator: Returns converted result from byte"
#     def inner():
#         pass
#     return inner
#
#
# # @convert_unit('KB')
# def get_directory_size(directory_address) -> int:
#     """Returns the `directory` size in bytes."""
#     path = directory_address
#     dirs = os.listdir(path)
#
#     for fname in dirs:
#         if os.path.isfile(fname):
#             return os.path.getsize(fname)
#
#
# if __name__ == '__main__':
#     # TODO: Complete here
#     pass
#
#
# print(get_directory_size('F:\me\Maktab Sharif\جنگو\hw5'))
#
#
#
#
#
#
#
#
# import translators as ts
# import sys
#
#
# def translator(func):
#     def inner(*args, **kwargs):
#         t = func(*args, **kwargs)
#         return ts.google(t, to_language='fa')
#
#     return inner
#
#
# @translator
# def text(txt):
#     txt = str(txt)
#     return txt
#
#
# if __name__ == '__main__':
#     text('hi')
#     print(sys.argv)
#
#
#
#
#
#
#
# import argparse
# import pyscreenshot
#
#
# def save_screenshot(path, name, ext):
#     my_screen_shot = pyscreenshot.grab()
#     file_name = f'{path}{name}.{ext}'
#     with open(file_name, 'wb') as f:
#         my_screen_shot.save(f)
#     return file_name
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Take screenshot example')
#     parser.add_argument('-p', '--path', action='store', metavar='DIR_PATH', default='',
#                         help='directory path for save')
#     parser.add_argument('-n', '--name', action='store', metavar='NAME', default='screen_shot',
#                         help='file name for save')
#     parser.add_argument('-e', '--ext', action='store', metavar='EXT', choices=['png', 'jpg', 'jpeg'], default='png',
#                         help='extension of image file')
#     args = parser.parse_args()
#     file_path = save_screenshot(args.path, args.name, args.ext)
#     print('File path:', file_path)
#
#
#
#
#
#
#
#
#
# import argparse
#
# import translators
# import sys
#
#
# def translator(text, to_lang, from_lang='auto', provider='google'):
#     translator_func = getattr(translators, provider)
#     return translator_func(text, from_language=from_lang, to_language=to_lang)
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Translator')
#
#     parser.add_argument(metavar='file_path', action='store', dest='file_path', help='file path', nargs='?')
#     parser.add_argument('-t', '--to_lang', metavar='TO_LANG', action='store', default='fa',
#                         help='select destination language')
#     parser.add_argument('-f', '--from_lang', metavar='FROM_LANG', action='store', default='auto',
#                         help='select origin language')
#     parser.add_argument('-p', '--provider', metavar='PROVIDER', action='store', default='google',
#                         help='select provider')
#     parser.add_argument('-s', '--save_path', metavar='SAVE_PATH', action='store', required=False,
#                         help='select a path to save the result (optional)')
#
#     args = parser.parse_args()
#     file_path = translator(args.file_path, 'fa')
#     if file_path:
#         with open(file_path) as f:
#             content = f.read()
#             # res = translator(content, 'fa')
#     else:
#         content = input(': ')
#
#     res = getattr(translators, args.provider)(content, to_language=args.to_lang, from_language=args.from_lang)
#
#     print('File path:', file_path, '\n', res)
#
#
#
#
#
#
#
#
#
#
#
# import datetime
# fourth_jan = datetime.date(2019, 5, 4)
# print(fourth_jan)
# for i in range(20):
#     delta = datetime.timedelta(fourth_jan.isoweekday()+7*i)
#     print(fourth_jan + delta)
#
#
#
#
#
#
# import re
# import datetime
#
# txt = """Neque est adipisci dolor labore numquam temp 1995-01-01 04:42:47 ora etincidunt.
# Numquam quaerat dolorem ut sit 1997-11-25 21:10:01 .
# Tempora quiquia ipsum numquam quaer 2005-09-06 09:41:28 at.
# Sit sit amet amet  1994-08-09 21:11:06 sit quiquia voluptatem adipisci.
# Quisquam quaerat tempora ut velit numquam dolo 2006-11-03 03:31:15 r.
# Dolor dolorem dolor a 1999-02-20 12:13:08 dipisci.
# Amet si 1992-05-28 16:30:26 t quiquia quiquia est labore neque etincidunt.
# Sit porro velit dolorem etincidun 1993-04-11 16:21:21 t magnam.
# Consectetur ut non non consect 1992-05-24 07:43:16 etur ipsum ut dolorem.
# Adipisci dolor temp 1995-02-12 15:55:26 ora quiquia est consectetur quisquam tempora.
# Dolore modi etincidunt quaerat d 2009-05-13 10:37:14 olorem.
# Amet est ipsu 2001-07-30 22:20:32 m tempora tempora eius.
# Dolor porro velit quaerat  2020-09-01 10:54:22 porro modi labore consectetur.
# Labore consectetur dolore magnam etin 1992-05-31 10:42:50 cidunt modi velit.
# Numquam  1996-01-24 07:11:33 quisquam sed est tempora.
# Numqu 2003-04-13 08:41:28 am ipsum porro numquam tempora tempora etincidunt sit.
# Am 2003-12-16 07:20:40 et quiquia neque magnam.
# Dolor porro etincid 2019-10-04 03:23:32 unt ipsum quaerat neque adipisci.
#  2008-02-15 04:52:01 Labore voluptatem quiquia eius velit adipisci.
# Consectetur quaerat aliquam velit quaerat la 2001-02-13 20:03:10 bore sed dolorem."""
#
# frmt = '(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})'
# # x = re.findall(frmt, txt)
# # print(x)
#
# txt = txt.splitlines()
#
#
# # print(txt)
#
# def dates(text):
#     a = re.search(frmt, text)
#     if a:
#         # print(a.group(1))
#         date_text = text[a.start():a.end()]
#         d = datetime.datetime.fromisoformat(date_text)
#         return d
#
#
# print(sorted(txt, key=dates))
#
#
#
#
#
#
#
#
#
from flask import Flask

app = Flask(__name__)


@app.route('/<int:a>', defaults={'b': 2})
@app.route('/<int:a>/<int:b>')
def power(a, b):
    return f'{a}**{b}={a ** b}'


app.run()
