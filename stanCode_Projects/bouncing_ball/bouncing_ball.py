"""
File: bouncing_ball
Name: Ting-Yu
-------------------------
The user clicks the mouse to make the ball start bouncing. Each bounce reduces
y velocity to REDUCE of itself. After the ball exceeds the window 3 times,
the ball will return to the original position and remain stationary.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global Variable
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
switch = False
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global switch, count
    window.add(ball)
    onmouseclicked(star_bouncing)
    while True:
        if switch:  # Click the mouse and make ball start to bounce
            switch = False
            count += 1
            while ball.x is START_X:
                vy = GRAVITY
                while True:
                    ball.move(VX, vy)
                    vy += GRAVITY
                    # ball.y exceeds the window, the ball will bounce up
                    if ball.y >= 500:
                        vy = -vy
                        ball.move(VX, vy)
                        vy *= REDUCE
                    # The ball disappears after passing the right side of window
                    if ball.x >= 800:
                        window.remove(ball)
                        break
                    pause(DELAY)
                ball.x = START_X
                ball.y = START_Y
                window.add(ball)
                switch = False
                break
        pause(DELAY)


def star_bouncing(mouse):
    global switch, count
    if count < 3:
        switch = True


if __name__ == "__main__":
    main()
