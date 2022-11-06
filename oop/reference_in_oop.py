class Human:
    def __init__(self, name):
        self.name = name


ehsan = Human('n1')
ehsan_new = ehsan

print(ehsan.name)
print(ehsan_new.name)

ehsan.name = 'n2'

print(ehsan.name)
print(ehsan_new.name)
