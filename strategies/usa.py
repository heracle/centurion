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
    
    # import sys
    # sys.path.insert(0, '../src')
    # from bosslangapi import BosslangApi
    # sys.path.insert(0, './bosslang')
    # sys.path.insert(0, './bosslang/lib')
    # from stdmethods import Injector
    # from exe import runsource

    # Injector.bosslang_injected_methods = BosslangApi(controller)
    # runsource("""
    # program NONAME00;
    # var round : integer;
    # begin
    #     round := CALL(getRound);
    #     IF round = 15 then
    #     begin
    #         CALL(move, 7, 3);
    #     end;

    #     if round % 4 = 0 then
    #         CALL(shot, 1, 2);
    #     end;

    #     if round % 4 = 2 then
    #         CALL(shot, 1, 3);
    #     end;

    #     if round % 4 = 1 then
    #         CALL(move, 8, 3);
    #     end;

    #     if round % 4 = 3 then
    #         CALL(move, 8, 2);
    #     end;
    # """)  


    # if round == 15:
    #     controller.move({'x':7,'y': 3})

    # if round % 4 == 0:
    #     controller.shot({'x': 1, 'y': 2})
    # if round % 4 == 2:
    #     controller.shot({'x': 1, 'y': 3})

    # if round % 4 == 1:
    #     controller.move({'x':8, 'y':3})
    # if round % 4 == 3:
    #     controller.move({'x':8, 'y':2})


    # sys.path.insert(0, '../src')
    # from bosslangapi import BosslangApi
    # sys.path.insert(0, './bosslang')
    # sys.path.insert(0, './bosslang/lib')
    # from stdmethods import Injector
    # from exe import runsource
