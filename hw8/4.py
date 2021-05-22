import argparse
import random


def guess_num_script(first_num: int, last_num: int, how_many_guess: int):
    x = random.randrange(first_num, last_num)
    print(x)
    i = 0
    while i <= how_many_guess:
        i += 1
        n = int(input('num\n'))
        if n < x:
            if i == how_many_guess:
                if n == x:
                    print(f'congrats, your {i} guess is true.')
                    break
                else:
                    print(f'False. You reach the max amount of guess.')
                    break
            else:
                print(f'{n=} is less than x')

        elif n > x:
            if i == how_many_guess:
                if n == x:
                    print(f'congrats, your {i} guess is true.')
                    break
                else:
                    print(f'False. You reach the max amount of guess.')
                    break
            else:
                print(f'{n=} is greater than x')

        elif n == x:
            print(f'congrats, your {i} guess is true.')
            break

    return 0


# print(guess_num_script())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='average of marks')

    parser.add_argument('-f', '--first_num', metavar='First_num', action='store', type=int, required=True,
                        help='Range of your random number begins from first number')
    parser.add_argument('-t', '--last_num', metavar='Second_num', action='store', type=int, required=True,
                        help='Range of your random number ends in last number')
    parser.add_argument('-g', '--guess', metavar='Guess', action='store', type=int, required=True,
                        help='How many guess do you want')

    args = parser.parse_args()
    # res = avg(args.grades, args.float)
    res = guess_num_script(args.first_num, args.last_num, args.guess)
    print(res)
