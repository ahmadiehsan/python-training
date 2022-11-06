from copy import deepcopy

# ----------- how my computer ram works
# id    key    value
# 111   a      999999999999999999999999999
# 356   b      999999999999999999999999999
# 864   c      [1, 2, 3]
# 990   d      -> 864
# 159   e      [1, 2, 3]


# ----------- by value

a = 999999999999999999999999999
b = a

a = 1

print(a)
print(b)

# ----------- by reference (pointer)
c = [1, 2, 3]
d = c

c.append(4)

print(c)
print(d)

# ----------- deep copy
e = deepcopy(c)
