from turtle import Turtle
FONT = ("Courier", 14, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.game_level = 1
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.display_game_level()

    def display_game_level(self):
        self.clear()
        self.write(f"Level {self.game_level}", align=ALIGNMENT, font=FONT)

    def increase_game_level(self):
        self.game_level += 1
        self.display_game_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
