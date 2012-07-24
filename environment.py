#coding=utf-8
import math
class Environment(object):
    THROW = 1
    PASS = 0

    def __init__(self):
        self.crane_direction = -1 #{-1;1}
        self.crane_pos = -49 #[-49,49]
        self.tower_vel = 5 #[-5,5]
        self.tower_pos = 0 #[-49,49]
        self.tower_size = 10
        self.tower_factor = 0

    def start(self):
        intial_state = self.state()
        final_state = "final"

        return (intial_state, final_state)

    def make_action(self, action):
        #BUG: Arrancando make_action con 0
        self.update_crane()

        if action == Environment.THROW:
            self.tower_factor += 0.1
            print self.tower_factor
            if self.tower_factor > 0.99:
                return "PERDISTE!!!"
        
        self.move_tower()

        reinforcement = 1
        next_state = self.state()
        return (next_state, reinforcement)

    def calculate_speed(self, speed, pos):
        sgn = (cmp(speed,0))
        vel =  (5 - abs(pos)/10) 
        return vel * sgn

    def state(self):
        return (self.tower_vel, self.tower_pos, self.crane_pos, self.crane_direction)

    def update_crane(self):
        if abs(self.crane_pos) == 49:
            self.crane_direction = -self.crane_direction
        
        self.crane_pos += self.crane_direction
    
    def move_tower(self):
        print self.__dict__
        self.tower_vel = self.calculate_speed(self.tower_vel, self.tower_pos)
        self.tower_pos += self.position_delta() 
        if abs(self.tower_pos) >= int(49*self.tower_factor): 
            self.tower_vel = abs(self.tower_vel) * cmp(0,self.tower_pos)


    def position_delta(self):
        if(self.tower_vel>0):
           return int(math.ceil(self.tower_factor * self.tower_vel))
        else:
           return int(math.floor(self.tower_factor * self.tower_vel))
