#coding=utf-8

import unittest

from environment import Environment


class TestEnvironmentStates(unittest.TestCase):

    def setUp(self):
        self.visited_statuses = set()
        self.environment = Environment(crane_pos=-15, crane_dir=1)
    
    def make(self, action):
        s,r = self.environment.make_action(action)
        self.visited_statuses.add(s)
        return s,r
        
    def make_many(self, quantity, action):
        for i in range(quantity):
            self.make(action)
            
    def test_singleton_states(self):
        self.make_many(2000, Environment.PASS)
        self.assertEqual(len(self.visited_statuses),196)
    
    def test_one_throw(self):
        self.make(Environment.THROW)
        self.make_many(2000, Environment.PASS)
        self.assertEqual(len(self.visited_statuses),196)
    
    def test_almost_not_missing_throw(self):
        self.make_many(4, Environment.PASS)
        self.make(Environment.THROW)
        self.make_many(200, Environment.PASS)
        self.assertEqual(len(self.visited_statuses),196)
        
    def test_not_missing_throw(self):
        self.make_many(5, Environment.PASS)
        s,r = self.make(Environment.THROW)
        self.assertTrue(s.has_finished())
