#coding=utf-8

import sys, pygame
from Towerbloxx import Towerbloxx
from RunInfo import RunInfo
from UI import UI
sys.path.append( "../" )
from environment import Environment

def main(path):

    run_info = RunInfo(path)
    towerbloxx = Towerbloxx(run_info)
    ui = UI(towerbloxx)
    
    ui.show()

if __name__ == "__main__":  
    main(sys.argv[1])
        
        
