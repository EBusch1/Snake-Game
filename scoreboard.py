from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Comic Sans MS', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.score = 0
        # with open("data.txt") as file:
        with open("data.txt") as data:
            self.high_score = int(data.read())
        # self.high_score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Clears current scoreboard and iterates score and reprints"""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """is called when snake dies. Updates high score and resets score"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    #def game_over(self):
        # self.goto(0, 0)
        # self.write("GAME OVER.", False, align=ALIGNMENT, font=FONT)
