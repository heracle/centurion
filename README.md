# Centurion

Programming game in which each player comes up with a strategy (function) to controll his own tank. Collaborate with your team and destroy all the enemies' tanks before they destroy you.

### Rules
* The game is turn-based, and each player has to write a function to control his own tank.
* There can be `1v1` or `2v2` games.
  * <span style='color: #DD4C3F;'>
      2v2 not supported in this version
     </span>
* In order to create your strategies, you will receive a `controller` which provides all the API you need to take decisions and control your tank.
* At each round, each strategy could get some informations abount the grid at that moment of time and choose if in that round eather the tank will move to a adiacent cell (on the 4 directions: up, down, left, right), while the cell is inside the grid or if the tank will shot a projectile to a destination position. The destination of a projectile should have the same Y with the tank and the X lower for team 1 and higher for team 0. The destination of any projectile should be a grould cell.
* You can't move on top of the water and you can't move to a cell if there is an obstacle.
* The projectiles you shoot can go above ground and water, but they will stop if they encounter an obstacle.
* If two enemy projectiles encounter each other, they will both be destroyed.
* Projectiles which belong to the same team will not destroy each other, instead they will form a queue of waiting
* Your tank's full HP is 100, and one projectile which hit the target is worth 25 points of damage.
* Your tank will get <span style='color: #DD4C3F;'>25 points of damage</span> each turn it waits. That is, if your tank doesn't move or shoot anything, it will lose 25 HP.
* Each player can be situated on the upper/bottom side of the map and he can't go to the other side. 
* The map is not symmetrical.
* At each 10 consecutive round, each tank should shot at least once. After 9 consecutive round when a tank was just moving, all the moving requests will be rejected.
* The order for processing the round: 
	* I) the new projectiles will be added. If the round is even, first will be added the projectiles from team 0 and, after, the projectiles from team 1; if the round is odd, will be processed the projectiles from team 1 and, after, from team 0. Each projectile is added at the position of the tank and will be moved in the next step.
	* II) the list of active projectiles is iterated and, each projectile which is not already on its destinations and has the cell in its direction free, is moved. For all the others, there will be do nothing.
	* III) will be received the autodamage for the all the tanks which have not choosed a valid move/shot
	* IV) all the tanks are moved as they want


### How to run
Clone the git repository. Go to the `centurion/src` folder and run `python3 main.py STRATEGY_1 STRATEGY_2` to make two strategies fight against each other.

Example `python3 main.py russia usa`

<span style='color: #DD4C3F;'>Be careful to select the right order for the arguments</span>. That is, `python3 main.py russia usa` is not the same as `python3 main.py usa russia`. The first player is positioned on the top of the map and the second one on the bottom

### Creating a new strategy
Move into `strategies/` and run `./new_strategy.sh STRATEGY_NAME`. More info on creating a new strategy [here](https://github.com/heracle/centurion/tree/master/strategies). (check the `README.md`)

### Bosslang
You can use `python3` or `bosslang` to write the code of your bot. More info on `bosslang` [here](https://github.com/heracle/centurion/tree/master/src/bosslang). (check the `README.md`)