import math
import random
from sympy import *
x, y = symbols('x y')

import subjects.Subject


class Human(subjects.Subject.Subject):
    name = str
    surname = str

    risk = float
    friendliness = float
    greed = float
    money = 100
    health = 1
    alive = "true"

    def __init__(self):
        self.default_stats()


    def get_info(self): #UNFINISHED
        print("Risk: ", self.risk)

    def default_stats(self):
        self.risk = self.__mutation(0.5)
        self.friendliness = 0.5
        self.greed = 0.5

    def __mutation(self, feature):
        funca = x ** 2 / feature ** 2
        randomnum = random.random()
        if (randomnum < feature):
            integrala = Integral(funca, (x, 0, feature))
            print("randomnum: ", randomnum)
            print("integrala: ", integrala.doit())

    def check_death(self):
        if (self.health == 0):
            alive = "false"

    def inherit(self):
        pass
