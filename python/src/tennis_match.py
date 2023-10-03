from src.validations.validator import Validator


class TennisMatch:

    def __init__(self, points: list) -> None:

        self.playes = ["P1", "P2"]

        self.scores = ["Love", "15", "30", "40"]

        self.points = points

        self.p1_points = 0

        self.p2_points = 0

    def score(self):

        Validator.isEmpty(self.points)

        Validator.isValidList(self.points, self.playes)

        Validator.isValidLength(self.points)

        result = ""

        for player in self.points:

            self.p1_points += 1 if player == "P1" else 0

            self.p2_points += 1 if player == "P2" else 0

            if self.p1_points >= 3 and self.p2_points >= 3:

                if abs(self.p1_points - self.p2_points) <= 1:

                    result += f"Deuce\n" if self.p1_points == self.p2_points else "Advantage P1\n" if self.p1_points > self.p2_points else "Advantage P2\n"

            elif self.p1_points < 4 and self.p2_points < 4:

                result += f"{self.scores[self.p1_points]} - {self.scores[self.p2_points]}\n"

        result += f"Player P1 has won\n" if self.p1_points > self.p2_points else "Player P2 has won\n"
        return result
