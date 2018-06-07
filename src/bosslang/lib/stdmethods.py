
# INSERT HERE PYTHON METHODS EXPOSED TO THE LANGUAGE

class Injector():
    bosslang_injected_methods = None

def getRound():
	return Injector.bosslang_injected_methods.get_round()

def getTeam():
	return Injector.bosslang_injected_methods.get_team()

def getCoordinatesX():
	return Injector.bosslang_injected_methods.get_coordinates_x()

def getCoordinatesY():
	return Injector.bosslang_injected_methods.get_coordinates_y()

def getTankHpByIndex(index):
	return Injector.bosslang_injected_methods.get_tankhp_by_index(index)

def getTotalNumberTanks():
	return Injector.bosslang_injected_methods.get_total_number_tanks()

def getTankTeam(index):
	return Injector.bosslang_injected_methods.get_tank_team(index)

def getGridSizeX():
	return Injector.bosslang_injected_methods.get_grid_size_x()

def getGridSizeY():
	return Injector.bosslang_injected_methods.get_grid_size_y()

def getMyTankCoordinatesX(): #the same as getCoordinatesX
	return Injector.bosslang_injected_methods.get_my_tank_coordinates_x()

def getMyTankCoordinatesY(): #the same as getCoordinatesY
	return Injector.bosslang_injected_methods.get_my_tank_coordinates_y()

def getEnemyTankCoordinatesX(index):
	return Injector.bosslang_injected_methods.get_enemy_tank_coordinates_x(index)

def getEnemyTankCoordinatesY(index):
	return Injector.bosslang_injected_methods.get_enemy_tank_coordinates_y(index)

def isGroundCell(x, y):
    return Injector.bosslang_injected_methods.is_ground_cell(x, y)

def isWaterCell(x, y):
	return Injector.bosslang_injected_methods.is_water_cell(x, y)

def isObjectCell(x, y):
	return Injector.bosslang_injected_methods.is_object_cell(x, y)

def isProjectileCell(x, y):
	return Injector.bosslang_injected_methods.is_projectile_cell(x, y)

def getTypeCell(x, y):
	return Injector.bosslang_injected_methods.get_type_cell(x, y)

def doMove(x, y):
	return Injector.bosslang_injected_methods.do_move(x, y)

def doShot(x, y):
	return Injector.bosslang_injected_methods.do_shot(x, y)

def squared(x):
    return x * x
