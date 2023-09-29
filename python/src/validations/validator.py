from src.exceptions.invalid_value_error import InvalidValueError

class Validator: 
    
    @staticmethod
    def validate_number(number):
        
        if not isinstance(number,(int)):
            
            raise InvalidValueError(f'{number} is not a valid number')
    
