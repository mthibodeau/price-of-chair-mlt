class UserError(Exception):
    def __init__(self, message):
        self.message = message

class UserNotExistsError(UserError):
    pass

class PasswordIncorrectError(UserError):
    pass

class UserExistsAlreadyError(UserError):
    pass

class InvalidEmailError(UserError):
    pass