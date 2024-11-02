from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.score = 0
        self.high_score = self.retrieve_high_score()
        self.penup()
        self.goto(-75, 280)
        self.write(f"Score: {self.score}, High Score = {self.high_score}", font=('Courier', 10, 'normal'))

    def change_score(self):
        self.score += 1
        self.update_scoreboard()

    def retrieve_high_score(self):
        with open("data.txt") as file:
            return int(file.read())
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score = {self.high_score}", font=('Courier', 10, 'normal'))

    def game_over(self):
        self.goto(-45, 0)
        self.write("GAME OVER", font=('Courier', 15, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        with open("data.txt", mode='w') as file:
            file.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()
