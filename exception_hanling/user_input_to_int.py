import sys


class NotUnder100Error(Exception):
    pass


def get_number():
    try:
        num = int(input('Please enter a nummer: '))
    except ValueError:
        raise ValueError('Your input is not a number')

    return num


def get_under_100_number():
    num = get_number()

    if num > 100:
        raise NotUnder100Error('Number is not less than 100')

    return num


def main():
    number = None

    while True:
        try:
            number = get_under_100_number()

        except NotUnder100Error:
            print('Kheili kesafati')
            sys.exit()

        except ValueError as err:
            print(str(err))
            continue

        break

    print(number + 10)


main()
