# ----------- how my computer ram works
# id    key                                   value
# 111   f(x)                                  return x ** 2 + 3
# 222   g                                     6
# 333   say_hi(first_name, last_name)         return f'hi, {first_name} {last_name}'
# 444   say_hi_bulk_mode(list_of_users)       for user_data in list_of_users:
#                                                 print(say_hi(user_data['first_name'], user_data['last_name']))
# 555   my_users                              [ {'first_name': 'akbar', 'last_name': 'naghash'}, {'first_name': 'jafar', 'last_name': 'banna'} ]

# 999   sample_fcc(a, b, c)                   print(a, b, c)
# 100   new_fcc                               --> 999


# ---------------- math like functions

# f(x) = x ** 2 + 3
# g = f(6)  => g = 39

def f(x):
    return x ** 2 + 3


g = f(6)
print(g)


# ---------------- data like functions
def say_hi(first_name, last_name):
    return f'hi, {first_name} {last_name}'


print(say_hi('ehsan', 'ahmadi'))


def say_hi_bulk_mode(list_of_users):
    for user_data in list_of_users:
        print(say_hi(user_data['first_name'], user_data['last_name']))


my_users = [
    {'first_name': 'akbar', 'last_name': 'naghash'},
    {'first_name': 'jafar', 'last_name': 'banna'}
]

say_hi_bulk_mode(my_users)


# ---------------- scopes
def scope_test():
    fullname = 'hassan ahmadi'
    return fullname


def scope_test2():
    fullname = 'ehsan ahmadi'
    return fullname


c = scope_test2()


def scope_test3(range_number):
    for i in range(range_number):
        return i


print(scope_test3(100))


# -------------- default values for function arguments
def say_hello2(fullname, hello_message='hi'):
    return f'{hello_message}, {fullname}'


print(say_hello2('hamed ahmadi', 'hello'))
print(say_hello2('hamed ahmadi'))


# ----- Very Important
# don't use reference base default values
def append_to_list(value, input_list=[]):
    input_list.append(value)

    return input_list


x = append_to_list(4)  # [4]

# ...

y = append_to_list(6)  # [4, 6]

# --------------- key base value assignment
def say_hi3(first_name, last_name, age):
    """
    This function will get first_name and last_name and age from user
    and will say hi to the person
    """

    return f'hi, {first_name} {last_name} -- {age}'


print(say_hi3(last_name='ahmadi', first_name='amir', age=10))
print(say_hi3(first_name='amir', last_name='ahmadi', age=15))
print(say_hi3('akbar', age=20, last_name='ahmadi'))

# --------------- global keyword
x = 150


def pp():
    global x
    x = 80
    print(x)


pp()


# --------------- lambda
def old(x):
    return x + 2


new = lambda x: x + 2

print(old(100))
print(new(100))


# --------------- first class citizen
def sample_fcc(a, b, c):
    print(a, b, c)


new_fcc = sample_fcc
sample_fcc(1, 2, 3)
new_fcc(1, 2, 3)
