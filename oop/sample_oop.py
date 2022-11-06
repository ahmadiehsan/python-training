from datetime import date


class Creature:
    def __init__(self, birth_year):
        self.birth_year = birth_year

    def age_calculator(self, this_year):
        return this_year - self.birth_year


class Human(Creature):
    def __init__(self, first_name, last_name, birth_year):
        super().__init__(birth_year)
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class VIPHuman(Human):
    def full_name(self):
        return f'sir {self.first_name} {self.last_name}'


class Animal(Creature):
    def __init__(self, sound, legs, birth_year):
        super().__init__(birth_year)
        self.sound = sound
        self.legs = legs

    def make_sound(self):
        return f'{self.sound} {self.sound} {self.sound}'


def main():
    hamed = Human('hamed', 'ahmadi', 1988)
    ehsan = Human('ehsan', 'ahmadi', 1996)
    sasha = VIPHuman('sasha', 'sobhani', 1993)

    dog = Animal('bark', 4, 2018)
    duck = Animal('quack', 2, 2016)

    print(hamed.first_name)
    print(ehsan.first_name)

    this_year = date.today().year

    print(hamed.age_calculator(this_year))
    print(ehsan.age_calculator(this_year))

    print(hamed.full_name())
    print(ehsan.full_name())
    print(sasha.full_name())

    print(dog.make_sound())
    print(duck.make_sound())

    print(duck.age_calculator(this_year))


main()
