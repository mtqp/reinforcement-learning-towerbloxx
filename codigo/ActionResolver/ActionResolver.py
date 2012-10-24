import math

def sign(val):
    return cmp(val,0) or 1

class ActionResolver(object): 
    PASS_REWARD = -1
    MISSING_REWARD = -50
    TOWER_FELL_REWARD = -5000
    HIT_REWARD = 100
    
    @classmethod
    def create_for(cls, environment, action):
        from PassActionResolver import PassActionResolver
        from ThrowActionResolver import ThrowActionResolver
        if action == environment.PASS:
            return PassActionResolver(environment)
        else:
            return ThrowActionResolver(environment)

    def __init__(self, environment):
        self.environment = environment

    def resolve(self):
        self.move_crane()
        self.move_tower()
        return self.reward()

    def move_crane(self):
        if abs(self.environment.crane_pos) == self.environment.POSITION_BOUND:
            self.environment.crane_direction = -sign(self.environment.crane_pos)

        self.environment.crane_pos += self.environment.crane_direction
    
    def move_tower(self):      
        new_angle, new_vel = self.pendulus_move()        
        new_pos = self.next_tower_pos(new_angle)
        
        self.environment.tower_angle = new_angle
        self.environment.tower_vel = new_vel
        self.environment.tower_pos = new_pos
    
    def next_tower_pos(self, angle):
        #Trigonometria (SOH-CAH-TOA) :)
        distance_from_zero = math.tan(angle) * self.environment.tower_height #TAN * ADYACENTE
        return distance_from_zero

    def pendulus_move(self):
        #Ver http://www.physics.ncsu.edu/courses/py299cp/Lesson10/index.html
        delta_time = 0.4 #dt
        old_theta = self.environment.tower_angle
        old_omega = self.environment.tower_vel#angular velocity
        gravity = 9.8 #g
        height = float(self.environment.tower_height)#l
        
        omega = old_omega - delta_time*gravity/height*math.sin(old_theta)
        theta = old_theta + delta_time * old_omega
        
        return theta, omega