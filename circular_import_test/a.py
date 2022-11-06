from circular_import_test.b import b


def a():
    print('a')
    b()
