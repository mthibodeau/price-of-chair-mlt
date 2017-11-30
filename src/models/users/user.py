import uuid
from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors
from src.models.alerts.alert import Alert
import src.models.users.constants as UserConstants

class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}".format(self.email)

    def is_login_valid(email, password):
        """
        Method verifies that an email/password combo is valid or no. 
        Checks that email exists, and password associated with email is correct.
        :param email: user's email
        :param password: a sha 512 hashed password
        :return: True if valid, False
        """
        user_data = Database.find_one("users", {"email": email})  # password in sha512 -> pbkdf2_sha512
        if user_data is None:
            # tells user that email doesn't exist
            raise UserErrors.UserNotExistsError("Your email does not exist.")


        if not Utils.check_hashed_password(password, user_data['password']):
            # tells user that their password doesn't match
            raise UserErrors.PasswordIncorrectError("Your password is incorrect.")

        return True

    @staticmethod
    def register_user(email, password):
        """
        Registers a user with email and password. 
        :param email: user's email (might be invalid)
        :param password: sha512-hashed password
        :return: True if registered sucessfully, or False otherwise (exceptions can be raised)
        """

        user_data = Database.find_one("users", {"email": email})
        print(user_data)

        if user_data is not None:
            raise UserErrors.UserExistsAlreadyError("There is already a user with that email")

        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError('This email is not a valid format')

        User(email, Utils.hash_password(password)).save_to_db()

        return True


    def save_to_db(self):
        Database.insert("users", self.json())

    def json(self):
        return {"_id": self._id,
                "email": self.email,
                "password": self.password}

    @classmethod
    def find_by_email(cls, email):
        return cls(**Database.find_one(UserConstants.COLLECTION, {'email': email}))

    def get_alerts(self):
        return Alert.find_by_user_email(self.email)