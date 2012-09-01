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

        if abs(tower_crane_difference) > self.environment.tower_size:
            self._reward = self.MISSING_REWARD
        else:
            self.hit_effect(tower_crane_difference)

               
    def hit_effect(self, tower_crane_difference):
        improve_tower_factor = self.update_tower_factor(tower_crane_difference)
        
        if self.tower_fell():
                self._reward = self.TOWER_FELL_REWARD
                self.environment.finish()
        else:
            if improve_tower_factor:
                self._reward = self.UPGRADE_STABILITY_REWARD
            else:
                self._reward = self.DOWNGRADE_STABILITY_REWARD
            
            self.environment.add_floor()
            self.environment.tower_pos = self.environment.crane_pos

    def tower_fell(self):
        return abs(self.environment.tower_factor) > 0.99

    def reward(self):
        return self._reward

    def update_tower_factor(self, tower_crane_difference):
        alignment_difference_rate = float(tower_crane_difference) / self.environment.tower_size #porcentaje de desvio del tiro entre (-1,1)
        self.environment.tower_factor += alignment_difference_rate


