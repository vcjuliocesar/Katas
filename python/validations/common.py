from exceptions.value_not_number_error import ValueNotNumberError 
    
def validate_number(number):
    
    if not isinstance(number,(int)):
        raise ValueNotNumberError(f'{number} is not a valid number')
    
