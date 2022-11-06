# --------- loops over data collections
# === list
a = [1, 'ehsan', 3, 'hassan']

for element in a:
    print(element)

# === dictionary
b = {'x': 'r', 'z': 't'}

print(b.keys())  # => ['x', 'z']

for key in b.keys():
    print(key)

for value in b.values():
    print(value)

for k, v in b.items():  # => [['x', 'r'], ['z', 't']]
    print(k)
    print(v)

# ---------- loops over range of numbers
for number in range(2, 20, 3):
    print(number)

# ---------- while loop
i = 1
while i <= 4:
    print(i)
    i += 1

print(i)

# ---------- break and continue
for n in range(100):
    if n % 9 != 0:
        continue

    print(n)

for name in ['mamad', 'javad', 'akbar']:
    if name == 'javad':
        print(name)
        break

# ---------- nested loops
for name2 in ['mamad', 'javad', 'akbar']:
    for num2 in [1, 2, 3, 4, 5]:
        print(f'{name2} -- {num2}')
