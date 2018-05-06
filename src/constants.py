from blocks import *

# Game name
GAME_NAME = 'Dau cu tancu\' 6 5'
# how much the graphics should wait until going to the next step
TIMEOUT = 1
# how much it should wait after endgame until the window closes
TIME_UNTIL_WINDOW_CLOSE = 50

# more constants
WINDOW_BACKGROUND = 'black'

# grid constants
HEIGHT = 10
WIDTH = 10
BLOCK_SIZE = 50

# color constants
colors = {
    'RED': 'Red',
    'BLUE': 'Blue',
    'GREEN': 'Green',
    'PURPLE': 'Purple',
}

# type (ground, water)
block_type = {
    'GROUND': 'Ground',
    'WATER': 'Water',
}

# directions
directions = {
    'UP': 0,
    'RIGHT': 1,
    'DOWN': 2,
    'LEFT': 3,
}

# first grid (empty map)
EMPTY_GRID = [[Ground() for j in range(WIDTH)] for i in range(HEIGHT)]

EMPTY_GRID[2][1] = Water()
EMPTY_GRID[2][2] = Water()
EMPTY_GRID[2][3] = Water()
EMPTY_GRID[3][1] = Water()
EMPTY_GRID[3][2] = Water()
EMPTY_GRID[3][3] = Water()

EMPTY_GRID[7][8] = Water()
EMPTY_GRID[7][7] = Water()
EMPTY_GRID[7][6] = Water()
EMPTY_GRID[6][8] = Water()
EMPTY_GRID[6][7] = Water()
EMPTY_GRID[6][6] = Water()

EMPTY_GRID[3][6] = Obstacle()
EMPTY_GRID[6][3] = Obstacle()
#  EMPTY_GRID[1][5] = Tank(colors['BLUE'])
#  EMPTY_GRID[8][5] = Tank(colors['RED'])
#  EMPTY_GRID[2][3] = Tank(colors['PURPLE'])
#  EMPTY_GRID[7][3] = Tank(colors['GREEN'])
#  EMPTY_GRID[5][3] = Projectile(block_type['GROUND'])
