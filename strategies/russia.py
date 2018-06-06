def strategy(controller, round):
  if round == 15:
    controller.move({'x':7,'y': 3})

  if round % 4 == 0:
    controller.shot({'x': 1, 'y': 2})
  if round % 4 == 2:
    controller.shot({'x': 1, 'y': 3})

  if round % 4 == 1:
    controller.move({'x':8, 'y':3})
  if round % 4 == 3:
    controller.move({'x':8, 'y':2})