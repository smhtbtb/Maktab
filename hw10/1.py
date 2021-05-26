import re


def name_validation(name: str):
    x = re.findall("([a-zA-Z\_?]{5,14}$)", name)
    if name == ''.join(x):
        return name
    else:
        return f'invalid name'


# print(name_validation('F____dsvs_jht_'))


def email_validation(email: str):
    x = re.search("([a-z\d_.?]){3,}\@[a-z]{3,}\.[a-z]{2,}", email)
    # print(x.group())
    if email == x.group():
        return email
    else:
        return f'invalid email'

# print(email_validation('saaalam_re.09@sal.ir'))


def phone_validation(phone: str):
    x = re.search("(\+98|0)[\d]{10}", phone)
    # print(x)
    if phone == x.group():
        return phone
    else:
        return f'invalid phone'


# print(phone_validation('+989309291934'))
