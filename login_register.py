import json

DB_FILE = 'users_db.json'

def load_database():
    try:
        with open(DB_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_database(data):
    with open(DB_FILE, 'w') as file:
        json.dump(data, file)


def in_database(name):
    db = load_database()
    return any(user['name'] == name for user in db)


def register_database(name, password1, password2):
    db = load_database()

    if in_database(name):
        raise Exception('Юзер с таким именем уже существует')

    if password1 != password2:
        raise Exception('Пароли не совпали')

    user = {'name': name, 'password': password1}
    db.append(user)
    save_database(db)
    return 'Вы успешно зарегистрировались'

def login_database(name, password):
    db = load_database()

    if not in_database(name):
        raise Exception('Пользователь не найден')

    for user in db:
        if user['name'] == name:
            if user['password'] != password:
                return 'Пароль не верный'
    return 'Вы успешно вошли'

def main():
    print('Добро пожаловать')
    try:
        while True:
            action = input('Введите что-то из этого --> rеgister:1, login:2, exit:3  ')
            if action == '3':
                break
            elif action== '1':
                name = input('введите имя пользователя: ')
                password1 = input('введите пароль: ')
                password2 = input('введите снова пароль: ')
                print(register_database(name, password1, password2))
            elif action == '2':
                name = input('введите имя пользователя: ')
                password1 = input('введите пароль: ')
                print(login_database(name, password1))
            else:
                print('Не корректный выбор')
    except Exception as error:
        print(error)
main()
