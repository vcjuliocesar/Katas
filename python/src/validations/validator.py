from src.exceptions.invalid_value_error import InvalidValueError


class Validator:

    @staticmethod
    def validate_number(number):

        if not isinstance(number, (int)):

            raise InvalidValueError(f'{number} is not a valid number')

    @staticmethod
    def isEmpty(param):

        if not param or len(param) < 1:

            raise InvalidValueError("empty value")

    @staticmethod
    def isValidList(lst, options):

        for item in lst:

            if item not in options:

                raise InvalidValueError(f"{item} is a valid option")

    @staticmethod
    def isValidLength(lst):

        if len(lst) <= 1:

            raise InvalidValueError(f"{len(lst)} is an invalid length")

    @staticmethod
    def max_length(param,length):
        
        if param > int(length):
            
            raise InvalidValueError(f"{param} is an invalid length")
        
    @staticmethod
    def min_length(param,length):
        
        if param < int(length):
            
            raise InvalidValueError(f"{param} is an invalid length")