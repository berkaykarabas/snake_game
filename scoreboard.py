from turtle import Turtle
FONT = ("Arial",14,"bold")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highest_score=int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.high_score = open("data.txt")
        set_y = 280
        self.goto(0,set_y)
        self.my_score()
        self.screen.tracer(0)
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highest_score} ",move=False,align="center",font=FONT)
    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", move=False, align="center", font=FONT)
    def my_score(self):
        self.update_scoreboard()
        self.score += 1


