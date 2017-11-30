from passlib.hash import pbkdf2_sha512
import re

class Utils(object):

    @staticmethod
    def hash_password(password):
        """
        Hashes a password using pbkdf2_sha512
        :param password: sha512 password from login/register form
        :return: a sha512->pbkdf2_sha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(password)


    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        checks that the password user sent matches the database
        The database password is encrypted more than user's at this point
        :param password: sha512-hashed password
        :param hashed_password: pbkf2_sha512 password
        :return: True if passwords match otherwise False
        """
        return pbkdf2_sha512.verify(password, hashed_password)

    @staticmethod
    def email_is_valid(email):
        email_address_matcher = re.compile('^[\w-]+@([\w-]+\.)[\w]+$')
        return True if email_address_matcher.match(email) else False