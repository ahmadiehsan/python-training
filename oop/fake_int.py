class FakeInt:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return self.number == other.number

    def __add__(self, other):
        return self.number + other.number

    def __ge__(self, other):
        return self.number >= other.number

    def __gt__(self, other):
        return self.number > other.number

    def __le__(self, other):
        return self.number >= other.number

    def __lt__(self, other):
        return self.number > other.number

    def __str__(self):
        return f'This is a FakeInt with value={self.number}'


def main():
    one = FakeInt(1)
    two = FakeInt(55)

    print(one == two)
    print(one + two)
    print(one >= two)
    print(one > two)
    print(one <= two)
    print(one < two)

    print(str(one))


main()
