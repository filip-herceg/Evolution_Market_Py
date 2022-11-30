import random

from sympy import *

x, y = symbols('x y')

import subjects.Subject


class Human(subjects.Subject.Subject):
    name = str
    surname = str

    # Personality start
    risk = float
    friendliness = float
    greed = float
    # Personality end

    money = 100
    health = 1
    alive = "true"

    def __init__(self):  # Constructor of class Human
        self.default_stats()
        self.get_info()

    def get_info(self):
        print("Risk: ", self.risk)
        print("Friendliness: ", self.friendliness)
        print("Greed: ", self.greed)

    def default_stats(self):
        self.risk = self.__mutation(0.5)
        self.friendliness = self.__mutation(0.5)
        self.greed = self.__mutation(0.5)

    def __mutation(self, feature):  # Feature (m) is the x value where func1 and func2 cross
        # Uses sympy lirbary to calculate

        # First functinon: f(x)
        funca = x ** 2 / feature ** 2

        # Integral of first Function
        integrala = Integral(funca, (x, 0, feature))

        # Second function: g(x)
        funcb = (x - 1) ** 2 / (1 - feature) ** 2

        # Integral of second Function
        integralb = Integral(funcb, (x, feature, 1))

        # Sum of both integrals
        sumintegral = integrala + integralb

        # Random number between 0 and 1
        randomnum = random.random()

        # Part of sum of integrals (0 % - 100%)
        partintegral = randomnum * sumintegral

        if partintegral <= integrala:
            resultfunc = ((x ** 3) / (3 * (feature ** 2))) - partintegral
            result = nsolve(resultfunc, x)
            return result

        else:
            resultfunc = (feature / 3) + (((x ** 3 / 3) - x ** 2 + x) / ((1 - feature) ** 2)) - (
                        ((feature ** 3 / 3) - feature ** 2 + feature) / ((1 - feature) ** 2)) - partintegral
            result = nsolve(resultfunc, x)
            return result

    def check_death(self):
        if (self.health == 0):
            alive = "false"

    def inherit(self):
        pass
