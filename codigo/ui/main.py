#coding=utf-8

import sys, pygame
from Towerbloxx import Towerbloxx
from RunInfo import RunInfo
from UI import UI
sys.path.append( "../" )
from environment import Environment

def main(path, refresh_rate):

    run_info = RunInfo(path)
    towerbloxx = Towerbloxx(run_info)
    ui = UI(towerbloxx, refresh_rate)
    
    ui.show()

def print_usage():
    print "main.py path [refresh_rate_seconds]"

if __name__ == "__main__":  
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print_usage()
    path = sys.argv[1]
    refresh_rate = 1
    if len(sys.argv) == 3:
        refresh_rate = float(sys.argv[2])
    main(path, refresh_rate)


        
