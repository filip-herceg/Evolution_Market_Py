import math
import random
from sympy import *
x, y = symbols('x y')

import subjects.Subject


class Human(subjects.Subject.Subject):
    name: str
    surname: str

    # PERSONALITY

    # This trait could influence how likely a human is to take risks, such as investing in the
    # stock market or starting a new business.
    risk_taking: float

    # This trait could influence how much a human values money and possessions, and how likely
    # they are to take advantage of others to acquire more.
    social_skills: float

    # This trait could influence how well a human is able to interact with others, and how likely
    # they are to form alliances or partnerships.
    greediness: float

    # This trait could influence how well a human is able to make decisions and solve problems,
    # which could affect their success in the market.
    intelligence: float

    # This trait could influence how well a human is able to understand and respond to the emotions
    # and needs of others, and how likely they are to help others or cooperate.
    empathy: float

    # This trait could influence how likely a human is to be truthful and trustworthy, and how likely
    # they are to cheat or deceive others.
    honesty: float

    # This trait could influence how likely a human is to persevere in the face of challenges or
    # obstacles, and how likely they are to give up or quit.
    persistance: float

    # This trait could influence how innovative and imaginative a human is, and how likely they are
    # to come up with new ideas or solutions.
    creativity: float

    def __init__(self):         #Constructor of class Human
        self.money = 100
        self.alive = "true"
        self.health = 1
        self.default_stats()


    def get_info(self): #UNFINISHED
        print("Risk: ", self.risk_taking)
        print("friendliness: ", self.social_skills)
        print("Greed: ", self.greediness)

    def default_stats(self):
        self.risk_taking = self.__mutate_trait(0.5)
        self.social_skills = self.__mutate_trait(0.5)
        self.greediness = self.__mutate_trait(0.5)

    def __mutate_trait(self, trait):
        # Generate a random value between 0 and 1 to determine how much mutation to apply
        mutation_factor = random.uniform(0, 1)

        # If the mutation factor is high, apply a small amount of mutation
        if mutation_factor > 0.8:
            trait += random.uniform(-0.1, 0.1)
        # If the mutation factor is low, apply a larger amount of mutation
        else:
            trait += random.uniform(-0.5, 0.5)

        # Make sure the personality value remains within the valid range of 0 to 1
        trait = max(0, min(trait, 1))

        return trait

    def inherit(self):
        pass
