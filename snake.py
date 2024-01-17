from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.direction = 360
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            s = Turtle(shape='square')
            s.color('White')
            s.penup()
            s.goto(position)
            self.snake_segments.append(s)


    def reset(self):
        for segment in self.snake_segments:
            segment.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]
        self.direction = 360

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.direction == 270:
            self.head.right(90)
            self.direction = 180

        else:
            self.head.left(90)
            self.direction = (self.direction + 90) % 360

    def right(self):
        if self.direction == 270:
            self.head.left(90)
            self.direction = 360
        else:
            self.head.right(90)
            self.direction = (self.direction - 90) % 360

    def up(self):
        if self.direction == 90 or self.direction == 270:
            pass
        elif self.direction == 180:
            self.right()
            self.direction = 90
        else:
            self.left()
            self.direction = 90

    def down(self):
        if self.direction == 90 or self.direction == 270:
            pass
        elif self.direction == 180:
            self.left()
            self.direction = 270
        else:
            self.right()
            self.direction = 270

    def increase_tail(self):

        xcor = self.snake_segments[-1].xcor()
        ycor = self.snake_segments[-1].ycor()
        s = Turtle(shape='square')
        s.color('White')
        s.penup()
        s.goto(xcor, ycor)
        self.snake_segments.append(s)
