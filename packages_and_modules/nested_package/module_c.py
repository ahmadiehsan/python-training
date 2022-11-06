from packages_and_modules.nested_package.module_a import sample_function2

print('I am the fist line of the happy module_c')


def another_func():
    print('I am the result of the another_function')


def another_func2():  # Not used by module_b nor module_a
    print('I am the result of the another_function2')
    sample_function2()


print('I am the last line of the happy module_c')
