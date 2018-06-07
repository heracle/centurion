from logger import Logger
import constants
from constants import *
from render import render
from blocks import *

class Controller:
    # add other stuff here
    def __init__(self, player_id, coordinates, color, team):
        self.player_id = player_id
        self.coordinates = coordinates
        self.color = color
        self.grid = []
        self.action = None # this is gonna be the json
        self.team = team
        self.tanksHP = []
        self.round = 0;
        self.last_shot = 0;

    def update(self, grid, tanksHP):
        self.grid = grid
        self.tanksHP = tanksHP
        self.round = self.round + 1
        self.action = None
        self.coordinates = self.get_my_tank_coordinates()

    def get_round(self):
        return self.round

    def get_team(self):
        return self.team['NO']

    def get_action(self):
        return self.action

    def get_coordinates(self):
        return self.coordinates

    def get_tankhp_by_index(self, index):
        return self.tanksHP[index]

    def get_total_number_tanks(self):
        return self.tanksHP.__len__()

    def get_tank_team(self, index):
        if(index < self.tanksHP.__len__() / 2):
            return 0
        return 1

    def get_grid_size(self):
        return { 'x': self.grid.__len__(), 
                 'y': self.grid[0].__len__()
                }

    def get_my_tank_coordinates(self):
        Logger.log('get_my_tank_coordinates(); player {}'.format(self.player_id))
        for i in range(self.grid.__len__()):
            for j in range(self.grid[0].__len__()): 
                if self.grid[i][j].type == 'Tank' and self.grid[i][j].player_id == self.player_id:
                    return {
                        'x': i,
                        'y': j,
                    }
    
    def get_enemy_tank_coordinates(self, enemy_id):
        Logger.log('get_enemy_tank_coordinates() ask for ' + str(enemy_id) + '; player {}'.format(self.player_id))
        for i in range(self.grid.__len__()):
            for j in range(self.grid[0].__len__()):
                if self.grid[i][j].type == 'Tank' and self.grid[i][j].player_id == enemy_id:
                    return {
                        'x': i,
                        'y': j,
                    }


    def is_ground_cell(self, coordinates):
        i = coordinates['x']
        j = coordinates['y']
        if self.grid[i][j].type == 'Ground' or self.grid[i][j].type == 'Tank':
            return True
        if self.grid[i][j].type == 'Projectile' and self.grid[i][j].block_type == 'Ground':
            return True
        return False


    def is_water_cell(self, coordinates):
        i = coordinates['x']
        j = coordinates['y']
        if self.grid[i][j].type  == 'Water':
            return True
        if self.grid[i][j].type == 'Projectile' and self.grid[i][j].block_type == 'Water':
            return True
        return False


    def is_object_cell(self, coordinates):
        i = coordinates['x']
        j = coordinates['y']
        if self.grid[i][j].type == 'Obstacle':
            return True
        return False

    def is_projectile_cell(self, coordinates):
        i = coordinates['x']
        j = coordinates['y']
        if self.grid[i][j].type == 'Projectile':
            return True
        return False

    def get_water_cells(self):
        Logger.log('get_water_cells(); player {}'.format(self.player_id))
        water_cells = []
        for i in range(self.grid.__len__()):
            for j in range(self.grid[0].__len__()):
                if self.is_water_cell({'x': i, 'y':j}):
                    water_cells.append({'x': i, 'y':j})
        return water_cells

    def get_ground_cells(self):
        Logger.log('get_ground_cells(); player {}'.format(self.player_id))
        ground_cells = []
        for i in range(self.grid.__len__()):
            for j in range(self.grid[0].__len__()):
                if self.is_ground_cell({'x': i, 'y':j}):
                    ground_cells.append({'x': i, 'y':j})
        return ground_cells

    def get_obstacle_cells(self):
        Logger.log('get_obstacle_cells(); player {}'.format(self.player_id))
        obstacle_cells = []
        for i in range(self.grid.__len__()):
            for j in range(self.grid[0].__len__()):
                if self.is_object_cell({'x': i, 'y':j}):
                    obstacle_cells.append({'x': i, 'y':j})
        return obstacle_cells

    def get_projectiles(self):#there will be not mentioned the destination of the projectils
        Logger.log('get_projectiles(); player {}'.format(self.player_id))
        projectiles = []
        for i in range(self.grid.__len__()):
            for j in range(self.grid[0].__len__()):
                if self.is_projectile_cell({'x': i, 'y': j}):
                    projectiles.append({'x': i, 'y':j, 'direction':self.grid[i][j].direction})
        return projectiles

    def is_coordinates_in_grid(self, coordinates):
        if coordinates['x'] < 0 or coordinates['y'] < 0:
            return False
        if coordinates['x'] >= self.grid.__len__() or coordinates['y'] >= self.grid[0].__len__():
            return False
        return True

    def move(self, coordinates):
        if self.action != None:
            Logger.indent('the action was already fixed for this round, player {}'.format(self.player_id))
            return False

        Logger.log('move(); player {}'.format(self.player_id))

        if self.round - self.last_shot >= constants.TIME_MAX_BETWEEN_SHOTS:
            Logger.error('this round the action must be a shot, player {}'.format(self.player_id))
            return False
            
        if self.is_coordinates_in_grid(coordinates) == False:
            Logger.error('coordinates out of the grid; player {}'.format(self.player_id))
            return False

        if self.is_ground_cell(coordinates) == False:
            Logger.error('coordinates not point to a gound cell, player {}'.format(self.player_id))
            return False
        
        
        if abs(coordinates['x'] - self.coordinates['x']) + abs(coordinates['y'] - self.coordinates['y']) != 1:
            Logger.error('the destination is not at distance 1 from the actual possition, player {}'.format(self.player_id))
            return False

        self.action = {'type' : constants.action_type['MOVE'], 'coordinates' : coordinates}
        return self.action

    def shot(self, coordinates):
        if self.action != None:
            Logger.indent('the action was already fixed for this round, player {}'.format(self.player_id))
            return False

        Logger.log('shot(); player {}'.format(self.player_id))

        #it is possible to choose a water destination -> but the projectile will be destroyed when it will reach he destination 
        #also, the same thing for obstacle destination

        if self.is_coordinates_in_grid(coordinates) == False:
            Logger.error('coordinates out of the grid, player {}'.format(self.player_id))
            return False

        if self.is_ground_cell(coordinates) == False:
            Logger.error('coordinates not point to a gound cell, player {}'.format(self.player_id))
            return False

        if coordinates['y'] != self.coordinates['y'] :
            Logger.error('coordinates do not have the same y value, player {}'.format(self.player_id))
            return False

        distance = coordinates['x'] - self.coordinates['x']

        if self.team['DX'] * distance <= 0: #0 is when we have the destination exactly on the actual possition
            Logger.error('coordinates are not in the good direction, player {}'.format(self.player_id))
            return False

        self.action = {'type' : constants.action_type['SHOT'], 'coordinates' : coordinates, 'dx': self.team['DX']}
        self.last_shot = self.round
        return self.action

   
