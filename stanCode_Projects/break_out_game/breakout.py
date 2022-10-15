"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program executes breakout game. If the user click the
mouse for the 1st time each round, the game starts. If the
ball falls to the ground, lives deducts one. The game will
end if there is no more lives or bricks.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel


FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    after click the mouse, ball drops and bounces back and forth between the bricks, walls and paddle above the screen,
    when the ball hits the bricks, the bricks will disappear.
    """

    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    num_bricks = graphics.get_num_bricks()
    clear_bricks = 0
    lives_label = GLabel("lives: "+str(lives))
    lives_label.font = "-20"
    graphics.window.add(lives_label, x=5, y=graphics.window.height)
    while True:
        if not graphics.switch:
            vx = graphics.get_vx()
            vy = graphics.get_vy()
            graphics.ball.move(vx, vy)
            if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width-graphics.ball.width:
                graphics.rebound_x()
            if graphics.ball.y <= graphics.ball.height:
                graphics.rebound_y()
            if graphics.ball.y >= graphics.window.height-graphics.ball.height:
                graphics.ball.x = (graphics.window.width-graphics.ball.width)/2
                graphics.ball.y = (graphics.window.height-graphics.ball.height)/2
                graphics.switch = True
                lives -= 1
                lives_label.text = "lives: " + str(lives)
                if lives == 0:
                    label = GLabel("GAME OVER")
                    label.font = "-40"
                    graphics.window.add(label, x=(graphics.window.width-label.width)/2, y=50)
                    break
            obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            obj2 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
            obj3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
            obj4 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y+graphics.ball.height)
            if obj1 is not None:
                if obj1 is not graphics.paddle and obj1 is not lives_label:
                    graphics.window.remove(obj1)
                    clear_bricks += 1
                    graphics.rebound_y()
                else:
                    if obj1 is graphics.paddle and vy > 0:
                        graphics.rebound_y()
            elif obj2 is not None:
                if obj2 is not graphics.paddle and obj2 is not lives_label:
                    graphics.window.remove(obj2)
                    clear_bricks += 1
                    graphics.rebound_y()
                else:
                    if obj2 is graphics.paddle and vy > 0:
                        graphics.rebound_y()
            elif obj3 is not None:
                if obj3 is not graphics.paddle and obj3 is not lives_label:
                    graphics.window.remove(obj3)
                    clear_bricks += 1
                    graphics.rebound_y()
                else:
                    if obj3 is graphics.paddle and vy > 0:
                        graphics.rebound_y()
            elif obj4 is not None:
                if obj4 is not graphics.paddle and not lives_label:
                    graphics.window.remove(obj4)
                    clear_bricks += 1
                    graphics.rebound_y()
                else:
                    if obj4 is graphics.paddle and vy > 0:
                        graphics.rebound_y()
            if clear_bricks == num_bricks:
                label = GLabel("YOU WIN!")
                label.font = "-40"
                graphics.window.add(label, x=(graphics.window.width-label.width)/2, y=50)
                break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
