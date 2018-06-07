import sys
sys.path.insert(0, '../src')
from bosslangapi import BosslangApi
sys.path.insert(0, './bosslang')
sys.path.insert(0, './bosslang/lib')
from stdmethods import Injector
from exe import runsource
    
def strategy(controller, round):
    Injector.bosslang_injected_methods = BosslangApi(controller)
    # Your bosslang code goes inside runsource
    runsource("""
    """)
    
