import math
import random
from sympy import *

x, y = symbols('x y')

import subjects.Subject


class Human(subjects.Subject.Subject):
    def __init__(self, name: str = None, surname: str = None, money: float = 100, parent: 'Human' = None,
                 traits: list = None):
        super().__init__(name, money)
        self.health = 1
        self.name = name
        self.surname = surname
        self.money = money
        self.possessions = []

        # If a parent is specified, inherit personality traits from the parent
        if parent is not None:
            self.risk_taking = _mutate_trait(parent.risk_taking)
            self.social_skills = _mutate_trait(parent.social_skills)
            self.greediness = _mutate_trait(parent.greediness)
            self.intelligence = _mutate_trait(parent.intelligence)
            self.empathy = _mutate_trait(parent.empathy)
            self.honesty = _mutate_trait(parent.honesty)
            self.persistance = _mutate_trait(parent.persistance)
            self.creativity = _mutate_trait(parent.creativity)
        # If a parent is not specified, generate random values for each trait
        else:
            # If a list of traits is specified, use those values
            if traits is not None:
                self.risk_taking = traits[0]
                self.social_skills = traits[1]
                self.greediness = traits[2]
                self.intelligence = traits[3]
                self.empathy = traits[4]
                self.honesty = traits[5]
                self.persistance = traits[6]
                self.creativity = traits[7]
            # If a list of traits is not specified, generate random values for each trait
            else:
                self.risk_taking = random.uniform(0, 1)
                self.social_skills = random.uniform(0, 1)
                self.greediness = random.uniform(0, 1)
                self.intelligence = random.uniform(0, 1)
                self.empathy = random.uniform(0, 1)
                self.honesty = random.uniform(0, 1)
                self.persistance = random.uniform(0, 1)
                self.creativity = random.uniform(0, 1)

    # Write a get_info method which returns a string containing the name, surname, money, and traits of the human
    def get_info(self):
        return f"Name: {self.name} {self.surname}, Money: {self.money}, Traits: {self.risk_taking}, " \
               f"{self.social_skills}, {self.greediness}, {self.intelligence}, {self.empathy}, {self.honesty}, " \
               f"{self.persistance}, {self.creativity} "

    # Remove human instance if health is 0 and transfer all possessions to the bank
    def check_health(self):
        if self.health <= 0:
            self.transfer_possessions(self.bank)
            self = None # Remove human instance
    def die(self):
        self.health = 0
        self.check_health()

def _mutate_trait(trait):
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
