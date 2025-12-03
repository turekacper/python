from user import User


class Admin(User):
    def __init__(self, first_name, last_name, login, job):
        super().__init__(first_name, last_name, login, job)
        self.priviliges = Priviliges()


class Priviliges:
    def __init__(self):
        self.priviliges = ("insert", "update", "delete")

    def show_privileges(self, user):
        print(
            f"The priviliges of {user.first_name} {user.last_name} {user.login} are: "
        )
        for privilege in self.priviliges:
            print(privilege)
