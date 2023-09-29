import unittest

from src.fizz_buzz import FizzBuzz

from src.exceptions.value_not_number_error import ValueNotNumberError

class TestFizzBuzz(unittest.TestCase):
    
    def test_it_return_an_exception_if_the_parameter_is_not_a_number(self) -> None:
         
        with self.assertRaises(ValueNotNumberError):
            
            FizzBuzz.convert("abc")
    
    def test_it_return_fizz_for_multiples_of_three(self) -> None:
        
        for number in [3,6,9,12]:
            
            self.assertEqual('fizz',FizzBuzz.convert(number))
            
    def test_it_return_buzz_for_multiples_of_five(self) -> None:
  
        for number in [5,10,20,25]:
      
            self.assertEqual('buzz',FizzBuzz.convert(number))
    
    def test_it_return_fizzbuzz_for_multiples_of_three_and_five(self) -> None:
  
        for number in [15,30,45,60]:
      
            self.assertEqual('fizzbuzz',FizzBuzz.convert(number))
            
    def test_it_return_the_number_if_not_divisible_by_three_or_five(self) -> None:

      for number in [1,2,4,7,8,11]:
    
          self.assertEqual(number,FizzBuzz.convert(number))  
        
if __name__ == "__main__":
    
    unittest.main()