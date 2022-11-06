from errors.nested_error_2 import print_x_variable_value


def one():
    print_x_variable_value()


def two():
    one()


def three():
    two()

three()
