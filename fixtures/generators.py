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