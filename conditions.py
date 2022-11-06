if 2 == 6:  # => False
    print('a')
elif 4 == 8 or 7 == 7:  # => True
    print('b')
elif not (6 == 6 and 9 == 10):  # => not(False) ==> True
    print('c')
else:
    print('d')


if 4 == 8 or 7 == 7:  # => True
    print('bb')

if not (6 == 6 and 9 == 10):  # => not(False) ==> True
    print('cc')

# ------------ compare operators
# >=
# <=
# >
# <

# ------------ operators for data collections
data_collection = (1, 2, 3, 4, 5)

if 10 in data_collection:  # => False
    print('1')
elif 18 not in data_collection:  # => True
    print('2')
else:
    print('3')

# =============== one line condition
x = 10

# ----- old way
# if x > 20:
#     status = 'happy :)'
# else:
#     status = 'sad :('

# ----- better way
status = 'happy :)' if x > 20 else 'sad :('
