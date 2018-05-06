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
* `update_grid(grid)`
Updates the grid that the player currently knows to a new one.
This can be useful if some of the cells are hidden.
    * `grid`: array of arrays
* `get_my_tank_coordinates()`
Returns the coordinates of player's tank.
    * `return_value`: object
        * `x`: integer
        * `y`: integer
* `get_enemy_tank_coordinates()`
Returns the coordinates of enemy's tank.
    * `return_value`: object
        * `x`: integer
        * `y`: integer
* `move(coordinates)`
Moves player's tank, if the move is valid (i.e. moving one unit at a time, not leaving the grid)
    * `coordinates`: object
        * `x`: integer
        * `y`: integer

