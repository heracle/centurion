## Strategies

Create here user strategies to fight agains (or teamed up) each other.

### Create new strategy
* `./new_strategy.sh STRATEGY_NAME`
* `./new_strategy.sh france`

### How to use
You will get a new python file called `STRATEGY_NAME.py`. The file should look like this:

```python
def strategy(controller, round):
    pass
```
Use the `controller` and `round` to figure out what the best strategy would be. Remember that your ultimate goal is to survive long enough to kill all your enemies' tanks.