class FizzBuzz:
    
    @staticmethod
    def convert(number:int):
        
        result = ''
        
        if number % 3 == 0 :
            
            result += 'fizz'
            
        if number % 5 == 0 :
            
            result += 'buzz'
        
        return result if result != '' else number