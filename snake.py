from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
SNAKE_POS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_blocks = []
        self.create_snake()
        self.head = self.snake_blocks[0]

    def create_snake(self):
        # x_cor = 0
        for pos in SNAKE_POS:
            self.add_block(pos)
            # x_cor -= 20

    def reset_snake(self):
        for block in self.snake_blocks:
            block.goto(1000, 1000)
        self.snake_blocks.clear()
        self.create_snake()
        self.head = self.snake_blocks[0]

    def move(self):
        for block_num in range(len(self.snake_blocks)-1, 0, -1):
            new_x = self.snake_blocks[block_num - 1].xcor()
            new_y = self.snake_blocks[block_num - 1].ycor()
            self.snake_blocks[block_num].goto(x=new_x, y=new_y)

        self.head.forward(MOVE_DISTANCE)

    def add_block(self, pos):

        # x_cor = 0
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(x=pos[0], y=pos[1])
        # x_cor -= 20
        self.snake_blocks.append(snake)

    def extend(self):
        self.add_block(self.snake_blocks[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
