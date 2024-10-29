import random
import string
from datetime import datetime, timedelta

AUTORISED_USER_PAYLOAD = {
    "login": "Ruslan",
    "password": "qwerty"
}
AUTORISED_USER_ID = 407483
ORDER_PAYLOAD = {}
def generate_order_payload(color):
    def generate_random_string(leng):
        letters = string.ascii_lowercase
        random_lowercase = ''.join(random.choice(letters) for i in range(leng))
        random_string = string.ascii_uppercase[0] + random_lowercase
        return random_string
    ORDER_PAYLOAD['firstName'] = generate_random_string(8)
    ORDER_PAYLOAD['lastName'] = generate_random_string(8)
    ORDER_PAYLOAD['address'] = f'{generate_random_string(6)}, {random.randint(1, 333)} apt.'
    ORDER_PAYLOAD['metroStation'] = random.randint(1, 4)
    ORDER_PAYLOAD['phone'] = f'+{random.randint(1000000000, 9999999999)}'
    ORDER_PAYLOAD['rentTime'] = random.randint(1, 10)
    date = datetime.now() + timedelta(seconds=random.randint(1000000, 999999990))
    date = str(date.date())
    ORDER_PAYLOAD['deliveryDate'] = date
    ORDER_PAYLOAD['comment'] = generate_random_string(20)
    ORDER_PAYLOAD['color'] = color
    return ORDER_PAYLOAD

def generate_register_payload(length):
    def generate_random_string(leng):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(leng))
        return random_string
    login = generate_random_string(length)
    password = generate_random_string(length)
    first_name = generate_random_string(length)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload

def assert_message(expected_status, received_status, resp_json):
    return  f'Ожидаемый статус {expected_status} \nполученный статус {received_status} \n{resp_json}'