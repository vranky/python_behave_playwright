import random
import string
from operator import index

import names
from faker import Faker
from random import randint

fake = Faker()


def random_digit(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def random_string(n):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(n))


def password_generator(length=8):
    LETTERS = string.ascii_letters
    NUMBERS = string.digits
    PUNCTUATION = string.punctuation
    # create alphanumerical from string constants
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'

    # convert printable from string to list and shuffle
    printable = list(printable)
    random.shuffle(printable)

    # generate random password and convert to string
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password


def random_data():
    fName = names.get_first_name(gender='female')
    lName = names.get_last_name()

    return {
        "first_name": fName,
        "last_name": lName,
        "user_name": f"test_{fName}{lName}@test.sk",
        "company_name": f"test_{fake.company().replace('-', '_').replace(' ', '_').replace(',', '').lower()}",
        "phone_number": f"+421{random_digit(9)}",
        "vat": str(random_digit(6)),
        "street_num": str(random_digit(4)),
        "street": str(fake.street_name()),
        "zip_code": f"{random_digit(3)} {random_digit(2)}",
        "country": "Slovakia",
    }


def get_item(data_table, item):
    input = dict([i.cells for i in data_table.rows])
    try:
       return input[item]
    except KeyError:
        return -1


def get_context_item(data_table, item_key):
    data = random_data()
    item_val = get_item(data_table, item_key)
    return item_val if item_val != -1 else data[item_key]
