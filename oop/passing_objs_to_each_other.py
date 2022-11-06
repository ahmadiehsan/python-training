from datetime import date


class Creature:
    def __init__(self, birth_year):
        self.birth_year = birth_year

    def age_calculator(self, this_year):
        return this_year - self.birth_year


class Animal(Creature):
    def __init__(self, sound, legs, birth_year):
        super().__init__(birth_year)
        self.sound = sound
        self.legs = legs

    def make_sound(self):
        return f'{self.sound} {self.sound} {self.sound}'


class Human(Creature):
    def __init__(self, first_name, last_name, birth_year, pet=None):
        super().__init__(birth_year)
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def pet_info(self):
        if self.pet:
            this_year = date.today().year
            return f"{self.full_name()}'s pet has {self.pet.age_calculator(this_year)} years old"
        else:
            return f"{self.full_name()} doesn't have any pet :("


class VIPHuman(Human):
    def full_name(self):
        return f'sir {self.first_name} {self.last_name}'


def main():
    sasha_dog = Animal('bark', 4, 2019)
    sasha = VIPHuman('sasha', 'sobhani', 1993, sasha_dog)
    ehsan = Human('ehsan', 'ahmadi', 1996)

    print(sasha.pet_info())
    print(ehsan.pet_info())


main()
