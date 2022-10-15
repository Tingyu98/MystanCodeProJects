"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Provide a : class: "BreakoutGraphics" that supports the breakout game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10       # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 3        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    """
    set up several bricks on the upper part of the screen, a ball in the middle of screen at the beginning and paddle
    moves with the mouse at the bottom of the screen.
    """

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        onmousemoved(self.drag_mouse)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width-self.ball.width)/2, y=(window_height-self.ball.height)/2)

        #  Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        self.switch = True
        onmouseclicked(self.ball_drop)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i == 0 or i == 1:
                    self.brick.fill_color = "red"
                elif i == 2 or i == 3:
                    self.brick.fill_color = "orange"
                elif i == 4 or i == 5:
                    self.brick.fill_color = "yellow"
                elif i == 6 or i == 7:
                    self.brick.fill_color = "green"
                elif i == 8 or i == 9:
                    self.brick.fill_color = "blue"
                self.window.add(self.brick, x=j*(brick_width+brick_spacing), y=brick_offset+i*(brick_height +
                                                                                               brick_spacing))

    def drag_mouse(self, event):
        if 0 <= event.x-self.paddle.width/2 <= self.window.width-self.paddle.width:
            self.paddle.y = self.window.height-PADDLE_OFFSET
            self.paddle.x = event.x - self.paddle.width/2
        elif event.x-self.paddle.width/2 < 0:
            self.paddle.y = self.window.height - PADDLE_OFFSET
            self.paddle.x = 0
        else:
            self.paddle.y = self.window.height - PADDLE_OFFSET
            self.paddle.x = self.window.width-self.paddle.width

    def ball_drop(self, event):
        if self.__dx != 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.switch = False

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    @staticmethod
    def get_num_bricks():
        return BRICK_ROWS*BRICK_COLS

    def rebound_y(self):
        self.__dy = -self.__dy

    def rebound_x(self):
        self.__dx = -self.__dx







