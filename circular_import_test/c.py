from circular_import_test.a import a


def c():
    print('c')
    a()
