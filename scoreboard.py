from turtle import Turtle
ALIGMENT = "center"
FONT = ('Courier', 24, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data_file:
            self.high_score = int(data_file.read())
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGMENT, font=FONT)

    def reset(self):
            if self.score > self.high_score:
                self.high_score = self.score
                with open("data.txt", mode="w") as data_file:
                    data_file.write(str(self.high_score))
            self.score = 0
            self.clear()
            self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()