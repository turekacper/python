class User:
    def __init__(self, first_name, last_name, login, job):
        self.last_name = last_name
        self.login = login
        self.first_name = first_name
        self.job = job

    def describe_user(self):
        print(f"the selected user {self.login} has the job {self.job}")

    def greet_user(self):
        print(
            f"Hello {self.first_name}. Welcome to the board. It's nice we are working together"
        )
