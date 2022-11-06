class FakeStr:
    def __init__(self, string):
        self.string = string

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError("can't multiply sequence by non-int of type 'FakeStr'")

        result = ''

        for i in range(other):
            result += self.string

        return result

    def __int__(self):
        return len(self.string)


ehsan = FakeStr('ehsan')
print(isinstance(ehsan, str))

print(int(ehsan))
