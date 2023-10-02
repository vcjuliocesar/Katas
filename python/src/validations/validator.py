from src.exceptions.invalid_value_error import InvalidValueError

class Validator: 
    
    @staticmethod
    def validate_number(number):
        
        if not isinstance(number,(int)):
            
            raise InvalidValueError(f'{number} is not a valid number')
    
    @staticmethod   
    def isEmpty(param):
        
        if not param or len(param) < 1:
            
            raise InvalidValueError("empty value")
    
