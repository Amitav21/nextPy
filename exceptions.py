import string

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"username {self.username} contains illegal characters"

class UsernameTooShort(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"username {self.username} is shorter than 3 characters"

class UsernameTooLong(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"username {self.username} is longer than 16 characters"

class PasswordMissingCharacter(Exception):
    def __init__(self, password):
        self.password = password

    def __str__(self):
        return f"password {self.password} is missing a required character"

class PasswordTooShort(Exception):
    def __init__(self, password):
        self.password = password

    def __str__(self):
        return f"password {self.password} is shorter than 8 characters"

class PasswordTooLong(Exception):
    def __init__(self, password):
        self.password = password

    def __str__(self):
        return f"password {self.password} is longer than 40 characters"


def check_input(username, password):
    try:
        if len(username) < 3:
            raise UsernameTooShort(username)
        if len(username) > 16:
            raise  UsernameTooLong(username)
        for letter in username:
            if letter.isalnum() == False and letter != '_':
                raise UsernameContainsIllegalCharacter(username)
        if len(password) < 8 :
            raise PasswordTooShort(password)
        if len(password) > 40:
            raise PasswordTooLong(password)
        upper_flag = any(char.isupper() for char in password)
        lower_flag = any(char.islower() for char in password)
        digit_flag = any(char.isdigit() for char in password)
        punctuation_flag = any(char in string.punctuation for char in password)
        if not upper_flag or not lower_flag or not digit_flag or not punctuation_flag:
            raise PasswordMissingCharacter(password)

    except UsernameTooShort as e:
        print(e.__str__())
    except UsernameTooLong as e:
       print(e.__str__())
    except UsernameContainsIllegalCharacter as e:
        print(e.__str__())
    except PasswordTooShort as e:
        print(e.__str__())
    except PasswordTooLong as e:
        print(e.__str__())
    except PasswordMissingCharacter as e:
        print(e.__str__())
    else:
        print("OK")



if __name__ == '__main__':
    username = input("enter the username: ")
    password = input("enter the password: ")
    check_input(username, password)
