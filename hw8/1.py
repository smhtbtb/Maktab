import argparse


def avg(*args, F=2):
    x = 0
    for i in range(len(args[0])):
        if str(args[0][i]).isnumeric() or str(args[0][i]).find('.'):
            print(args)
            x += float(args[0][i])
        else:
            raise Exception('please enter only numbers')
    a = x / len(args[0])
    return f'{a:.{args[1]}f}'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='average of marks')

    parser.add_argument('-g', '--grades', metavar='Grades', action='store', type=float, required=True, nargs='+', help='marks')
    parser.add_argument('-f', '--float', metavar='Float', action='store', default=2, help='decimal of average num')

    args = parser.parse_args()
    res = avg(args.grades, args.float)
    print(res)
