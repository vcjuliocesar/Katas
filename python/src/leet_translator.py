from src.validations.validator import Validator


class LeetTranslator:

    @staticmethod
    def convert(text: str):

        result = ""

        Validator.isEmpty(text)

        for character in text:

            result += Dictionary.find_in_dictionary(character).strip()

        return result


class Dictionary:

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
    def find_in_dictionary(character: str):

        if character.isdigit():

            return Dictionary.__isNumber(character)

        if isinstance(character, str):

            return Dictionary.__isString(character)

    @staticmethod
    def __isNumber(param: int):

        numbers = Dictionary.DICTIONARY['numbers']

        number = int(param)

        if number in numbers.keys():

            return numbers[number]

    @staticmethod
    def __isString(param: str):

        alphabet = Dictionary.DICTIONARY['alphabet']

        uppercase = param.upper()

        if not uppercase in alphabet.keys():

            return param

        return alphabet[uppercase]