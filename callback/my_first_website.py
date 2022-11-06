from callback.django_sample import django_runner


def home_page():
    return 'This is my first website home page, I am very happy now'


django_runner(home_page)
