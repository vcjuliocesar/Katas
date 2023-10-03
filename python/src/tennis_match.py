from src.validations.validator import Validator


class TennisMatch:

    def __init__(self, points: list) -> None:

        self.playes = ["P1", "P2"]

        self.scores = ["Love", "15", "30", "40"]

        self.points = points

        self.p1_points = 0

        self.p2_points = 0
        
        self.finished = False

    def score(self):

        Validator.isEmpty(self.points)

        Validator.isValidList(self.points, self.playes)

        Validator.isValidLength(self.points)

        result = ""

        for player in self.points:

            self.update_points(player)

            result += self.get_score()

        if self.finished:
            
            winner = f"Player P1 has won\n" if self.p1_points > self.p2_points else "Player P2 has won\n"

            result += winner

        return result

    def update_points(self, player: str):

        if player == "P1":
            self.p1_points += 1
        else:
            self.p2_points += 1

    def get_score(self):

        if self.p1_points >= 3 and self.p2_points >= 3:

            score_diff = abs(self.p1_points - self.p2_points)

            if not self.finished and score_diff <= 1:

                return f"Deuce\n" if self.p1_points == self.p2_points else "Advantage P1\n" if self.p1_points > self.p2_points else "Advantage P2\n"
            
            self.finished = True
        
        elif self.p1_points < 4 and self.p2_points < 4:

            return f"{self.scores[self.p1_points]} - {self.scores[self.p2_points]}\n"

        self.finished = True
        
        return ""
