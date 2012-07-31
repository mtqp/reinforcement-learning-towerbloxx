#coding=utf-8
import math
class Environment(object):
    THROW = 1
    PASS = 0

    def __init__(self):
        self.crane_direction = 1#-1 #{-1;1}
        self.crane_pos = -15#-49 #[-49,49]
        self.tower_vel = 0 #[-5,5]
        self.tower_pos = 0 #[-49,49]
        self.tower_size = 0
        self.tower_factor = 0

    def start(self):
        intial_state = self.state()
        final_state = "final"

        return (intial_state, final_state)

    def make_action(self, action):
        previous_tower_factor = self.tower_factor
        
        self.update_tower_state(action)
        if not self.is_tower_raised():
            return "PERDISTE!!!"

        self.move_tower()
        self.move_crane()

        next_state = self.state()
        reinforcement = self.get_reward(action, previous_tower_factor)
        return (next_state, reinforcement)

    def get_reward(self, action, comparison_factor):
        reinforcement = 0
        improved_tower_balance = self.tower_factor <= comparison_factor
        
        if self.has_new_floor(action):
            if improved_tower_balance:
                reinforcement = 500
            else:
                reinforcement = 100
        else:
            if action == Environment.THROW:
                reinforcement = -100 #negativo por no haber fallado
            else:
                reinforcement = -5 #negativo por no haber tirado

        return reinforcement

    #[MDS] --> un piso se agrega si queda a +- 10 de la posicion del 
    #--------> piso anterior
    #PRE: NO se movió el crane
    def has_new_floor(self, action):
        has_new_floor = False
        if action == Environment.THROW:
            drop_offset = abs(self.get_drop_offset())
            has_new_floor = drop_offset <= 10     
        
        return has_new_floor

    def get_drop_offset(self):
        if self.tower_pos == 0:
            return self.crane_pos

        crane = abs(self.crane_pos)
        tower = abs(self.tower_pos)
        same_sign = (crane * tower) > 0
        
        if same_sign:        
            return crane - tower
        else:
            return crane + tower            
    
    #PRE: NO se movió el crane           
    def update_tower_state(self, action):
        if self.has_new_floor(action):
            self.tower_size += 1
            self.update_tower_factor()

    #PRE: El crane cae sobre el edificio
    def update_tower_factor(self):
        drop_offset = self.get_drop_offset()
     
        if drop_offset != 0: ##sino no modifico el movimiento del edificio
            drop_right = drop_offset > 0 #se si lanzo a izquierda o derecha del ultimo piso
            tower_right = self.tower_pos > 0 #se para que lado se mueve la torre
            
            centers_from_left = drop_right and not tower_right
            centers_from_right= not drop_right and tower_right
            tower_balanced = self.tower_factor <= 0.0
            
            increase_stability =  centers_from_left or centers_from_right
            increase_stability &= not tower_balanced
            
            #TODO: la cuenta de la estabilizacion no me parece real...            
            normalize_offset = abs(drop_offset) / 100.0
            normalize_height = (self.tower_size + 1)/100.0
                        
            print "drop offset %d" % drop_offset
            print "normalize_offset %f" % normalize_offset
            print "tower pos %d" % self.tower_pos
            print increase_stability

            if increase_stability:
                self.tower_factor -= 0.1 + normalize_offset + normalize_height
                if self.tower_factor < 0: #por si se estabiliza "de mas"
                    self.tower_factor = 0
            else:
                self.tower_factor += 0.1 + normalize_offset + normalize_height

    def is_tower_raised(self):
        return self.tower_factor <= 0.99

    def calculate_tower_speed(self, sgn, pos):
        vel =  (5 - abs(pos)/10) 
        return vel * sgn

    def state(self):
        return (self.tower_vel, self.tower_pos, self.crane_pos, self.crane_direction)

    def move_crane(self):
        if abs(self.crane_pos) == 49:
            self.crane_direction = -self.crane_direction
        
        self.crane_pos += self.crane_direction
    
    # [MDS] --> no quedo lo suficientemente prolijo!
    # --> cmp(0,0) da cero, x lo tanto no podes romper el equilibrio
    def get_speed_sign(self):
        moving = self.tower_vel != 0
        sgn = (cmp(self.tower_vel,0))
        if not moving:
            sgn = cmp(self.crane_pos, 0)
        return sgn
    
    def move_tower(self):
        print self.__dict__
        
        sgn = self.get_speed_sign()
        speed = self.calculate_tower_speed(sgn, self.tower_pos)
        self.tower_vel = speed * self.tower_factor #int(speed * self.tower_factor)
        self.tower_pos += self.position_delta() 
        
        print "tower_vel %f" %self.tower_vel
        print "tower pos %f" %self.tower_pos
        if abs(self.tower_pos) >= int(49*self.tower_factor): 
            self.tower_vel = abs(self.tower_vel) * cmp(0,self.tower_pos)

    def position_delta(self):
        if(self.tower_vel>0):
           return int(math.ceil(self.tower_factor * self.tower_vel))
        else:
           return int(math.floor(self.tower_factor * self.tower_vel))
