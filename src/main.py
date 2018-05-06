from controller import Controller
from logger import Logger
from render import *
import constants


# just some init things I'm doing now for the architecture demo
# don't take this crappy code too serious
grid = constants.EMPTY_GRID
player1 = {
    'player_id': 1,
    'coordinates': {
        'x': 8,
        'y': 2,
    },
    'color': constants.colors['RED'],
}
player2 = {
    'player_id': 2,
    'coordinates': {
        'x': 1,
        'y': 7,
    },
    'color': constants.colors['BLUE'],
}
grid[player1['coordinates']['x']][player1['coordinates']['y']] = Tank(player1['color'])
grid[player2['coordinates']['x']][player2['coordinates']['y']] = Tank(player2['color'])
# okay the crappy init code is over here, we will probably do another config
# file for this, but for now it looks ok just the way it is right here


# now define the two players controllers
controller = []
controller.append(
    Controller(
        player1['player_id'],
        player1['coordinates'],
        player1['color']))
controller.append(
    Controller(
        player2['player_id'],
        player2['coordinates'],
        player2['color']))


# each player will have a function, so let's hardcode those for now
def player1_function(controller):
    Logger.log(controller.get_my_tank_coordinates())

def player2_function(controller):
    Logger.log(controller.get_my_tank_coordinates())


# now let's play
if __name__ == '__main__':
    render([grid])
    game_over = False
    while game_over == False:
        # note that it's very important to update the grid each time before calling player_function.
        # if not, the player wouldn't know the latest configuration of the grid
        Logger.log('A new move is occuring')
        controller[0].update_grid(grid)
        player1_function(controller[0]);
        controller[1].update_grid(grid)
        player2_function(controller[1])
        game_over = True # demo
