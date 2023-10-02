from src.validations.validator import Validator


class TennisMatch:

    def __init__(self, points: list) -> None:

        self.scores = ["Love", "15", "30", "40", "Deuce"]
        self.points = points
        self.p1_points = 0
        self.p2_points = 0

    def score(self):

        Validator.isEmpty(self.points)

        # Validator.isValidList(self.points,self.options)

        Validator.isValidLength(self.points)
        
        result = ""
        
        for player in self.points:
            
             self.p1_points += 1 if player == "P1" else 0
             
             self.p2_points += 1 if player == "P2" else 0
              
             if self.p1_points < 5 and self.p2_points < 5:
                 
                 result += f"{self.scores[self.p1_points]} - {self.scores[self.p2_points]}\n"
              
        
        return result