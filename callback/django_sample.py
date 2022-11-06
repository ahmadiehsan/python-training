def django_runner(developer_callback_func):
    print('get user url')
    print('do security step 1')
    print('do security step 2')
    print('do security step 3')
    print('run middlewares')

    result = developer_callback_func()

    print('do final security check')
    print(f'send user response {result}')
