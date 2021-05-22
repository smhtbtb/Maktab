def calculate(values: str):
    values1 = values.split()
    print(values1)
    # a = values1[0]
    # b = values1[2]
    # calc = values1[1]

    if len(values1) != 3:
        raise IndexError('two numbers please')
    if not values1[0].isnumeric() or not values1[2].isnumeric():
        raise Exception('wrong numbers')
    if int(values1[2]) == 0 and values1[1] == '/':
        raise ZeroDivisionError('second number is 0')

    c1 = ['*', '/', '+', '-', '**', '//', '%']
    if values1[1] not in c1:
        raise Exception('not valid sign')

    return print(eval(values))


calculate('3 * 3')
