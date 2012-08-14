#coding=utf-8
import math
class Environment(object):
    THROW = 1
    PASS = 0

    EOE = "EOE"
    MAX_HEIGHT = 100
    
    def initialize(self):
        self.crane_direction = -1 #{-1;1}
        self.crane_pos = -49#-49 #[-49,49]
        self.tower_vel = 0 #[-5,5]
        self.tower_pos = 0 #[-49,49]
        self.tower_height = 0
        self.tower_factor = 0
        self.tower_size = 10
        self._state = None
        
    def __init__(self):
        self.initialize()
    
    def start(self):
        self.initialize()
        initial_state = self.state()
        return initial_state

    def make_action(self, action):
        if not self._correct_action(action):
            return "UNKNOWN ACTION"

        previous_tower_factor = self.tower_factor
        
        self._update_tower_state(action)

        self._move_tower()
        self._move_crane()

        next_state = self.state()
        reinforcement = self._get_reward(action, previous_tower_factor)
        
        ####
        print self.tower_factor
        if self._state == Environment.EOE:
            if reinforcement > 0:
                print "GANASTESS!"
            else:
                print "PERDISTESS!"
        #####
        
        return (next_state, reinforcement)

    def _correct_action(self, action):
        return action == Environment.THROW or action == Environment.PASS

    def _get_reward(self, action, comparison_factor):
        reinforcement = 0
        improved_tower_balance = self.tower_factor <= comparison_factor
        
        if self._has_new_floor(action):
            if improved_tower_balance:
                reinforcement = 100
            else:
                reinforcement = 20
        else:
            if action == Environment.THROW:
                reinforcement = -20 #negativo por haber fallado
            else:
                reinforcement = -1 #negativo por no haber tirado
        
        if not self._is_tower_raised():
            reinforcement = -100

        return reinforcement

    #[MDS] --> un piso se agrega si queda a +- size/2 de la posicion del 
    #--------> piso anterior
    #PRE: NO se movió el crane
    def _has_new_floor(self, action):
        has_new_floor = False
        if action == Environment.THROW:
            drop_offset = abs(self._get_drop_offset_from_tower())
            has_new_floor = drop_offset <= self.tower_size/2    
        
        return has_new_floor

    def _get_drop_offset_from_tower(self):
        if self.tower_pos == 0:
            return self.crane_pos

        if self.crane_pos == 0:
            return self.tower_pos

        same_sign = (self.crane_pos * self.tower_pos) > 0

        crane = abs(self.crane_pos)
        tower = abs(self.tower_pos)
        
        crane_sgn = cmp(self.crane_pos, 0)

        if same_sign:
            return crane_sgn * (crane - tower)
        else:
            return crane_sgn * (crane + tower)
        
    #PRE: NO se movió el crane           
    def _update_tower_state(self, action):
        if self._has_new_floor(action):
            self.tower_height += 1
            self._update_tower_factor()
            if self.tower_height > Environment.MAX_HEIGHT or not self._is_tower_raised():
                self._state = Environment.EOE

    #PRE: El crane cae sobre el edificio
    def _update_tower_factor(self):
        drop_offset = self._get_drop_offset_from_tower()
     
        if drop_offset != 0: ##sino no modifico el movimiento del edificio
            drop_right = drop_offset > 0 #se si lanzo a izquierda o derecha del ultimo piso
            tower_right = self.tower_pos > 0 #se para que lado se mueve la torre
            
            centers_from_left = drop_right and not tower_right
            centers_from_right= not drop_right and tower_right
            tower_balanced = self.tower_factor == 0.0
            
            increase_stability =  centers_from_left or centers_from_right
            increase_stability &= not tower_balanced
            
            #TODO: la cuenta de la estabilizacion no me parece real...            
            normalize_offset = abs(drop_offset) / 100.0
            normalize_height = (self.tower_height + 1)/100.0

            if increase_stability:
                self.tower_factor -= 0.1 + normalize_offset + normalize_height
                if self.tower_factor < 0: #por si se estabiliza "de mas"
                    self.tower_factor = 0
            else:
                self.tower_factor += 0.1 + normalize_offset + normalize_height

    def _is_tower_raised(self):
        return self.tower_factor <= 0.99

    def _calculate_tower_speed(self, sgn, pos):
        vel =  (5 - abs(pos)/10) 
        return vel * sgn

    def state(self):
        if self._state:
            return self._state
        else:
            return (self.tower_vel, self.tower_pos, self.crane_pos, self.crane_direction)

    def _move_crane(self):
        if abs(self.crane_pos) == 49:
            self.crane_direction = -self.crane_direction
        
        self.crane_pos += self.crane_direction
    
    # [MDS] --> no quedo lo suficientemente prolijo!
    # --> cmp(0,0) da cero, x lo tanto no podes romper el equilibrio
    def _get_speed_sign(self):
        moving = self.tower_vel != 0
        sgn = 0

        if moving:
            sgn = cmp(self.tower_vel,0)
        else:
            sgn = cmp(self.crane_pos, 0)
        return sgn
    
    def _move_tower(self):        
        sgn = self._get_speed_sign()
        speed = self._calculate_tower_speed(sgn, self.tower_pos)
        self.tower_vel = self._round_up_far_from_zero(speed * self.tower_factor)
        
        if(self.tower_factor != 0):
            self.tower_pos += self._round_up_far_from_zero(self.tower_factor * self.tower_vel)
        else:
            self.tower_pos = 0

        tower_off_boundaries = abs(self.tower_pos) > int(49*self.tower_factor)
        if tower_off_boundaries: 
            reversed_pos_sgn = cmp(0,self.tower_pos)
            self.tower_vel = abs(self.tower_vel) * reversed_pos_sgn

    def _round_up_far_from_zero(self, value): #--> QUE FEO NOMBRE!!! :P
        if(value>0):
           return int(math.ceil(value))
        else:
           return int(math.floor(value))    
   
