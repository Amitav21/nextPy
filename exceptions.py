import string

class UsernameContainsIllegalCharacter(Exception):

    """
    A class used to represent an UsernameContainsIllegalCharacter exception
    """

    """A constructor of the UsernameContainsIllegalCharacter class.
        :param username: The entered username.
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

    """
    A class used to represent an UsernameTooShort exception
    """

    """A constructor of the UsernameTooShort class.
        :param username: The entered username.
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

    """
    A class used to represent an UsernameTooLong exception
    """

    """A constructor of the UsernameTooLong class.
        :param username: The entered username.
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

    """
    A class used to represent a PasswordMissingCharacter exception
    """

    """A constructor of the PasswordMissingCharacter class.
        :param password: The entered password.
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

    """
    A class used to represent a PasswordTooShort exception
    """

    """A constructor of the PasswordTooShort class.
        :param password: The entered password.
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

    """
    A class used to represent a PasswordTooLong exception
    """

    """A constructor of the PasswordTooLong class.
        :param password: The entered password.
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

    """
    A class used to represent a PasswordMissingLower exception
    """

    """A method for describing the error.
        :return: None.
        :rtype: None.
        """
    def __str__(self):
        return super().__str__() + "(lower)"

class PasswordMissingUpper(PasswordMissingCharacter):

    """
    A class used to represent a PasswordMissingUpper exception
    """

    """A method for describing the error.
        :return: None.
        :rtype: None.
        """
    def __str__(self):
        return super().__str__() + "(upper)"

class PasswordMissingDigit(PasswordMissingCharacter):

    """
    A class used to represent a PasswordMissingDigit exception
    """

    """A method for describing the error.
        :return: None.
        :rtype: None.
        """
    def __str__(self):
        return super().__str__() + "(digit)"

class PasswordMissingSpeciel(PasswordMissingCharacter):

    """
    A class used to represent a PasswordMissingSpeciel exception
    """

    """A method for describing the error.
        :return: None.
        :rtype: None.
        """
    def __str__(self):
        return super().__str__() + "(special)"

"""Checks if given username and password are valid.
    :param username: the given username.
    :param password: the given password.
    :type username: str.
    :type password: str.
    :return: None.
    :rtype: None.
    :raise: UsernameTooShort: raises an Exception
    :raise: UsernameTooLong: raises an Exception
    :raise: UsernameContainsIllegalCharacter: raises an Exception
    :raise: PasswordTooShort: raises an Exception
    :raise: PasswordTooLong: raises an Exception
    :raise: PasswordMissingUpper: raises an Exception
    :raise: PasswordMissingLower: raises an Exception
    :raise: PasswordMissingDigit: raises an Exception
    :raise: PasswordMissingSpeciel: raises an Exception
    """
def check_input(username, password):
    try:
        # if the length of the username is shorter than 3 it's too short
        if len(username) < 3:
            raise UsernameTooShort(username)

        # if the length of the username is longer than 16 it's too long
        if len(username) > 16:
            raise  UsernameTooLong(username)

        # if the username contains a letter which isn't alphanumeric or '_' it's invalid
        for letter in username:
            if letter.isalnum() == False and letter != '_':
                raise UsernameContainsIllegalCharacter(username, letter)

        # if the length of the password is shorter than 8 it's too short
        if len(password) < 8 :
            raise PasswordTooShort(password)

        # if the length of the password is longer than 40 it's too long
        if len(password) > 40:
            raise PasswordTooLong(password)

        # checks if there is at least 1 character from each requirement

        # upper english letters
        upper_flag = any(char.isupper() for char in password)
        # lower english letters
        lower_flag = any(char.islower() for char in password)
        # digits
        digit_flag = any(char.isdigit() for char in password)
        # special characters
        punctuation_flag = any(char in string.punctuation for char in password)
        if not upper_flag:
            raise PasswordMissingUpper(password)
        if not lower_flag:
            raise PasswordMissingLower(password)
        if not digit_flag:
            raise PasswordMissingDigit(password)
        if not punctuation_flag:
            raise PasswordMissingSpeciel(password)

    # catch the exceptions
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

    # if there wasn't any exception, it means the username and password are valid
    else:
        print("OK")



if __name__ == '__main__':
    username = input("enter the username: ")
    password = input("enter the password: ")
    check_input(username, password)
