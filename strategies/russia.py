def strategy(controller, round):
  

  if round % 2 == 0:
    controller.shot({'x':8, 'y':2})
    controller.shot({'x':8, 'y':3})
    
  controller.move({'x':1, 'y':2})
  controller.move({'x':1, 'y':3})