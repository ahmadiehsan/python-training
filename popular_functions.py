# from functions import say_hi

# --------------- input (get data from user in runtime)
# first_name = input('Please enter you first_name: ')
# last_name = input('Please enter you last_name: ')
# print(say_hi(first_name, last_name))


# --------------- map
ages = [12, 80, 93, 15, 27, 31]

# == real:
for new_age in map(lambda num: num + 7, ages):
    print(new_age)

# == simulation:
def map_simulator(func, data_collection):
    r = []

    for element in data_collection:
        answer = func(element)
        r.append(answer)

    return r


def add_7(entry):
    return entry + 7

print(map_simulator(add_7, ages))


# --------------- filter
for i in filter(lambda x: x > 18, ages):
    print(i)
