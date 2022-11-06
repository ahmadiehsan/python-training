a = [2, 10, 11, 89, -1, 1, 33, 88, {'y': 11, 'u': 17}]
b = [66, 90]

print(a[0])
print(a[2])

a.sort()
print(len(a))

a.extend(b)
print(a)

print(a[1:5])  # slicing
print(a[:5])  # slicing
print(a[1:])  # slicing
print(a[1:6:2])  # slicing
print(a[-1])  # slicing

a[0] = 3  # update
