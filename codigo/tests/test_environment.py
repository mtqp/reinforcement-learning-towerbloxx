#coding=utf-8
import math
import unittest

from environment import Environment

class TestEnvironmentStates(unittest.TestCase):

    def setUp(self):
        self.visited_statuses = set()
        self.environment = Environment(crane_pos=-15, crane_dir=1)
    
    def cant_states_without_new_floor(self):
        crane_cant_pos = len(range(-48,49))
        crane_cant_dir = 2
        cant_states = crane_cant_dir * crane_cant_pos
        return cant_states
    
    def do(self, action):
        s,r = self.environment.make_action(action)
        self.visited_statuses.add(s)
        return s,r
        
    def do_many(self, quantity, action):
        for i in range(quantity):
            last = self.do(action)
        return last
    
    def test_singleton_states(self):
        self.do_many(2000, Environment.PASS)    
        self.assertEqual(len(self.visited_statuses),self.cant_states_without_new_floor())
    
    def test_one_throw(self):
        self.do(Environment.THROW)
        self.do_many(2000, Environment.PASS)
        self.assertEqual(len(self.visited_statuses),self.cant_states_without_new_floor())
    
    def test_almost_not_missing_throw(self):
        self.do_many(4, Environment.PASS)
        self.do(Environment.THROW)
        self.do_many(200, Environment.PASS)
        self.assertEqual(len(self.visited_statuses),self.cant_states_without_new_floor())

    def test_not_missing_downgrade_stability_throw(self):
        self.do_many(12, Environment.PASS)
        s,r = self.do(Environment.THROW)
        self.assertFalse(s.has_finished())
        tower_speed, b, c, d = s.state_factors()
        self.assertLess(tower_speed,0)
