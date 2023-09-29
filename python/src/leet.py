from src.validations.validator import Validator


class Leet:

    DICTIONARY = {
        "alphabet": {
            "A": "4",
            "B": "I3",
            "C": "[",
            "D": ")",
            "E": "3",
            "F": "|=",
            "G": "&",
            "H": "#",
            "I": "1",
            "J": ",_|",
            "K": ">|",
            "L": "|_",
            "M": "/\/\\",
            "N": "^/",
            "O": "0",
            "P": "|*",
            "Q": "(_,)",
            "R": "I2",
            "S": "5",
            "T": "7",
            "U": "(_)",
            "V": "\/",
            "W": "\/\/",
            "X": "><",
            "Y": "j",
            "Z": "2"
        },
        "numbers": {
            1: "L",
            2: "R",
            3: "E",
            4: "A",
            5: "S",
            6: "b",
            7: "T",
            8: "B",
            9: "g",
            0: "o",
        }
    }

    @staticmethod
    def convert(text: str):

        result = ""

        Validator.validate_empty_value(text)

        for character in text:

            result += Leet.__find_in_dictionary(character).strip()

        return result

    @staticmethod
    def __find_in_dictionary(character: str):

        if character.isdigit():

            return Leet.__isNumber(character)

        if isinstance(character, str):

            return Leet.__isString(character)

    @staticmethod
    def __isNumber(param: int):

        numbers = Leet.DICTIONARY['numbers']

        number = int(param)

        if number in numbers.keys():

            return numbers[number]

    @staticmethod
    def __isString(param: str):

        alphabet = Leet.DICTIONARY['alphabet']

        uppercase = param.upper()

        if not uppercase in alphabet.keys():

            return param

        return alphabet[uppercase]
