from cryptography.fernet import Fernet


# TODO: testing(making string to bytes)
# key = Fernet.generate_key()
# f = Fernet(key)
# s = 'bah bah'
# b = bytes(s, 'utf-8')
# token = f.encrypt(b)
# print(f.decrypt(token))


# TODO: Generating key in file
def key_generating(key_file_name):
    key = Fernet.generate_key()
    with open(key_file_name, 'wb') as f:
        f.write(key)
    return f


# TODO: testing(encrypt from file)
# with open('key_file', 'rb') as g:
#     f = Fernet(g.read())
#
# token = f.encrypt(b'salam')
# print(f.decrypt(token))


# def my_dec(key):
#     def inner1(func):
#         def inner2(*args, **kwargs):
#             pass
#
#         return inner2
#
#     return inner1
#
#
class Encrypt:

    def encrypting_passage(self, passage, key_file_name):
        s = passage
        b = bytes(s, 'utf-8')
        k = key_generating(key_file_name)
        with open(key_file_name, 'rb') as f:
            key = f.read()
            g = Fernet(key)
            token = g.encrypt(b)
        return g.encrypt(token)

    def encrypting_files(self, passage_file, key_file_name):
        with open(passage_file) as p:
            s = p.read()
        b = bytes(s, 'utf-8')
        k = key_generating(key_file_name)
        with open(key_file_name, 'rb') as f:
            key = f.read()
            g = Fernet(key)
            token = g.encrypt(b)
        return g.encrypt(token)


class Decrypt:

    def decrypting_passage(self, binary_passage, keyy):
        pass

#     def decrypting_files(self, file, keyy):
#         pass
