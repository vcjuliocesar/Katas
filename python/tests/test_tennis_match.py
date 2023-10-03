import unittest
from src.exceptions.invalid_value_error import InvalidValueError
from src.tennis_match import TennisMatch


class TestTennisMatch(unittest.TestCase):

    def test_it_returns_an_exception_if_the_sequence_is_empty(self) -> None:

        with self.assertRaises(InvalidValueError):
            
            match = TennisMatch([])
            
            match.score()
    
    def test_it_returns_an_exception_if_the_sequence_item_is_invalid(self) -> None:
        
        with self.assertRaises(InvalidValueError):
            
            match = TennisMatch(["P","P4"])
            
            match.score()
            
    def test_it_returns_an_exception_if_the_sequence_is_less_than_2(self) -> None:
        
        with self.assertRaises(InvalidValueError):
            
            match = TennisMatch(["P1"])
            
            match.score()
            
    def test_it_retuens_score_game(self) -> None:
        
        score = "15 - Love\n30 - Love\n30 - 15\n30 - 30\n40 - 30\nDeuce\nAdvantage P1\nPlayer P1 has won\n"
        
        match = TennisMatch(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])
        
        self.assertEqual(score,match.score());