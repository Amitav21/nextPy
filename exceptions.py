import string

class UsernameContainsIllegalCharacter(Exception):

    """A constructor of the UsernameContainsIllegalCharacter class.
    :param username: The username entered.
    :param illegal_char: The illegal character in the name.
    :type username: str.
    :type illegal_char: char.
    :return: None.
    :rtype: None.
    """
    def __init__(self, username, illegal_char):
        self.username = username
        self.illegal_char = illegal_char

    """A method for describing the error.
    :return: None.
    :rtype: None.
    """
    def __str__(self):
        return f"username {self.username} contains an illegal char \"{self.illegal_char}\" at index {username.find(self.illegal_char)}"

class UsernameTooShort(Exception):
    """A constructor of the UsernameTooShort class.
    :param username: The username entered.
    :type username: str.
    :return: None.
    :rtype: None.
    """
    def __init__(self, username):
        self.username = username

    """A method for describing the error.
    :return: None.
    :rtype: None.
    """
    def __str__(self):
        return f"username {self.username} is shorter than 3 characters"

class UsernameTooLong(Exception):
    """A constructor of the UsernameTooLong class.
    :param username: The username entered.
    :type username: str.
    :return: None.
    :rtype: None.
    """
    def __init__(self, username):
        self.username = username

    """A method for describing the error.
    :return: None.
    :rtype: None.
    """
    def __str__(self):
        return f"username {self.username} is longer than 16 characters"

class PasswordMissingCharacter(Exception):
    """A constructor of the PasswordMissingCharacter class.
    :param password: The password entered.
    :type password: str.
    :return: None.
    :rtype: None.
    """
    def __init__(self, password):
        self.password = password

    """A method for describing the error.
    :return: None.
    :rtype: None.
    """
    def __str__(self):
        return f"password {self.password} is missing a required character"

class PasswordTooShort(Exception):
    """A constructor of the PasswordTooShort class.
    :param password: The password entered.
    :type password: str.
    :return: None.
    :rtype: None.
    """
    def __init__(self, password):
        self.password = password

    """A method for describing the error.
    :return: None.
    :rtype: None.
    """
    def __str__(self):
        return f"password {self.password} is shorter than 8 characters"

class PasswordTooLong(Exception):
    """A constructor of the PasswordTooLong class.
    :param password: The password entered.
    :type password: str.
    :return: None.
    :rtype: None.
    """
    def __init__(self, password):
        self.password = password

    """A method for describing the error.
    :return: None.
    :rtype: None.
    """
    def __str__(self):
        return f"password {self.password} is longer than 40 characters"

class PasswordMissingLower(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(lower)"

class PasswordMissingUpper(PasswordMissingCharacter):
    """A method for describing the error.
    :return: None.
    :rtype: None.
    """
    def __str__(self):
        return super().__str__() + "(upper)"

class PasswordMissingDigit(PasswordMissingCharacter):
    """A method for describing the error.
    :return: None.
    :rtype: None.
    """
    def __str__(self):
        return super().__str__() + "(digit)"

class PasswordMissingSpeciel(PasswordMissingCharacter):
    """A method for describing the error.
    :return: None.
    :rtype: None.
    """
    def __str__(self):
        return super().__str__() + "(special)"


def check_input(username, password):
    try:
        if len(username) < 3:
            raise UsernameTooShort(username)
        if len(username) > 16:
            raise  UsernameTooLong(username)
        for letter in username:
            if letter.isalnum() == False and letter != '_':
                raise UsernameContainsIllegalCharacter(username, letter)
        if len(password) < 8 :
            raise PasswordTooShort(password)
        if len(password) > 40:
            raise PasswordTooLong(password)
        upper_flag = any(char.isupper() for char in password)
        lower_flag = any(char.islower() for char in password)
        digit_flag = any(char.isdigit() for char in password)
        punctuation_flag = any(char in string.punctuation for char in password)
        if not upper_flag:
            raise PasswordMissingUpper(password)
        if not lower_flag:
            raise PasswordMissingLower(password)
        if not digit_flag:
            raise PasswordMissingDigit(password)
        if not punctuation_flag:
            raise PasswordMissingSpeciel(password)

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
