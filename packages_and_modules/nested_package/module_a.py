from packages_and_modules.nested_package.module_c import another_func

print('I am the first line of the module_a')


def sample_function():
    print('I the first version of the sample_function')


def sample_function():
    print('I am the the first line of the second version of the sample_function')
    another_func()
    print('I am the the last line of the second version of the sample_function')


def sample_function2():  # Not used by module_b
    print('I am the sample_function2')


print('I am the last line of the module_a')
