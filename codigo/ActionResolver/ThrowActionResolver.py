#coding=utf-8
import math

from ActionResolver import *

class ThrowActionResolver(ActionResolver):
    def __init__(self, environment):
        self._reward = 0
        super(ThrowActionResolver,self).__init__(environment)

    def resolve(self):
        self.throw()
        if self.environment.state().has_finished():
            return self.reward()
        else:
            return super(ThrowActionResolver,self).resolve()
        
    def throw(self):
        tower_crane_difference = self.environment.crane_pos - self.environment.tower_pos
        #diferencia entre centros (visto desde el punto de vista de la torre).

        if abs(tower_crane_difference) >= self.environment.tower_size:
            self._reward = self.MISSING_REWARD
        else:
            self.hit_effect(tower_crane_difference)
            

    def hit_effect(self, tower_crane_difference):
        self.environment.tower_pos = self.environment.crane_pos
        
        self.update_tower_angle()
        
        self._reward = self.HIT_REWARD
        
        if self.tower_fell():
            self._reward = self.TOWER_FELL_REWARD
            self.environment.finish()
        else:
            self.environment.add_floor()
            self.update_tower_speed(tower_crane_difference)



    def tower_fell(self):
        return abs(math.degrees(self.environment.tower_angle)) >= 30

    def reward(self):
        return self._reward

    def update_tower_speed(self, tower_crane_difference):
        alignment_difference_rate = float(tower_crane_difference) / self.environment.tower_size #porcentaje de desvio del tiro entre (-1,1)
        self.environment.tower_vel += self.environment.tower_vel * alignment_difference_rate
    
    def update_tower_angle(self):
        #Trigonometria
        tower_pos = self.environment.tower_pos #opuesto
        new_angle = 0

        if tower_pos != 0:
            height = self.environment.tower_height #adyacente
            new_angle = math.atan(tower_pos/float(height))
            
        self.environment.tower_angle = new_angle