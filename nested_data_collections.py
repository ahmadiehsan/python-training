# ----------- how my computer ram works
# id    key         value
# 111   students    [{'name': 'aaa', 'age': 12 }, ...]
# 222   school      {'name': '13aban', 'students': -> 111, 'classes': [{'name': 'a1', 'students': [--> 111 -> 0, --> 111 -> 2]}]}

students = [
    {'name': 'aaa', 'age': 12},
    {'name': 'bbb', 'age': 14},
    {'name': 'ccc', 'age': 13}
]
school = {
    'name': '13aban',
    'students': students,
    'classes': [
        {'name': 'a1', 'students': [students[0], students[2]]},
        {'name': 'a2', 'students': [students[1]]},
        {'name': 'a3', 'students': [students[1], students[2]]},
    ]
}

# print aaa --> a1
# print ccc --> a1
# print bbb --> a2
# print bbb --> a3
# print ccc --> a3
for classroom in school['classes']:
    for student in classroom['students']:
        print(f"{student['name']} --> {classroom['name']}")

# print name: aaa -- age: 12
# print name: bbb -- age: 14
# print name: ccc -- age: 13
for student in students:
    print(f"name: {student['name']} -- age: {student['age']}")

# print => a1: aaa
# print => a1: ccc
# print => a2: bbb
# print => a3: bbb
# print => a3: ccc
for c in school['classes']:
    for s in c['students']:
        print(f"{c['name']}: {s['name']}")

# print => a1
# print => a2
# print => a3
for c in school['classes']:
    print(c['name'])

# # print => a1
print(school['classes'][0]['name'])