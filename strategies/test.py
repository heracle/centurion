import sys
sys.path.insert(0, '../src')
from bosslangapi import BosslangApi
sys.path.insert(0, './bosslang')
sys.path.insert(0, './bosslang/lib')
from stdmethods import Injector
from exe import runsource
    
def strategy(controller):
    Injector.bosslang_injected_methods = BosslangApi(controller)
    # Your bosslang code goes inside runsource
    runsource("""
    program test;
    var round, team, myX, myY, noTanks, gridX, gridY, aux1, aux2, mat : integer;
    begin
        round := CALL(getRound);
        team := CALL(getTeam);
        myX := CALL(getCoordinatesX);
        myY := CALL(getCoordinatesY);
        noTanks := Call(getTotalNumberTanks);
        gridX := CALL(getGridSizeX);
        gridY := CALL(getGridSizeY);

        CALL(printer, round);
        CALL(printer, team);
        CALL(printer, myX);
        CALL(printer, myY);
        CALL(printer, noTanks);
        CALL(printer, gridX);
        CALL(printer, gridY);

        aux1 := 0;
        while aux1 < gridX then 
        begin
            aux2 := 0;
            while aux2 < gridY then 
            begin
                mat[aux1][aux2] := CALL(getTypeCell, aux1, aux2);
                CALL(printer, mat[aux1][aux2]);
                aux2 := aux2 + 1;
            end;
            aux1 := aux1 + 1;
        end;

        
        aux1 := 0;
        while aux1 < gridX then 
        begin
            aux2 := 0;
            while aux2 < gridY then 
            begin
                CALL(printer, mat[aux1][aux2]);
                aux2 := aux2 + 1;
            end;
            aux1 := aux1 + 1;
        end;
        

        IF round - round div 2 * 2 = 1 THEN
        BEGIN
            CALL(shot, 8, 2);
            CALL(shot, 8, 3);
        END;

        CALL(move, 1, 2);
        CALL(move, 1, 3);
    end.

    """)
    
