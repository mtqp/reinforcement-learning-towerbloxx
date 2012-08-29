#coding=utf-8

import unittest

from environment import Environment


class TestEnvironmentBounds(unittest.TestCase):
    
    def setUp(self):
        self.environment = Environment()
    
    def _bounded_building_test(self, crane_offset):
        initial_state, final_state = self.environment.start()
        
        
        finish = False
        count_until = 200
        while not finish and count_until:
            self.environment.crane_pos = self.environment.tower_pos + crane_offset
            response = self.environment.make_action(Environment.THROW)
            if "PERDISTE" in response:
                finish = True
            self.assertLessEqual(abs(self.environment.tower_pos), 49)
            count_until -= 1
        
        self.assertTrue(bool(count_until))
    
    def test_bounded_right_building(self):
        for offset in range(1,11):
            self._bounded_building_test(offset)
            self.environment = Environment()
    
    def test_bounded_left_building(self):
        for offset in range(-1,-11,-1):
            self._bounded_building_test(offset)
            self.environment = Environment()
    

class TestEnvironmentBalancing(unittest.TestCase):
    pass

class TestEnvironmentStates(unittest.TestCase):
    def test_singleton_states(self):
        e = Environment()
        statuses = set()
        for i in range(2000):
            s,r = e.make_action(Environment.PASS)
            statuses.add(s)
        print len(statuses)
        self.assertTrue(len(statuses) == 196)