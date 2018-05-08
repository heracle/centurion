import constants

class Ground:
    def __init__(self):
        self.type = constants.block_type['GROUND']

class Water:
    def __init__(self):
        self.type = constants.block_type['WATER']

class Obstacle:
    def __init__(self):        
        self.type = constants.block_type['OBSTACLE']

class Tank:
    def __init__(self, color, player_id):
        self.color = color
        self.player_id = player_id
        self.type = constants.block_type['TANK']

class Projectile:
    def __init__(self, block_type, direction, destination):
        self.block_type = block_type
        self.direction = direction
        self.destination = destination;
        self.type = constants.block_type['PROJECTILE']
