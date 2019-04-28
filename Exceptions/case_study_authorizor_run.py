import Exceptions.case_study_exceptions_auth as cse


class NotLoggedInError(cse.AuthException):
    pass

class Authorizor:

    def __init__(self, auth):
        self.auth = auth
        self.permissions = {}

    def add_permission(self, permission):

        try:
            perm_set = self.permissions[permission]
        except KeyError:
            self.permissions[permission] = set()
        else:
            PermissionError('Permission exists')


    def permit_user(self,username, permission):

        try:
            perm_set = self.permissions[permission]
        except KeyError:
            raise PermissionError("Permission does not exist")

        #this is called when there is no exception
        else:
            if username not in self.auth.users:
                raise cse.InvalidUsername(username)

    def check_permission(self,username, permission):

        if not self.auth.is_logged_in(username):
            raise NotLoggedInError(username)

        try:
            perm_set = self.permissions[permission]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            return permission in perm_set

    def __getitem__(self, item):
        return self.__dict__[item]


auth = cse.Authenticator()
auth.add_user('piotr','kumbaLagumba5')

autor = Authorizor(auth)

autor.add_permission('read_only')
autor.add_permission('read_only')

autor.permit_user('piotr','read_only')
#autor.check_permission('piotr','write')

auth.login('piotr','kumbaLagumba5')
autor.check_permission('piotr','read_only')