class Round_process:
    def __init__(self):
        self.projectile_active = [] # the format will be the direction DX, actual coordinates and destination coordinates
        self.grid_history = [] # the round, the counter inside the round, the grid, the tanksHP
        self.round = 0;
        self.counter = 0;
        pass

    def get_round(self):
        return self.round


    def free_cell(self, grid, x, y):
        if grid[x][y].type == 'Water' or grid[x][y].type == 'Ground':
            return True
        return False

    def tank_cell(self, grid, x, y):
        if grid[x][y].type == 'Tank':
            return True
        return False

    def projectile_cell(self, grid, x, y):
        if grid[x][y].type == 'Projectile':
            return True
        return False

    def find_tank(self, id, grid):
        # print("find tank with id " + str(id))
        for i in range(grid.__len__()):
            for j in range(grid[0].__len__()):
                if grid[i][j].type == 'Tank' and grid[i][j].player_id == id:
                    return {
                        'x': i,
                        'y': j,
                    }

    def no_move_auto_damage(self, grid, tanksHP, controllers):
        Logger.log('in no move auto damage')
        for i in range(controllers.__len__()):
            action = controllers[i].get_action()
            if tanksHP[i] > 0 and action == None:
                self.damage(self.find_tank(i, grid), tanksHP, grid)
                self.grid_history.append(self.make_grid_moment(self.round, self.counter, grid, tanksHP))
                render.render([grid])


    def damage(self, tank_coordinates, tanksHP, grid):
        tank = grid[tank_coordinates['x']][tank_coordinates['y']]

        player_id = tank.player_id
        tanksHP[player_id] = tanksHP[player_id] - PROJECTILE_DAMAGE
        Logger.log('Take damage; HP ' + str(tanksHP[player_id]) + ' player {}'.format(player_id))

        if tanksHP[player_id] <= 0:
            grid[tank_coordinates['x']][tank_coordinates['y']] = Ground()
        pass

    def find_index_in_projectiles(self, coordinates):
        for i in range(self.projectile_active.__len__()):
            act = self.projectile_active[i];
            if act == None:
                continue
            if act['act_coord'] == coordinates:
                return i

    def delete_projectile(self, x):
        self.projectile_active[x] = None
        # self.projectile_active.pop(x)
        
    def new_water_ground_cell(self, kind):
        if kind == 'Water':
            return Water()
        elif kind == 'Ground':
            return Ground()
        else:
            Logger.error("asked for generate a non water/ground cell")


    def move_tanks(self, grid, controllers, tanksHP):
        Logger.log('In move tanks')
        
        for i in range(controllers.__len__()):
            action = controllers[i].get_action()
            if action == None:
                continue
            if tanksHP[i] > 0 and action['type'] == constants.action_type['MOVE']:
                
                tank_coordinates = self.find_tank(i, grid)
                destination = action['coordinates']
                if grid[destination['x']][destination['y']].type == constants.block_type['PROJECTILE']:
                    self.damage(tank_coordinates, tanksHP, grid)
                    self.delete_projectile(self.find_index_in_projectiles(destination))
                
                grid[destination['x']][destination['y']] = grid[tank_coordinates['x']][tank_coordinates['y']]
                grid[tank_coordinates['x']][tank_coordinates['y']] = Ground()


    def move_projectiles(self, grid, tanksHP):
        #two projectiles will destroy each other just if they are on the same y and had different directions
        #in any other case: obstacle / consecutive projectiles -> the possition will not be incresed
        for i in range(self.projectile_active.__len__()):
            act = self.projectile_active[i]
            if act == None:
                continue
            something_changed = False
            if act['act_coord'] != act['dest_coord']:
                x = act['act_coord']['x']
                y = act['act_coord']['y']
                mx = act['act_coord']['x'] + act['dx']
                my = act['act_coord']['y']
                if self.free_cell(grid, mx, my):
                    #the projectile is going to a free cell
                    something_changed = True
                    grid[mx][my] = Projectile(grid[mx][my].type, act['dx'], act['dest_coord'])
                    if self.projectile_cell(grid, x, y):
                        grid[x][y] = self.new_water_ground_cell(grid[x][y].block_type)

                    self.projectile_active[i]['act_coord']['x'] = self.projectile_active[i]['act_coord']['x'] + act['dx'] 

                elif self.tank_cell(grid, mx, my):
                    #the projectile is going to hit a tank
                    something_changed = True
                    self.damage({'x':mx, 'y':my}, tanksHP, grid)
                    if self.projectile_cell(grid, x, y):
                        grid[x][y] = self.new_water_ground_cell(grid[x][y].block_type)
                        
                    self.delete_projectile(i)
                elif self.projectile_cell(grid, mx, my):
                    #the projectile is going to another projectile
                    direction_m = grid[mx][my].direction
                    direction_a = act['dx']

                    if(direction_a * direction_m < 0):
                        m_projectile = self.find_index_in_projectiles({'x':mx, 'y':my})
                        something_changed = True
                        grid[mx][my] = self.new_water_ground_cell(grid[mx][my].block_type)
                        if self.projectile_cell(grid, x, y):
                            grid[x][y] = self.new_water_ground_cell(grid[x][y].block_type)
    
                        self.delete_projectile(i)
                        self.delete_projectile(m_projectile)
                    else:
                        if self.tank_cell(grid, x, y):
                            something_changed = True
                            self.damage({'x':x, 'y':y}, tanksHP, grid);
                            self.delete_projectile(i)

                else: #the projectile could not be move forward
                    if self.tank_cell(grid, x, y):
                        something_changed = True
                        self.damage({'x':x, 'y':y}, tanksHP, grid);
                        self.delete_projectile(i)
            # print(something_changed)
            if something_changed == True:
                self.grid_history.append(self.make_grid_moment(self.round, self.counter, grid, tanksHP))
                render.render([grid])


    def add_projectiles(self, controllers, parity, grid):
        for i in range(controllers.__len__()):
            if controllers[i].get_team() == parity:
                action = controllers[i].get_action()

                if action == None:
                    continue

                if action['type'] == constants.action_type['SHOT']:
                    self.projectile_active.append({'dx': action['dx'], 
                                                    'act_coord': self.find_tank(i, grid),
                                                    'dest_coord': action['coordinates']} )

    def make_grid_moment(self, round, counter, grid, tanksHP):
        return {'round': round, 'index': counter, 'grid': grid, 'taksHP': tanksHP}

    def clear_actual_used_projectiles(self):
        for i in range(self.projectile_active.__len__(), 0):
            act = self.projectile_active[i]
            if act == None:
                self.projectile_active.pop(i)

    def check_if_finished(self, tanksHP, controllers):
        #return True for continue the game
        team_alive = [False, False]
        
        for i in range(tanksHP.__len__()):
            if(tanksHP[i] > 0):
                team = controllers[i].get_team()
                team_alive[team] = True

        if(team_alive[0] == False and team_alive[1] == False):
            Logger.indent('Game finished; Draw')
            return False
        elif(team_alive[0] == False):
            Logger.indent('Game finised; Team 1 won; ' + str(team_name[1]['NAME']) + ' won')
            return False
        elif(team_alive[1] == False):
            Logger.indent('Game finised; Team 0 won; ' + str(team_name[0]['NAME']) + ' won')
            return False
        return True




    def apply_next_move(self, controllers, grid, tanksHP):
        #firstly, the already thrown projectiles will be moved (because we don't want to make a strategy by moving or throw another projectile in defense),
        #then, the new projectiles will be moved (for hiting always any very close enemy tank)
        #the 'none'-s, which mean auto damage
        #the moves of the tanks

        #this function will return false if the game is finished after this round
        #controller here is the array of controllers
        self.round = self.round + 1
        self.counter = 0
        self.grid_history.append(self.make_grid_moment(self.round, self.counter, grid, tanksHP))

        #attach the new projectiles to the projectile_active -> if the round parity decide the first processed team
        #so, for round 1, the first team will be team 1 and the second one will be team 0
        self.add_projectiles(controllers, self.round % 2, grid)     
        self.add_projectiles(controllers, 1 - self.round % 2, grid) #2 calls, 1 for each team

        self.move_projectiles(grid, tanksHP);
        self.no_move_auto_damage(grid, tanksHP, controllers);

        self.move_tanks(grid, controllers, tanksHP)
        self.clear_actual_used_projectiles()
        return self.check_if_finished(tanksHP, controllers)


if __name__ == '__main__':
    pass
