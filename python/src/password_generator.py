import string
import random

from src.validations.validator import Validator


class PasswordGenerator:

    def __init__(self, capital_letters: bool = False, numbers: bool = False, symbols: bool = False) -> None:

        self.max_length = 16

        self.min_length = 8

        self.capital_letters = capital_letters

        self.numbers = numbers

        self.symbols = symbols

    def create(self):

        while True:

            password = self.generate_random_substring()

            if self.is_valid_password(password):

                return password

    def is_valid_password(self, password):
        return (
            len(password) >= self.min_length
            and len(password) <= self.max_length
            and (self.capital_letters and any(char.isupper() for char in password) or not self.capital_letters)
            and (self.numbers and any(char.isdigit() for char in password) or not self.numbers)
            and (self.symbols and any(char in string.punctuation for char in password) or not self.symbols)
        )

    def password_characters(self):

        characters = self.get_letters()

        if self.numbers:

            characters += self.get_numbers()

        if self.symbols:

            characters += self.get_symbols()

        return characters

    def generate_random_substring(self):

        substring = ''.join(random.choice(self.password_characters()) for _ in range(
            random.choice([self.min_length, self.max_length])))

        return substring

    def get_letters(self):

        return string.ascii_letters if self.capital_letters else string.ascii_lowercase

    def get_numbers(self):

        return string.digits

    def get_symbols(self):

        return string.punctuation
