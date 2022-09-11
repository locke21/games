from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.current_score = 0
        with open("data.txt") as file:
            self.highest_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color('green')
        self.goto(-165, 260)
        self.write(f'Current Score: {self.current_score}       --       '
                   f'Highest Score: {self.highest_score}', font=("ariel", 12, "bold"))

    def add_score(self):
        self.current_score += 1
        self.update_score()

    def game_over(self):
        self.current_score = 0
        self.update_score()

    def update_score(self):
        self.highest_score = self.current_score if self.current_score >= self.highest_score else self.highest_score
        with open("data.txt", "w") as change_score:
            change_score.write(str(self.highest_score))
        self.clear()
        self.write(f'Current Score: {self.current_score}       --       '
                   f'Highest Score: {self.highest_score}', font=("ariel", 12, "bold"))
