#coding=utf-8

from TowerbloxxState import * 

class RunInfo(object):
    def __init__(self, path):
        self.path = path
        self.states = []
        self._load_info()
        
    def _load_info(self):
        file_source = open(self.path, 'r')

        for line in file_source:
            splitted_line = line.split()
            if len(splitted_line) == 6:
                crane_dir = splitted_line[0]
                crane_pos = splitted_line[1]
                tower_vel = splitted_line[2]
                tower_pos = splitted_line[3]
                tower_height = splitted_line[4]
                tower_factor = splitted_line[5]
                
                crane_state = CraneState(crane_pos, crane_dir)
                tower_state = TowerState(tower_pos, tower_vel, tower_height, tower_factor)
                
                self.states.append(TowerbloxxState(crane_state, tower_state))
            else:
                raise Exception("Cannot parse file")

        if len(self.states) == 0:
            raise Exception("Empty file!")

        file_source.close()
