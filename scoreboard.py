from turtle import Turtle
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update()

    def update(self):
        self.goto(-270, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def calculate (self):
        self.level +=1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)




