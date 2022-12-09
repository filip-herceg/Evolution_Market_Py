import random

from sympy import *

from subjects.Subject import Subject

x, y = symbols('x y')


class Humanoid(Subject):
    # Needs to contain/do:
    # Can die
    # Has personality
    # Has health
    # Can make Child
    # Genes can mutate
    # Has name and surname
    # Can have money ([equal/slightly unequal] starting money)

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

    def __init__(self):  # Constructor of class HomoOeconomicus
        super().__init__()
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

    @staticmethod
    def __mutation(feature):  # Feature (m) is the x value where func1 and func2 cross
        # Uses sympy lirbary to calculate

        # First functinon: f(x)
        funca = x ** 2 / feature ** 2

        # Integral of first Function
        integrala = Integral(funca, (x, 0, feature)).doit()

        # Second function: g(x)
        funcb = (x - 1) ** 2 / (1 - feature) ** 2

        # Integral of second Function
        integralb = Integral(funcb, (x, feature, 1)).doit()

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
           # resultfunc = (feature / 3) + (((x ** 3 / 3) - x ** 2 + x) / ((1 - feature) ** 2)) - (
            #        ((feature ** 3 / 3) - feature ** 2 + feature) / ((1 - feature) ** 2)) - partintegral
            resultfunc = ( ((3*(partintegral*feature*2) - 6*(partintegral*feature) + 3*partintegral - 1) / (2) ) + ( ((3*(partintegral*feature*2) - 6*(partintegral*feature) + 3*partintegral - 1) / (2) )**2 + (1-(-1)**2)**3)**(1/2))**(1/3) + ( ((3*(partintegral*feature*2) - 6*(partintegral*feature) + 3*partintegral - 1) / (2) ) - ( ((3*(partintegral*feature*2) - 6*(partintegral*feature) + 3*partintegral - 1) / (2) )**2 + (1-(-1)**2)**3)**(1/2))**(1/3) - 1 - x
            result = nsolve(resultfunc, x)
            return result

    def check_death(self):
        if self.health == 0:
            alive = "false"

    def inherit(self):
        pass
