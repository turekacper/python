class User: 
    def __init__(self, first_name, last_name, login, job):
        User.last_name = last_name
        User.login = login
        User.first_name = first_name
        User.job = job

    def describe_user(self):
        print(f"the selected user {self.login} has the job {self.job}")


    def greet_user(self):
        print(f"Hello {self.first_name}. Welcome to the board. It's nice we are working together")


class Admin(User):

    def __init__(self, first_name, last_name, login, job):

        super().__init__(first_name, last_name, login, job)
        self.priviliges = ('insert', 'update', 'delete')

    def show_privileges(self):
        print(f"The priviliges of {self.first_name} {self.last_name} {self.login} are: ")

        for privilege in self.priviliges:
            print(privilege)

pi1212 = Admin('Robert', 'Respondek', 'pi1212', 'devops admin')

pi1212.show_privileges()
