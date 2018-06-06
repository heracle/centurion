from controller import Controller

class BosslangApi:
    def __init__(self, controller):
        self.controller = controller

    def get_team(self)
        r = []
        r.append(self.controller.get_team())
        return r
    
    def get_coordinates(self)
        coord = self.controller.get_coordinates()
        r = []
        r.append(coord['x'])
        r.append(coord['y'])
        return r

    def get_tankhp_by_index(self, index)
        r = []
        r.append(self.controller.get_tankhp_by_index(index))
        return r

    def get_total_number_tanks(self)
        r = []
        r.append(self.controller.get_total_number_tanks())
        return r

    def get_tank_team(self, index)
        r = []
        r.append(self.controller.get_tank_team(index))
        return r

    def get_grid_size(self)
        r = []
        coord = self.controller.get_grid_size()
        x = coord['x']
        y = coord['y']
        r = []
        r.append(x)
        r.append(y)
        return r

    def get_my_tank_coordinates(self):
        coord = self.controller.get_my_tank_coordinates()
        x = coord['x']
        y = coord['y']
        r = []
        r.append(x)
        r.append(y)
        return r
    
    def get_enemy_tank_coordinates(self, enemy_id):
        coord = self.controller.get_enemy_tank_coordinates(enemy_id)
        x = coord['x']
        y = coord['y']
        r = []
        r.append(x)
        r.append(y)
        return r

    def is_ground_cell(self, x, y):
        r = []
        r.append(self.controller.is_ground_cell({'x': x, 'y':y}))
        return r
    
    def is_water_cell(self, x, y):
        r = []
        r.append(self.controller.is_water_cell({'x': x, 'y':y}))
        return r
    
    def is_object_cell(self, x, y):
        r = []
        r.append(self.controller.is_object_cell({'x': x, 'y':y}))
        return r
    
    def is_projectile_cell(self, x, y):
        r = []
        r.append(self.controller.is_projectile_cell({'x': x, 'y':y}))
        return r

    def get_water_cells(self):
        r = []
        rec = self.controller.get_water_cells()
        r.append(rec.__len__())
        for i in range(rec.__len__()):
            r.append(rec[i]['x'])
            r.append(rec[i]['y'])
        return r

    def get_ground_cells(self)
        r = []
        rec = self.controller.get_ground_cells()
        r.append(rec.__len__())
        for i in range(rec.__len__()):
            r.append(rec[i]['x'])
            r.append(rec[i]['y'])
        return r

    def get_obstacle_cells(self)
        r = []
        rec = self.controller.get_obstacle_cells()
        r.append(rec.__len__())
        for i in range(rec.__len__()):
            r.append(rec[i]['x'])
            r.append(rec[i]['y'])
        return r

    def get_projectiles(self)
        r = []
        rec = self.controller.get_projectiles()
        r.append(rec.__len__())
        for i in range(rec.__len__()):
            r.append(rec[i]['x'])
            r.append(rec[i]['y'])
        return r


    def do_move(self, x, y):
        coord = {}
        coord['x'] = x
        coord['y'] = y
        rec = self.controller.move(coord)
        if(rec == False)
            return 0;
        return 1;
    
    def do_shot(self, x, y):
        coord = {}
        coord['x'] = x
        coord['y'] = y
        rec = self.controller.shot(coord)
        if(rec == False)
            return 0;
        return 1;

if __name__ == '__main__':
    pass