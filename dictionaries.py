x = {
    'a': 16,
    5: 6.7,
    'name': 'amir',
    'final': [1, 2, 3]
}

print(x['name'])  # get

del x['name']
print(x)

x['a'] = 20  # update

print(len(x))  # length

x_keys = x.keys()  # keys
x_keys_as_list = list(x_keys)  # keys
print(x_keys_as_list[1])  # keys

x_values = x.values()  # values
x_values_as_list = list(x_values)  # values
print(x_values_as_list[-1])  # values
