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
                crane_pos = int(splitted_line[0])
                tower_pos = int(splitted_line[1])
                tower_height = int(splitted_line[2])
                tower_factor = float(splitted_line[3])
                game_action = splitted_line[4]
                game_reward = int(splitted_line[5])
                
                crane_state = CraneState(crane_pos)
                tower_state = TowerState(tower_pos, tower_height, tower_factor)
                game_state = GameState(game_action, game_reward)
                
                self.states.append(TowerbloxxState(crane_state, tower_state, game_state))
            else:
                raise Exception("Cannot parse file")

        if len(self.states) == 0:
            raise Exception("Empty file!")

        file_source.close()
        

