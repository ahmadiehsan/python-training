from circular_import_test.c import c


def b():
    print('b')
    c()
