from datetime import date


def age_calculator(birth_year, this_year):
    age = this_year - birth_year
    return f'This human has {age} years old'


def full_name(first_name, last_name):
    return f'{first_name} {last_name}'


def make_sound(sound):
    return f'{sound} {sound} {sound}'


def main():
    hamed = {
        'first_name': 'hamed',
        'last_name': 'ahmadi',
        'birth_year': 1988,
    }
    ehsan = {
        'first_name': 'ehsan',
        'last_name': 'ahmadi',
        'birth_year': 1996,
    }

    dog = {
        'sound': 'bark',
        'legs': 4,
        'birth_year': 2016,
    }
    duck = {
        'sound': 'quack',
        'legs': 2,
        'birth_year': 2018,
    }

    print(hamed['first_name'])
    print(ehsan['first_name'])

    this_year = date.today().year

    print(age_calculator(hamed['birth_year'], this_year))
    print(age_calculator(ehsan['birth_year'], this_year))

    print(full_name(hamed['first_name'], hamed['last_name']))
    print(full_name(ehsan['first_name'], ehsan['last_name']))

    print(make_sound(dog['sound']))
    print(make_sound(duck['sound']))

    print(age_calculator(dog['birth_year'], this_year))  # <-- wrong usage


main()
