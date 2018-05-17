
# INSERT HERE PYTHON METHODS EXPOSED TO THE LANGUAGE

class Injector():
    bosslang_injected_methods = None

def isgroundcell(x, y):
    return Injector.bosslang_injected_methods.is_ground_cell(x, y)

def getmycoord():
    r = Injector.bosslang_injected_methods.get_my_tank_coordinates()
    return r

def move():
    print("Execute a move up command")

def squared(x):
    return x * x
