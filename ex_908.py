class User: 
    def __init__(self, first_name, last_name, login, job):
        self.last_name = last_name
        self.login = login
        self.first_name = first_name
        self.job = job

    def describe_user(self):
        print(f"the selected user {self.login} has the job {self.job}")


    def greet_user(self):
        print(f"Hello {self.first_name}. Welcome to the board. It's nice we are working together")


class Admin(User):

    def __init__(self, first_name, last_name, login, job):
        super().__init__(first_name, last_name, login, job)
        self.priviliges = Priviliges()
class Priviliges:


    def __init__(self):
        self.priviliges = ('insert', 'update', 'delete')
    def show_privileges(self, user):

        print(f"The priviliges of {user.first_name} {user.last_name} {user.login} are: ")

        for privilege in self.priviliges:
            print(privilege)

user1 = Admin('kapi', 'turek', 'pi33966', 'devops')
user1.priviliges.show_privileges(user1)
