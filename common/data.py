import random
import string


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