from IPONG import Pong


class playWithFriend(Pong):
    def play(self):
        """Keyboard Binding"""
        # Moving PaddleA
        self.wn.listen()
        self.wn.onkeypress(self.paddle_a_up, "w")
        self.wn.onkeypress(self.paddle_a_down, "s")
        # Moving Paddle B
        self.wn.onkeypress(self.paddle_b_up, "Up")
        self.wn.onkeypress(self.paddle_b_down, "Down")
        while True:
            self.wn.update()

            # Moving our ball
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            """Defining Horizontal Borders"""
            # 1st and 2nd Quadrants
            if self.ball.ycor() > 250:
                self.ball.sety(250)
                self.ball.dy *= -1
            # 3rd and 4th Quadrant
            elif self.ball.ycor() < -250:
                self.ball.sety(-250)
                self.ball.dy *= -1

            """Defining Vertical Borders"""
            # right-hand side
            if self.ball.xcor() > 390:
                self.ball.goto(0, 0)
                self.ball.dx *= -1
                self.player_a_score += 1
                self.pen.clear()
                self.pen.write("Player A: {} Player B: {} ".format(self.player_a_score, self.player_b_score), align="center",
                          font=("Courier", 14, "bold"))

            # Left-Hand Side
            elif self.ball.xcor() < -390:
                self.ball.goto(0, 0)
                self.ball.dx *= -1
                self.player_b_score += 1
                self.pen.clear()
                self.pen.write("Player A: {} Player B: {} ".format(self.player_a_score, self.player_b_score), align="center",
                          font=("Courier", 14, "bold"))

            """Defining Ball collisions with our paddles"""
            # Paddle B
            if (self.ball.xcor() > 360 and self.ball.xcor() < 370 and (
                    self.ball.ycor() < self.paddle_b.ycor() + 50 and self.ball.ycor() > self.paddle_b.ycor() - 50)):
                self.ball.setx(360)
                self.ball.dx *= -1

            # Paddle A
            if (self.ball.xcor() < -360 and self.ball.xcor() > -370 and (
                    self.ball.ycor() < self.paddle_a.ycor() + 50 and self.ball.ycor() > self.paddle_a.ycor() - 50)):
                self.ball.setx(-360)
                self.ball.dx *= -1

