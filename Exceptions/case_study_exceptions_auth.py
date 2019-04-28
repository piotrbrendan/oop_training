import hashlib
import collections

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False


    def _encrypt_pw(self,password):

        hash_string = '{}{}'.format(self.username, password).encode('utf8')
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self,password):
        encrypted = self._encrypt_pw(password)

        return encrypted == self.password

    def change_password(self,old_password,new_password):

        if self.check_password(old_password):
            self.password = self._encrypt_pw(new_password)
            print('Password changed')
        else:
            print('Wrong password')



class AuthException(Exception):
    def __init__(self,username, user = None):
        super().__init__(username, user)
        self.username = username
        self.user = user

class UsernameAlreadyExists(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass

class PasswordTooSimple(AuthException):
    pass

class InvalidUsername(AuthException):
    pass

class InvalidPassword(AuthException):
    pass

class Authenticator:

    def __init__(self):
        self.users = {}

    def add_user(self,username, password):



        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 4:
            raise PasswordTooShort(username)

        little_dist_words = (len(collections.Counter(password).keys()) / len(password)) < 0.5
        all_lower = password.islower()
        alpha_only = password.isalpha()

        if any([little_dist_words,all_lower, alpha_only]):
            raise PasswordTooSimple(username)

        self.users[username] = User(username,password)

    def login(self,username, password):

        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):

        if username in self.users:
            return self.users[username].is_logged_in

        return False







