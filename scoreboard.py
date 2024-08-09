from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.initial_score = 0
        with open("/Users/shivanshshukla/Desktop/Coding/Learning Materials/Udemy/100 days of code/Day 20, 21/Snake Game/data.txt") as data:
            self.high_score = int(data.read())
        self.display_score()

    def update_score(self):
        self.initial_score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.initial_score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.initial_score > self.high_score:
            self.high_score = self.initial_score

            with open("/Users/shivanshshukla/Desktop/Coding/Learning Materials/Udemy/100 days of code/Day 20, 21/Snake Game/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.initial_score = 0
        self.display_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     # self.clear()
    #     self.write("GAME OVER", align=ALIGN, font=FONT)