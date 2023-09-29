import unittest
from src.exceptions.invalid_value_error import InvalidValueError
from src.leet import Leet

class TestLeer(unittest.TestCase):
    
    def test_it_returns_an_exception_if_value_is_empty(self) -> None:
        
        with self.assertRaises(InvalidValueError):
            
            param = ""
            
            Leet.convert(param)
    
    def test_it_returns_original_text_if_is_not_found_inside_leet_alphabet(self) -> None:
        
        self.assertEqual("@·$%&/ñÑ",Leet.convert("@·$%&/ñÑ"))
        
    
    def test_it_returns_text_in_leet_alphabet(self) -> None:
        
        self.assertEqual("#3|_|_0",Leet.convert("hello"))
    
        
    def test_it_returns_text_in_leet_numbers(self) -> None:
  
        self.assertEqual("LREA",Leet.convert("1234"))
        
    
    def test_it_returns_text_in_leet(self) -> None:
        
        self.assertEqual("|*j7#0^/E",Leet.convert("python3"))