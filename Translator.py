import translators as ts


def translator(func):
    def inner(*args, **kwargs):
        t = func(*args, **kwargs)
        return ts.google(t, to_language='fa')

    return inner


# decorator with parameters
# def translator(to_lang, from_lang='auto', provider='google'):
#     def inner(func):
#         return ts.deepl
#
#     return inner

@translator
def text(txt):
    txt = str(txt)
    return txt


s = 'jacob'
print(text(s))
