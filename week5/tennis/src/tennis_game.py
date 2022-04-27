class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.draw()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.winning()
        else:
            return self.format_score()

    def draw(self):
        score = ["Love-All", "Fifteen-All", "Thirty-All", "Forty-All"]
        return score[self.player1_score] if self.player1_score <= 3 else "Deuce"


    def winning(self):
        scores = {
            1: "Advantage player1",
            2: "Win for player1",
            -1: "Advantage player2",
            -2: "Win for player2"
        }
        minus_result = min(self.player1_score - self. player2_score, 2)
        return scores[minus_result]

    def format_score(self):
        scores = ["Love", "Fifteen", "Thirty", "Forty"]
        return scores[self.player1_score] + "-" + scores[self.player2_score]
