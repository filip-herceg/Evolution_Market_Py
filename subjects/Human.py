import math
import random
from sympy import *
x, y = symbols('x y')

import subjects.Subject


class Human(subjects.Subject.Subject):
    name = str
    surname = str

    #Personality start
    risk = float
    friendliness = float
    greed = float
    #Personality end

    money = 100
    health = 1
    alive = "true"

    def __init__(self):         #Constructor of class Human
        self.default_stats()


    def get_info(self): #UNFINISHED
        print("Risk: ", self.risk)

    def default_stats(self):
        self.risk = self.__mutation(0.5)
        self.friendliness = self.__mutation(0.5)
        self.greed = self.__mutation(0.5)

    def __mutation(self, feature):                      #Feature (m) is the x value where func1 and func2 cross
        #Uses sympy lirbary to calculate

        funca = x ** 2 / feature ** 2                   #First functinon: f(x)
        integrala = Integral(funca, (x, 0, feature))    #Integral of first Function
        randomnum = random.random()                     #Random number between 0 and 1

        if randomnum <= feature:    #Is this compare even correct?
            print("randomnum: ", randomnum)             #DELETE ME
            print("integrala: ", integrala.doit())      #doit() means "return decimal instead of formula" DELETE ME
            ###CONTINUE

        if randomnum > feature:
            funcb = (x-1)**2 / (1-feature)**2
            integralb = Integral(funcb, (x, feature, 1))
            ###CONTINUE


    def check_death(self):
        if (self.health == 0):
            alive = "false"

    def inherit(self):
        pass
