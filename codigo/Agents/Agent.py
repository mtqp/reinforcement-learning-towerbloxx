#coding=utf-8
from random import random

from environment import Environment

class Agent(object):
    def __init__(self, environment):
        self.environment = environment
