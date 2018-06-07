## bosslangAPI

The bosslangSTDmethods offers some method useful for develop a strategy in bosslang language
Here are the methods available:

* `CALL(isgroundcell, 1, 1)`

* `CALL(getTeam)`
	Returns 0 or 1, depending the team of the actual controller

* `CALL(getCoordinatesX)`
	Returns an Integer - the X coordinates of the tank

* `CALL(getCoordinatesY)`
	Returns an Integer - the Y coordinates of the tank


* `CALL(getTankHpByIndex, index)`
	Returns an Integer - the remaining HP of the tank `index`


* `CALL(getTotalNumberTanks)`
	Returns an Integer - the total number of tanks in the game

* `CALL(getTankTeam, index)`
	Returns an Integer (0 or 1) - the team for the Tank index

* `CALL(getGridSizeX)`
	Returns an Integer - the length of the grid


* `CALL(getGridSizeY)`
	Returns an Integer - the width of the grid

* `CALL(getMyTankCoordinatesX)`
	Returns an Integer - the X coordinates of the tank

* `CALL(getMyTankCoordinatesY)`
	Returns an Integer - the Y coordinates of the tank



* `CALL(getEnemyTankCoordinatesX, index)`
	Returns an Integer - the X coordinates of the tank index

* `CALL(getEnemyTankCoordinatesY, index)`
	Returns an Integer - the Y coordinates of the tank index

* `CALL(isGroundCell, x, y)`
	Returns an Integer (0 or 1) - 1 if the cell at coordinates `x y` is a ground cell or 0 otherwise


* `CALL(isWaterCell, x, y)`
	Returns an Integer (0 or 1) - 1 if the cell at coordinates `x y` is a water cell or 0 otherwise

* `CALL(isObjectCell, x, y)`
	Returns an Integer (0 or 1) - 1 if the cell at coordinates `x y` is an object cell or 0 otherwise

* `CALL(isProjectileCell, x, y)`
	Returns an Integer (0 or 1) - 1 if the cell at coordinates `x y` has a projectile on it or 0 otherwise

* `CALL(get_type_cell, x, y)`
	Returns an Integer R
		if `R & 1`  -> ground cell
		if `R & 2`  -> water cell
		if `R & 4`  -> object cell
		if `R & 8`  -> projectile cell

* `CALL(isObjectCell, x, y)`
	Returns an Integer (0 or 1) - 1 if the cell at coordinates `x y` is an object cell or 0 otherwise

* `Call(move, x, y)`
	Moves player's tank, if the move is valid (i.e. moving one unit at a time, not leaving the grid, the destination is one of the 4 adiacent cells)
    * `Return_value`: Integer
        * `1` if the move was valid 
        * `0` if the move was not valid

* `Call(shot, x, y)`
    Take a shot which will be constantly moving forward with one unit per round until it will reach the destination at coordinates, where will be waiting for a tank to move in the respective cell
    * `Return_value`: Integer
        * `1` if the move was valid 
        * `0` if the move was not valid