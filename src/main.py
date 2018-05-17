from controller import Controller
from controller import Round_process
from logger import Logger
from render import *
import constants

from bosslangapi import BosslangApi
sys.path.insert(0, './bosslang')
sys.path.insert(0, './bosslang/lib')
from stdmethods import Injector
from exe import runsource

# just some init things I'm doing now for the architecture demo
# don't take this crappy code too serious
grid = constants.EMPTY_GRID
tanksHP = [constants.INITIAL_HP, constants.INITIAL_HP]


player0 = {
    'player_id': 0,
    'coordinates': {
        'x': 1,
        'y': 2,
    },
    'color': constants.colors['BLUE'],
    'team': constants.team_name[0]
}

player1 = {
    'player_id': 1,
    'coordinates': {
        'x': 8,
        'y': 2,
    },
    'color': constants.colors['RED'],
    'team': constants.team_name[1]
}
grid[player0['coordinates']['x']][player0['coordinates']['y']] = Tank(player0['color'], player0['player_id'])
grid[player1['coordinates']['x']][player1['coordinates']['y']] = Tank(player1['color'], player1['player_id'])
# okay the crappy init code is over here, we will probably do another config
# file for this, but for now it looks ok just the way it is right here


# now define the two players controllers
controller = []
controller.append(
    Controller(
        player0['player_id'],
        player0['coordinates'],
        player0['color'],
        player0['team'] 
        ))
controller.append(
    Controller(
        player1['player_id'],
        player1['coordinates'],
        player1['color'],
        player1['team']
        ))


# each player will have a function, so let's hardcode those for now
def player1_function(controller, round):
    # Logger.log(controller.get_water_cells())
    # Logger.log(controller.get_ground_cells())
    # Logger.log(controller.get_obstacle_cells())
    # Logger.log(controller.get_projectiles())

    if round == 15:
    	Logger.indent(controller.move({'x':7,'y': 3}))

    # 'x': 8,
    # 'y': 2,
    if round % 4 == 0:
    	Logger.indent(controller.shot({'x': 1, 'y': 2}))
    if round % 4 == 2:
    	Logger.indent(controller.shot({'x': 1, 'y': 3}))

    if round % 4 == 1:
    	Logger.indent(controller.move({'x':8, 'y':3}))
    if round % 4 == 3:
    	Logger.indent(controller.move({'x':8, 'y':2}))


    # Logger.log(controller.move({'x': 9, 'y': 2}))
    # Logger.log(controller.move({'x': 9, 'y': 1}))
    # Logger.log(controller.move({'x': 8, 'y': 1}))

    # Logger.log(controller.move({'x': 8, 'y': 1}))

    pass

def player0_function(controller, round):
    # Logger.log(controller.get_my_tank_coordinates())

    # Logger.log(controller.get_enemy_tank_coordinates(1))

    # 'x': 1,
    # 'y': 2,

    # Logger.log(controller.shot({'x':20, 'y':7}))

    Injector.bosslang_injected_methods = BosslangApi(controller)
    runsource("""
    program NONAME00;
    var x, y, t : integer;
    var r : real;
    begin
        t := CALL(isgroundcell, 1, 1);
        CALL(print, t);
        { x := CALL(getmycoord); }
    end.
    """)

    if round % 2 == 0:
    	Logger.indent(controller.shot({'x':8, 'y':2}))
    	Logger.indent(controller.shot({'x':8, 'y':3}))
    	
    Logger.indent(controller.move({'x':1, 'y':2}))
    Logger.indent(controller.move({'x':1, 'y':3}))

    # Logger.log(controller.shot({'x':0, 'y':7}))
    # Logger.log(controller.shot({'x':8, 'y':7}))
    # Logger.log(controller.shot({'x':5, 'y':6}))
    # Logger.log(controller.shot({'x':1, 'y':7}))

    # Logger.log(controller.shot({'x':3, 'y':7}))

    pass

# now let's play
def main():
    render([grid])
    game_over = False

    game = Round_process()

    while game_over == False:
    # for i in range(15):
        # note that it's very important to update the grid each time before calling player_function.
        # if not, the player wouldn't know the latest configuration of the grid
        Logger.log('A new round is occuring; Round' +  str(game.get_round()) )

        if tanksHP[0] != 0:
            controller[0].update(grid, tanksHP) 
            player0_function(controller[0], game.get_round())
        if tanksHP[1] != 1:
            controller[1].update(grid, tanksHP)
            player1_function(controller[1], game.get_round())
        

        if game.apply_next_move(controller, grid, tanksHP) == False:
        	game_over = True # demo

if __name__ == '__main__':
    main()
