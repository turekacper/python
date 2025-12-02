from getpass import getpass

class User: 
    def __init__(self, first_name, last_name, usr_login, password, job):
        self.last_name = last_name
        self.usr_login = usr_login
        self.first_name = first_name
        self.job = job
        self.password = password

        self.login_attempts = 0 

    def describe_user(self):
        print(f"the selected user {self.usr_login} has the job {self.job}")

    def greet_user(self):
        print(f"Hello {self.first_name}. Welcome to the board. It's nice we are working together")

    def increment_login_attempts(self):
        print(f"Login failed")
        self.login_attempts += 1

        print(self.login_attempts)
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"{self.usr_login} Your current login attempt has been reseted to {self.login_attempts}")

    def login(self):
        while True:
            val_pass = getpass("Give me the password: ")
            if val_pass == self.password:
                print(f"Congratulations {self.usr_login}. You've logged in.")
                self.reset_login_attempts()
                break
            else:
                self.increment_login_attempts()

                continue

new_user1 = User('kacper', 'turek', 'pi33966', 'haselko', 'devops')

new_user1.login()
