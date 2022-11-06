class A:
    def one(self):
        return 'A -> one'


class AA(A):
    pass


class B:
    def one(self):
        return 'B -> one'


class C(AA, B):
    pass


def main():
    c = C()
    print(c.one())

    # ----------------------

    print(isinstance(c, A))


main()
