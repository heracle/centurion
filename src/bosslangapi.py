from controller import Controller

class BosslangApi:
    def __init__(self, controller):
        self.controller = controller

    def get_my_tank_coordinates(self):
        coord = self.controller.get_my_tank_coordinates()
        x = coord['x']
        y = coord['y']
        return y
    
    def get_enemy_tank_coordinates(self, enemy_id):
        coord = self.controller.get_enemy_tank_coordinates(enemy_id)
        x = coord['x']
        y = coord['y']
        return y

    def is_ground_cell(self, x, y):
        return self.controller.is_ground_cell({'x': x, 'y':y})
    
    def is_water_cell(self, x, y):
        return self.controller.is_water_cell({'x': x, 'y':y})
    
    def is_object_cell(self, x, y):
        return self.controller.is_object_cell({'x': x, 'y':y})
    
    def is_projectile_cell(self, x, y):
        return self.controller.is_projectile_cell({'x': x, 'y':y})

    def do_move(self, x, y):
        coord = {}
        coord['x'] = x
        coord['y'] = y
        self.controller.move(coord)
        pass
    
    def do_shot(self, x, y):
        coord = {}
        coord['x'] = x
        coord['y'] = y
        self.controller.shot(coord)
        pass

if __name__ == '__main__':
    pass