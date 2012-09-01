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

        if abs(tower_crane_difference) > self.environment.tower_size/2:
            self._reward = self.MISSING_REWARD
        else:
            self.hit_effect(tower_crane_difference)

    def hit_effect(self, tower_crane_difference):
        has_improved_tower_factor = self.update_tower_factor(tower_crane_difference)#-1,0,1 son los valores posibles
        
        if self.tower_fell():
                self._reward = self.TOWER_FELL_REWARD
                self.environment.finish()
        else:
            #ERROR: Para mi el reward deberia estar relacionado con cuan bien
            # quedó la torre con respecto de antes no solo si mejoró, se
            # mantuvo o empeoró...
            if has_improved_tower_factor == 1:
                self._reward = self.UPGRADE_STABILITY_REWARD
            elif has_improved_tower_factor == -1:
                self._reward = self.DOWNGRADE_STABILITY_REWARD
            else:#improve_tower_factor == 0
                self._reward = self.MANTAIN_STABILITY_REWARD
            
            self.environment.add_floor()
            self.environment.tower_pos = self.environment.crane_pos
            
            self.update_tower_angle()

    def tower_fell(self):
        return abs(self.environment.tower_factor) > 0.99

    def reward(self):
        return self._reward

    def update_tower_factor(self, tower_crane_difference):
        old_tower_factor = self.environment.tower_factor
        alignment_difference_rate = float(tower_crane_difference) / self.environment.tower_size #porcentaje de desvio del tiro entre (-1,1)
        self.environment.tower_factor += alignment_difference_rate
        return cmp(abs(old_tower_factor),abs(self.environment.tower_factor))
    
    def update_tower_angle(self):
        #Trigonometria
        distance_from_zero = self.environment.tower_pos #opuesto
        if distance_from_zero > 0:
            height = self.environment.tower_height #adyacente
            new_angle = math.atan(float(height)/distance_from_zero)
        else:
            new_angle = 0
        self.environment.tower_angle = new_angle