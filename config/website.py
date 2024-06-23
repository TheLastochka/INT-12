import random
import json

class Website:
    DOMAIN = 'https://www.automationexercise.com/'
    _LOGIN_DATA = [
        {
            "username": "test_user_8352",
            "email": "test_user_8352@mail.ru",
            "password": ";g.GK5QE"
        }
    ]

    def get_login_data(self) -> dict:
        login_data = self._LOGIN_DATA
        with open('config/test_data.json', 'r') as file:
            data = json.load(file)
            login_data.extend(data['login_data'])
        return random.choice(login_data)

    def add_login_data(self, username: str, email: str, password: str) -> None:
        login_data = self.get_login_data()
        login_data.append({
            'username': username,
            'email': email,
            'password': password
        })
        with open('config/test_data.json', 'w') as file:
            json.dump({'login_data': login_data}, file, indent=4)