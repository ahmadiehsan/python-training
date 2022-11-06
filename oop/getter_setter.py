from datetime import date


class Human:
    def __init__(self, birth_year):
        self.this_year = date.today().year
        self.birth_year = birth_year

    def get_this_year(self):  # <-- this is a getter in c#, java mode
        return self.this_year

    def set_this_year(self, new_this_year):  # <-- this is a setter in c#, java mode
        self.this_year = new_this_year

    @property
    def this_year(self):  # <-- this is a getter in python mode
        print('this_year getter called')
        return self.this_year_

    @this_year.setter
    def this_year(self, value):  # <-- this is a setter in python mode
        print('this_year setter called')
        self.this_year_ = value

    def calc_age(self):
        return self.this_year - self.birth_year


h = Human(1990)
print(h.calc_age())

# sample getters
print(h.get_this_year())  # <-- c#, java mode
print(h.this_year)  # <-- python mode

# sample setters
h.set_this_year(2050)  # <-- c#, java mode
h.this_year = 2050  # <-- python mode
