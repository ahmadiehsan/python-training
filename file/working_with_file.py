from os import path

# --------------- ram
# id    key                 value
# 111   sample_data.txt     ...
# 222   file2               -> 111

# --------------- common
# file modes: r or rb (read), w or wb (write), a or ab (append), r+ (read and write)
# old_path = 'file/sample_data.txt'
new_path = path.join('file', 'sample_data.txt')

# --------------- regular one
file = open(new_path, 'r')

for line in file.readlines():
    print(f'--- {line.strip()}')

file.close()


# --------------- context manager one
with open(new_path, 'r') as file2:
    print(file2.read())

# print(file2.read())  # => error


# --------------- writing in the file
with open(new_path, 'w') as file3:
    file3.write('Another person data')


# --------------- appending data into the file
with open(new_path, 'a') as file4:
    file4.write('\n')
    file4.write('And another good person')
