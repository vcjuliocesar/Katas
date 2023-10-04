import unittest
import string
from src.exceptions.invalid_value_error import InvalidValueError 
from src.password_generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    
    def test_it_returns_min_length_or_max_lenhth_password(self):
         
        min_length = 8
        max_length = 16
         
        generator = PasswordGenerator()    
        password = generator.create()
        
        if len(password) == min_length:
                 
            self.assertLessEqual(len(password),min_length)
        
        else:
        
            self.assertGreaterEqual(len(password),max_length)
       
                
    def test_it_returns_password_with_capital_letters(self):
        
        generator = PasswordGenerator(capital_letters=True)
        
        password = generator.create()
        
        self.assertTrue(any(c.isupper() for c in password))
        
    def test_it_returns_password_without_capital_letters(self):
        
        generator = PasswordGenerator(capital_letters=False)
        
        password = generator.create()
        
        self.assertFalse(any(c.isupper() for c in password))
        
    def test_it_returns_password_with_numbers(self):
        
        generator = PasswordGenerator(numbers=True)
        
        password = generator.create()
        
        self.assertTrue(any(c.isdigit() for c in password))
    
    def test_it_returns_password_without_numbers(self):
        
        generator = PasswordGenerator(numbers=False)
        
        password = generator.create()
        
        self.assertFalse(any(c.isdigit() for c in password))
        
    def test_it_returns_password_with_symbols(self):
        
        generator = PasswordGenerator(numbers=False,symbols=True)
        
        password = generator.create()
        
        self.assertTrue(any(elm in string.punctuation for elm in password))
        
    def test_it_returns_password_without_symbols(self):
        
        generator = PasswordGenerator(numbers=False,symbols=False)
        
        password = generator.create()
        
        self.assertFalse(any(elm in string.punctuation for elm in password))
    
    def test_it_returns_password_with_all(self):
        
        generator = PasswordGenerator(capital_letters=True,numbers=True,symbols=True)
        
        password = generator.create()
        
        self.assertTrue(any(c.isupper() for c in password))
        
        self.assertTrue(any(c.isdigit() for c in password))
        
        self.assertTrue(any(elm in string.punctuation for elm in password))