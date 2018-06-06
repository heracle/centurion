from controller import Controller
from controller import Round_process
from logger import Logger
import constants
import sys
from bosslangapi import BosslangApi
from blocks import *
sys.path.insert(0, './bosslang')
sys.path.insert(0, './bosslang/lib')
sys.path.insert(0, '../strategies/');
from stdmethods import Injector
from exe import runsource
grid = constants.EMPTY_GRID
tanksHP = [constants.INITIAL_HP, constants.INITIAL_HP]


teams = [[], []]
def import_player_functions():
    args_count = sys.argv.__len__() - 1

    if args_count != 2 and args_count != 4:
        Logger.error('You need to provide arguments')
        Logger.error('Currently only 2 or 4 arguments are allowed')
        Logger.error('Although for 4 arguments the game does not act properly')
        Logger.error('Example: `python3 main.py russia usa`')
        exit(0)
    
    if args_count == 4:
        Logger.error('Stopping because currently only 2 args supported')
        exit(0)
    
    for arg_index in range(args_count):
        try:
            strategy = __import__(sys.argv[arg_index + 1])
            print(strategy.strategy)
            if arg_index < args_count / 2:
                teams[0].append(strategy.strategy)
            else:
                teams[1].append(strategy.strategy)
        except:
            Logger.error('Could not import `strategy` function')


players = []
def create_players():
    args_count = sys.argv.__len__() - 1
    colors = ['BLUE', 'RED']
    coordinates = [
        {
            'x': 1,
            'y': 2
        }, {
            'x': 8,
            'y': 2
        }
    ]

    for player_index in range(args_count):
        team = 1
        if player_index < args_count / 2:
            team = 0

        player = {
            'player_id': player_index,
            'coordinates': coordinates[player_index],
            'color': constants.colors[colors[player_index]],
            'team': constants.team_name[team],
            'strategy': teams[team][0]
        }
        players.append(player)


def init_grid():
    for player_index in range(players.__len__()):
        grid[players[player_index]['coordinates']['x']][players[player_index]['coordinates']['y']] = \
            Tank(players[player_index]['color'], players[player_index]['player_id'])


controllers = []
def create_controllers():
    for player_index in range(players.__len__()):
        controllers.append(
            Controller(
                players[player_index]['player_id'],
                players[player_index]['coordinates'],
                players[player_index]['color'],
                players[player_index]['team'] 
                ))


def main():
    game_over = False
    game = Round_process()

    import_player_functions()
    create_players()
    init_grid()
    create_controllers()

    while game_over == False:
        Logger.log('A new round is occuring; Round' +  str(game.get_round()) )

        for player_index in range(players.__len__()):
            if tanksHP[player_index] != 0:
                controllers[player_index].update(grid, tanksHP) 
                players[player_index]['strategy'](controllers[player_index], game.get_round())

        if game.apply_next_move(controllers, grid, tanksHP) == False:
        	game_over = True


if __name__ == '__main__':
    main()
