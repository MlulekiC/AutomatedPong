import turtle

#answer = input("Play with friend or pc?: ")

class Pong():
    """
    Code to implement our pong screen
    """
    wn = turtle.Screen()
    wn.title("PONG")
    wn.bgcolor("brown")
    wn.setup(width=800, height=500)
    wn.tracer(0)

    """"Paddle A"""
    paddle_a = turtle.Turtle()
    paddle_a.penup()
    paddle_a.shape("square")
    paddle_a.color("black")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.goto(-370, 0)
    player_a_score = 0

    """"Paddle B"""
    paddle_b = turtle.Turtle()
    paddle_b.penup()
    paddle_b.color("black")
    paddle_b.shape("square")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.goto(370, 0)
    player_b_score = 0

    """Ball"""
    ball = turtle.Turtle()
    ball.penup()
    ball.color("blue")
    ball.shape("circle")
    ball.goto(0, 0)

    """Pen"""
    pen = turtle.Turtle()
    pen.penup()
    pen.color("white")
    pen.hideturtle()
    pen.goto(0, 230)
    pen.write("Player A: 0 Player B: 0 ", align="center", font=("Courier", 14, "bold"))

    # Change in both x and y coordinates
    ball.dx = -0.5
    ball.dy = 0.5

    """Defining methods to move the paddles"""

    def paddle_a_up(self):
        y = self.paddle_a.ycor()
        y += 20
        y = self.paddle_a.sety(y)

    def paddle_a_down(self):
        y = self.paddle_a.ycor()
        y -= 20
        y = self.paddle_a.sety(y)

    def paddle_b_up(self):
        y = self.paddle_b.ycor()
        y += 20
        y = self.paddle_b.sety(y)

    def paddle_b_down(self):
        y = self.paddle_b.ycor()
        y -= 20
        y = self.paddle_b.sety(y)

    def play(self):
        pass