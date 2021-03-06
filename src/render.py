import sys
sys.path.append('..')
import time
import random
from third_party import graphics
from logger import Logger
import constants
from constants import *
from blocks import *


class RenderBlock:
    @staticmethod
    def build_point(i, j):
        p1 = graphics.Point((j + 0.5) * BLOCK_SIZE, (i + 0.5) * BLOCK_SIZE)
        return p1

    @staticmethod
    def ground(win, i, j, block):
        point = RenderBlock.build_point(i, j)
        image = graphics.Image(point, '../resources/img/Ground.gif')
        image.draw(win)

    @staticmethod
    def water(win, i, j, block):
        point = RenderBlock.build_point(i, j)
        image = graphics.Image(point, '../resources/img/Water.gif')
        image.draw(win)

    @staticmethod
    def obstacle(win, i, j, block):
        point = RenderBlock.build_point(i, j)
        image = graphics.Image(point, '../resources/img/Obstacle.gif')
        image.draw(win)

    @staticmethod
    def tank(win, i, j, block):
        point = RenderBlock.build_point(i, j)
        tank_name = 'Tank' + block.color
        image = graphics.Image(point, '../resources/img/{}.gif'.format(tank_name))
        image.draw(win)

    @staticmethod
    def projectile(win, i, j, block):
        point = RenderBlock.build_point(i, j)
        block_name = 'Projectile' + block.block_type
        image = graphics.Image(point, '../resources/img/{}.gif'.format(block_name))
        image.draw(win)


class Render:
    def __init__(self):
        self.win = graphics.GraphWin(constants.GAME_NAME, HEIGHT * BLOCK_SIZE, WIDTH * BLOCK_SIZE, autoflush=False)
        self.win.setBackground(constants.WINDOW_BACKGROUND)

    def __del__(self):
        time.sleep(AT_ENDGAME_TIME_UNTIL_WINDOW_CLOSE)

    @staticmethod
    def draw_grid(win, grid):
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if type(grid[i][j]) is Ground:
                    RenderBlock.ground(win, i, j, grid[i][j]);
                elif type(grid[i][j]) is Water:
                    RenderBlock.water(win, i, j, grid[i][j]);
                elif type(grid[i][j]) is Obstacle:
                    RenderBlock.obstacle(win, i, j, grid[i][j]);
                elif type(grid[i][j]) is Tank:
                    RenderBlock.tank(win, i, j, grid[i][j]);
                elif type(grid[i][j]) is Projectile:
                    RenderBlock.projectile(win, i, j, grid[i][j]);
        graphics.update()

    def render(self, grids):
        for grid in grids:
            self.draw_grid(self.win, grid)
            time.sleep(TIMEOUT)


render = Render()

if __name__ == '__main__':
    pass