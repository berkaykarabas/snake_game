from turtle import Turtle
FONT = ("Arial",14,"bold")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        set_y = 280
        self.goto(0,set_y)
        self.my_score()
        self.screen.tracer(0)
    def update_scoreboard(self):
        self.write(f"Score: {self.score} ",move=False,align="center",font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", move=False, align="center", font=FONT)
    def my_score(self):
        self.clear()
        self.update_scoreboard()
        self.score += 1


