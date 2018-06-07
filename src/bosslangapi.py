from controller import Controller

class BosslangApi:
    def __init__(self, controller):
        self.controller = controller

    def get_team(self):
        return self.controller.get_team()
    
    def get_coordinates_x(self):
        coord = self.controller.get_coordinates()
        return coord['x']

    def get_coordinates_y(self):
        coord = self.controller.get_coordinates()
        return coord['y']

    def get_tankhp_by_index(self, index):
        return self.controller.get_tankhp_by_index(index)

    def get_total_number_tanks(self):
        return self.controller.get_total_number_tanks()

    def get_tank_team(self, index):
        return self.controller.get_tank_team(index)

    def get_grid_size_x(self):
        coord = self.controller.get_grid_size()
        return coord['x']

    def get_grid_size_y(self):
        coord = self.controller.get_grid_size()
        return coord['y']

    def get_my_tank_coordinates_x(self):
        coord = self.controller.get_my_tank_coordinates()
        return coord['x']
    
    def get_my_tank_coordinates_y(self):
        coord = self.controller.get_my_tank_coordinates()
        return coord['y']

    def get_enemy_tank_coordinates_x(self, enemy_id):
        coord = self.controller.get_enemy_tank_coordinates(enemy_id)
        return coord['x']

    def get_enemy_tank_coordinates_y(self, enemy_id):
        coord = self.controller.get_enemy_tank_coordinates(enemy_id)
        return coord['y']

    def is_ground_cell(self, x, y):
        return self.controller.is_ground_cell({'x': x, 'y':y})
    
    def is_water_cell(self, x, y):
        return self.controller.is_water_cell({'x': x, 'y':y})
    
    def is_object_cell(self, x, y):
        return self.controller.is_object_cell({'x': x, 'y':y})
    
    def is_projectile_cell(self, x, y):
        return self.controller.is_projectile_cell({'x': x, 'y':y})

    def get_type_cell(self, x, y):
        ret = 0
        if elf.controller.is_ground_cell({'x': x, 'y':y}) ==  True:
            ret += 1
        if self.controller.is_water_cell({'x': x, 'y':y}) ==  True:
            ret += 2
        if self.controller.is_object_cell({'x': x, 'y':y}) == True:
            ret += 4
        if self.controller.is_projectile_cell({'x': x, 'y':y}) == True:
            ret += 8
        return ret


    # def get_water_cells(self):
    #     r = []
    #     rec = self.controller.get_water_cells()
    #     r.append(rec.__len__())
    #     for i in range(rec.__len__()):
    #         r.append(rec[i]['x'])
    #         r.append(rec[i]['y'])
    #     return r

    # def get_ground_cells(self):
    #     r = []
    #     rec = self.controller.get_ground_cells()
    #     r.append(rec.__len__())
    #     for i in range(rec.__len__()):
    #         r.append(rec[i]['x'])
    #         r.append(rec[i]['y'])
    #     return r

    # def get_obstacle_cells(self):
    #     r = []
    #     rec = self.controller.get_obstacle_cells()
    #     r.append(rec.__len__())
    #     for i in range(rec.__len__()):
    #         r.append(rec[i]['x'])
    #         r.append(rec[i]['y'])
    #     return r

    # def get_projectiles(self):
    #     r = []
    #     rec = self.controller.get_projectiles()
    #     r.append(rec.__len__())
    #     for i in range(rec.__len__()):
    #         r.append(rec[i]['x'])
    #         r.append(rec[i]['y'])
    #     return r


    def move(self, x, y):
        coord = {}
        coord['x'] = x
        coord['y'] = y
        rec = self.controller.move(coord)
        if(rec == False)
            return 0;
        return 1;
    
    def shot(self, x, y):
        coord = {}
        coord['x'] = x
        coord['y'] = y
        rec = self.controller.shot(coord)
        if(rec == False)
            return 0;
        return 1;

if __name__ == '__main__':
    pass