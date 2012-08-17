from ActionResolver import *

class ThrowActionResolver(ActionResolver):
    def resolve(self):
        self.throw()
        if self.environment.state.has_finished():
            return self.environment.state, self.reward()
        else:
            return super(ActionResolver,self).resolve()
        
    def throw(self):
        tower_crane_difference = self.environment.crane_pos - self.environment.tower_pos 
        #diferencia entre centros (visto desde el punto de vista de la torre).

        if abs(tower_crane_difference) > self.environment.tower_size:
            self.reward = self.MISSING_REWARD
        else:
            self.hit_effect(tower_crane_difference)

               
    def hit_effect(self, tower_crane_difference):
        improve_tower_factor = self.update_tower_factor(tower_crane_difference)
        
        if self.tower_fell():
                self.reward = self.TOWER_FELL_REWARD
                self.environment.state.finish()
        else:
            if improve_tower_factor:
                self.reward = self.UPGRADE_STABILITY_REWARD
            else:
                self.reward = self.DOWNGRADE_STABILITY_REWARD
            
            self.environment.add_floor()
            self.environment.tower_pos = self.environment.crane_pos

    def tower_fell(self):
        return abs(self.tower_factor) > 0.99

    def reward(self):

    def update_tower_factor(self, tower_crane_difference):
        alignment_difference_rate = tower_crane_difference / self.tower_size #porcentaje de desvio del tiro entre (-1,1)
        self.environment.tower_factor += alignment_difference_rate


