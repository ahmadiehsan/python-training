# ---------------- Basic data types

12  # integer
3.5  # float
"ehsan"  # string
'ehsan'  # string
True  # boolean
False  # boolean
None  # none

5.7
'results of ehsan in his last exam: 5.7'

# ---------------- Data collections

e = [
    16,
    6.7,
    'hamed',
    [1, 2, 3],
    4,
    5,
    6,
    7,
    8,
    9,
]  # list (other languages: array)

b = (
    16,
    6.7,
    'ehsan',
    [1, 2, 3]
)  # tuple

x = {
    'a': 16,
    5: 6.7,
    'name': 'amir',
    'final': [1, 2, 3]
}  # dictionary

# ---------------- Data conversion

str(49)  # => "49"
int("56")  # => 56
float(33)  # => 33.0
float("35")  # => 35.0
bool(1)  # => True
bool(0)  # => False

# # ---------------- Operations

print(2 + 2)
print(3 + 5.0)
# print("5" + 7)  # => error
print('34' + '90')
print(type('34' + '90'))
print('ehsan' * 2)
# print('ehsan' - 2)  # => error
# print(50/0)  # => error
print(2**3)
print(9.0//2)

print([1, 2] + [3, 4])
