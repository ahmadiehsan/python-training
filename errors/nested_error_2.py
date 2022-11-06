import requests
from datetime import datetime


def print_x_variable_value():
    requests.get(
        'https://google.com',
        json={
            'time': str(datetime.now())
        }
    )
