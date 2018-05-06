class Ground:
    def __init__(self):
        pass

class Water:
    def __init__(self):
        pass

class Obstacle:
    def __init__(self):
        pass

class Tank:
    def __init__(self, color):
        self.color = color

class Projectile:
    def __init__(self, block_type, direction=0):
        self.block_type = block_type
        self.direction = direction
