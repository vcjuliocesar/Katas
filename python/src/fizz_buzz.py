from src.validations.validator import Validator


class FizzBuzz:
    
    @staticmethod
    def convert(number:int):
        
        result = ''
        
        Validator.validate_number(number)
        
        if number % 3 == 0 :
            
            result += 'fizz'
        
        if number % 5 == 0 :
        
            result += 'buzz'
        
        return result or number
