## Controller

The controller class offers useful API and can be used by the player
Here are the functions available:

* `__init__(player_id, coordinates, color)`
    * `player_id`: integer
    * `coordinates`: object 
        * `x`: integer
        * `y`: integer
    * `color`: enum 
        * `red`, `green`, `blue`, `purple`
    * `team`: integer

* `update_grid(grid)`
Updates the grid that the player currently knows to a new one.
This can be useful if some of the cells are hidden.
    * `grid`: array of arrays
    * `tanksHP`: array of HP for all the tanks

* `get_round()`
Returns an Integer, the number of the round

* `get_team()`
Returns 0 or 1, depending the team of the actual controller

* `get_action()`
Returns NULL if there was not set an action for the current move or am object with 
* `return_value`: object
    * `type`: enum ('Move', 'Shot'),
    * `coordinates`: object 
        * `x`: integer
        * `y`: integer
    * `dx`: integer
        * +1 for team 0
        * -1 for team 1


* `get_coordinates()`
Returns the coordinates of player's tank.
    * `return_value`: object
        * `x`: integer
        * `y`: integer

* `get_tankhp_by_index(index)`
Returns an Integer - the remaining HP for the tank `index`

* `get_total_number_tanks()`
Returns an Integer - the total numer of tanks in the game

* `get_tank_team(index)`
Returns an Integer (0 or 1) - the team for the tank `index`

* `get_grid_size()`
Returns the lenght of the grid in an object:
    * `return_value`: object
        * `x`: integer
        * `y`: integer


* `get_my_tank_coordinates()`
Returns the coordinates of player's tank.
    * `return_value`: object
        * `x`: integer
        * `y`: integer

* `get_enemy_tank_coordinates(index)`
Returns the coordinates of enemy's tank with index `index`.
    * `return_value`: object
        * `x`: integer
        * `y`: integer

* `is_ground_cell(coordinates)`
Return True/ False if the cell is a ground cell or not 
    * `coordinates`: object 
        * `x`: integer
        * `y`: integer

* `is_water_cell(coordinates)`
Return True/ False if the cell is a water cell or not 
    * `coordinates`: object 
        * `x`: integer
        * `y`: integer

* `is_object_cell(coordinates)`
Return True/ False if the cell is an object cell or not 
    * `coordinates`: object 
        * `x`: integer
        * `y`: integer

* `is_projectile_cell(coordinates)`
Return True/ False if in the cell is a projectile or not 
    * `coordinates`: object 
        * `x`: integer
        * `y`: integer

* `get_water_cells()`
Returns all the water cells in the grid
    * `return_value`: array of objects
        * `x`: integer
        * `y`: integer


* `get_ground_cells()`
Returns all the ground cells in the grid
    * `return_value`: array of objects
        * `x`: integer
        * `y`: intege


* `get_obstacle_cells()`
Returns all the obstacle cells in the grid
    * `return_value`: array of objects
        * `x`: integer
        * `y`: intege


* `get_projectiles()`
Returns all the projectiles active in the grid
    * `return_value`: array of objects
        * `x`: integer
        * `y`: intege

* `is_coordinates_in_grid(coordinates)`
Returns True/False if the cell is in the grid or not
    * `coordinates`: object 
        * `x`: integer
        * `y`: integer



* `move(coordinates)`
Moves player's tank, if the move is valid (i.e. moving one unit at a time, not leaving the grid, the destination is one of the 4 adiacent cells)
    * `coordinates`: object
        * `x`: integer
        * `y`: integer
    * `Return_value`: boolean
        * `True` if the move was valid 
        * `False` if the move was not valid

* `shot(coordinates)`
Take a shot which will be constantly moving forward with one unit per round until it will reach the destination at coordinates, where will be waiting for a tank to move in the respective cell
    * `coordinates`: object
        * `x`: integer
        * `y`: integer
    * `Return_value`: boolean
        * `True` if the move was valid (has the same y value as the tank which send the projectile and the x value is correspondent with the direction in which the tank is able to shot)
        * `False` if the move was not valid

