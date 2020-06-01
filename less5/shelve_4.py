from datetime import datetime, date, timedelta
from random import randint
import shelve

class AdminCounterException:
    pass


class IncorrectLoginOrPassword:
    pass

filename = 'user_dict'

class User:

    user_dict = {}
    user_posts = {}

    def __init__(self, username, login, password, is_admin=False):
        self._username = username.lower()
        self._login = login
        self._password = password
        self._is_admin = is_admin
        self._registration_date = date.today() - timedelta(randint(0, 1000))
        self._posts = []

        if not is_admin and not User.user_dict:
            raise AdminCounterException

    def check_login(self, login):
        if login in User.user_dict:
            return False
        else:
            return True

    def create_post(self):
        post = input("Post: \n")
        User._posts = {
            self._username: {
                "post": post,
                "post_date": datetime.strftime(datetime.now() ,"%Y.%m.%d %H:%M:%S")
            }}
        print(User._posts)

    def show_post(self, user=None):
        if self._is_admin and user:
            print(user)
            user = User.user_dict.get(user)
            if user:
                for post in user.posts:
                    print(post, end='\n\n')
            print('\n\n')
        elif self._is_admin:
            for username in User.user_dict:
                self.show_post(username)
        else:
            for post in self._posts:
                print(post, end='\n\n')

    def show_user_list(self):
        if self._is_admin:
            for value in User.user_dict.values():
                print(value.username, value.registration_date)
        else:
            print(self._username, self._registration_date)


class Registration_Authorisation:

    def check_pass(self, password):
        while True:
            alphabet = set('abcdefghijklmnopqrstuvwxyz')
            numbers = set('0123456789')
            good_password = False
            if len(password) >= 8:
                good_password = True

            for s in alphabet:
                if good_password and s in password:
                    break
                elif not good_password:
                    break
            else:
                good_password = False

            for s in numbers:
                if good_password and s in password:
                    break
                elif not good_password:
                    break
            else:
                good_password = False
            return good_password

    def sign_up(self):
        if User.user_dict:
            register_str = 'Enter desired username: '
            is_admin = False
        else:
            register_str = 'Enter login(admin): '
            is_admin = True
        while True:
            username = input(register_str).strip().lower()
            if User.user_dict.get(username):
                print('Such user already exists')
                continue
            break
        while True:
            password = input('Type password: ')
            if password != input('Retype password: '):
                print('Type password, please')
                continue
            if not self.check_pass(password):
                print('Your password should follow the rules')
                continue
            break
        with shelve.open(filename) as db:
            db[username] = {
                "login": username,
                "password": password}
        try:
              User.user_dict[username] = User(username, password, is_admin)
        except AdminCounterException as err:
            print(err)


    def sign_in(self, username, password):
        with shelve.open(filename) as db:
            login = username
            password = password
            if login and password in db:
                print(f"You have sing in with the name {username}")


    def exit(self, username):
        return print(f"you are log out {username}")

    def load_info_to_file(self, filename):
        with shelve.open(filename) as user_dict_shelve:
            for user, attributes in user_dict_shelve.items():
                User.user_dict[user] = attributes

    def save_info_to_file(self, filename):
        with shelve.open(filename) as user_dict_shelve:
            for user, attribute in User.user_dict.items():
                user_dict_shelve[user] = attribute

def main():
    r_a = Registration_Authorisation()

    user_db = 'user_dict_file.db'


    while True:
        choise = input('You want to login(1), register(2) or exit(3)?: ').strip()
        if choise not in set('123'):
            print('Wrong input!')
            continue
        elif choise == '3':
            print('Goodbye!!!')
            break
        elif choise == '2':
            r_a.sign_up()
            continue
        elif choise == '1':
            try:
                user = r_a.sign_in(input('login: '), input('password: '))
            except IncorrectLoginOrPassword as err:
                print(err)
                continue
        while True:
            choise = input('You want to see_user_list(1), create_post(2), see_posts(3) or exit(4)?: ').strip()
            if choise not in set('1234'):
                print('Wrong input!')
                continue
            elif choise == '4':
                print('Goodbye!!!')
                break
            elif choise == '3':
                user.show_post()
                continue
            elif choise == '2':
                user.create_post()
                continue
            elif choise == '1':
                user.show_user_list()
                continue


if __name__ == '__main__':
    main()





