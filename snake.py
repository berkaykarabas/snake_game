from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.segments = []
        self.crate_snake()
        self.head = self.segments[0]

    def crate_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self,position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.crate_snake()
        self.head = self.segments[0]
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)