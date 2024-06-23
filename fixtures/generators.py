import pytest
import random
import string


@pytest.fixture(scope='function')
def username() -> str:
    return f"test_user_{random.randint(0, 10000)}"

@pytest.fixture(scope='function')
def password() -> str:
    length = 8
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@pytest.fixture(scope='function')
def card_payment():
    return {
        "name": f"Test User {random.randint(0, 10000)}",
        "card_number": ''.join(random.choice(string.digits) for _ in range(16)),
        "expiration_mm": f"{random.randint(1, 12):02d}",
        "expiration_yyyy": str(random.randint(2022, 2030)),
        "cvc": ''.join(random.choice(string.digits) for _ in range(3))
    }