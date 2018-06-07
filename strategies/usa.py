import sys
sys.path.insert(0, '../src')
from bosslangapi import BosslangApi
sys.path.insert(0, './bosslang')
sys.path.insert(0, './bosslang/lib')
from stdmethods import Injector
from exe import runsource

def strategy(controller):
    Injector.bosslang_injected_methods = BosslangApi(controller)
    runsource("""
    program NONAME00;
    var round : integer;
    begin
        round := CALL(getRound);
        IF round = 15 then
        begin
            CALL(move, 7, 3);
        end;
        if round - round div 4 * 4 = 0 then
        begin
            CALL(shot, 1, 2);
        end;
        if round - round div 4 * 4 = 2 then
        begin
            CALL(shot, 1, 3);
        end;
        if round - round div 4 * 4 = 1 then
        begin
            CALL(move, 8, 3);
        end;
        if round - round div 4 * 4 = 3 then
        begin
            CALL(move, 8, 2);
        end;
    end.
    """)  
