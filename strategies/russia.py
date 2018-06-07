def strategy(controller, round):
    # if round % 2 == 0:
    #     controller.shot({'x':8, 'y':2})
    #     controller.shot({'x':8, 'y':3})
    # controller.move({'x':1, 'y':2})
    # controller.move({'x':1, 'y':3})

    import sys
    sys.path.insert(0, '../src')
    from bosslangapi import BosslangApi
    sys.path.insert(0, './bosslang')
    sys.path.insert(0, './bosslang/lib')
    from stdmethods import Injector
    from exe import runsource
    

    Injector.bosslang_injected_methods = BosslangApi(controller)
    runsource("""
    program NONAME00;
    var round : integer;
    begin
        round := CALL(getRound);
        IF round - round div 2 * 2 = 1 THEN
        BEGIN
            CALL(shot, 8, 2);
            CALL(shot, 8, 3);
        END;

        CALL(move, 1, 2);
        CALL(move, 1, 3);
    end.

    """)

    

    