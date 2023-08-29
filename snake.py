from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.starting_x = 0
        self.starting_y = 0
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Initializes the first three segments of the snake"""
        for segment in range(0, 3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=self.starting_x, y=self.starting_y)
            self.starting_x -= 20
            self.segments.append(new_segment)

    def move(self):
        """Moves all segments to follow the head"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        # self.segments[0].left(90)

    def up(self):
        """Turns the head of the snake north"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turns the head of the snake south"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turns head of the snake east"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turns head of the snake west"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        """Add a new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def add_segment(self, segment):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        # new_segment.goto(x=self.starting_x, y=self.starting_y)
        # self.starting_x -= 20
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
