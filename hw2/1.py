s = input('string: ')


def turn(_: str):
    list1 = [i for i in _]
    list2 = []
    x = 0
    while x < len(list1):
        list2.append(list1[-1 - x])
        x += 1

    return list2


def palindrome(_: str):
    list1 = [i for i in _]
    if turn(_) == list1:
        return True
    else:
        return False


print(palindrome(s))