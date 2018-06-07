#oscilating on 

def strategy(controller):
    round = controller.get_round()
    my_team = controller.get_team()    
    my_coord = controller.get_coordinates()
    if controller.get_tank_team(0) != my_team:
        opp_coord = controller.get_enemy_tank_coordinates(0)
    if controller.get_tank_team(1) != my_team:
        opp_coord = controller.get_enemy_tank_coordinates(1)

    if round < 3:
        controller.move({'x': my_coord['x'], 'y': my_coord['y'] - 1})

    round -= 3

    grid = controller.get_grid_size();
    grid['y'] = grid['y'] - 1

    if round % 2 == 0:
        controller.shot({'x': opp_coord['x'], 'y': my_coord['y']})
    else:
        print(int(int(round / 2) / grid['y']))
        if int(int(round / 2) / grid['y']) % 2 == 0:
            controller.move({'x': my_coord['x'], 'y': my_coord['y'] + 1})
        else:
            controller.move({'x': my_coord['x'], 'y': my_coord['y'] - 1})
    controller.shot({'x': opp_coord['x'], 'y': my_coord['y']})
    print(str(round) + " current round")

    
