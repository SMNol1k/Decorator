import requests

from attempts import with_attempts
from printable import printable


@with_attempts(sleep=1, attempts=4)
def summator(a, b):
    return a + b


@printable
@with_attempts(sleep=2, attempts=10)
def get_swapi_character(character_id):

    return requests.get(f"https://swapi.py4e.com/api/people/{character_id}").json()


get_swapi_character(4)
