from logger import Logger


class Controller:
    # add other stuff here
    def __init__(self, player_id, coordinates, color):
        self.player_id = player_id
        self.coordinates = coordinates
        self.color = color
        self.grid = []
        self.action = None # this is gonna be the json

    def update_grid(self, grid):
        self.grid = grid

    def get_my_tank_coordinates(self):
        Logger.log('get_my_tank_coordinates(); player {}'.format(self.player_id))
        for i in range(self.grid.__len__()):
            for j in range(self.grid[0].__len__()):
                if self.grid[i][j] == self.player_id:
                    return {
                        'x': i,
                        'y': j,
                    }
    
    def get_enemy_tank_coordinates(self):
        Logger.warn('not yet implemented')
        Logger.log('get_enemy_tank_coordinates(); player {}'.format(self.player_id))
        pass

    def move(self, coordinates):
        Logger.warn('not yet implemented')
        Logger.log('move(); player {}'.format(self.player_id))
        pass


def apply_next_move(controller):
    pass


if __name__ == '__main__':
    pass
