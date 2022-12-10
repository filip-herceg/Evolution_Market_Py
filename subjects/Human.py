import random

import scipy.stats as stats

from subjects.Subject import Subject
from subjects.Bank import Bank
from subjects.Company import Company
import scipy


class Human(Subject):
    human_list = []

    def __init__(self, name: str = None, surname: str = None, money: float = 100, parent: 'Human' = None,
                 traits: list = None):
        super().__init__(money, name)
        self.health = 1
        self.name = name
        self.surname = surname
        self.money = money
        self.possessions = []
        self.human_list.append(self)

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

        # If a parent is not specified, generate random values for each trait or use the specified traits
        else:
            self.set_traits(traits)

    @classmethod
    def set_traits(cls, traits):
        # If a list of traits is specified, use those values
        if traits is not None:
            cls.risk_taking = traits[0]
            cls.social_skills = traits[1]
            cls.greediness = traits[2]
            cls.intelligence = traits[3]
            cls.empathy = traits[4]
            cls.honesty = traits[5]
            cls.persistance = traits[6]
            cls.creativity = traits[7]
        # If a list of traits is not specified, generate random values for each trait
        else:
            cls.risk_taking = random.uniform(0, 1)
            cls.social_skills = random.uniform(0, 1)
            cls.greediness = random.uniform(0, 1)
            cls.intelligence = random.uniform(0, 1)
            cls.empathy = random.uniform(0, 1)
            cls.honesty = random.uniform(0, 1)
            cls.persistance = random.uniform(0, 1)
            cls.creativity = random.uniform(0, 1)

    # Write a get_info method which returns a string containing the name, surname, money, and traits of the human
    def get_info(self):
        return f"Name: {self.name} {self.surname}, Money: {self.money}, Traits: {self.risk_taking}, " \
               f"{self.social_skills}, {self.greediness}, {self.intelligence}, {self.empathy}, {self.honesty}, " \
               f"{self.persistance}, {self.creativity} "

    # Remove human instance if health is 0 and transfer all possessions to the bank
    def check_health(self):
        if self.health == 0:
            # Transfer all possessions to the bank
            for possession in self.possessions:
                self.transfer_possession(Bank.list_banks()[0], possession)

            # Remove human instance and all references to it
            self.human_list.remove(self)
            self.subject_list.remove(self)
            del self

    def die(self):
        self.health = 0
        self.check_health()

    # Write a method which returns a list of all humans
    @classmethod
    def list_humans(cls):
        return cls.human_list

    # Write a method which creates a company and adds it to the list of companies.
    # The company should be owned by the human and the higher the spending money
    # the better is the companys quality
    def create_company(self, name: str, spending_money: float):
        # Check if the human has enough money to create the company
        if self.money >= spending_money:
            # Create the company
            company = Company(name, spending_money, self)
            # Transfer money to the company
            self.transfer_money(company, spending_money)
        else:
            print("Insufficient funds")


def _mutate_trait(trait: float, std: float = 0.1) -> float:
    # Generate a random value from a normal distribution with mean 0 and the specified standard deviation
    mutation_amount = stats.norm.rvs(0, std)

    # Add the mutation amount to the original trait value
    mutated_trait = trait + mutation_amount

    # Make sure the mutated trait is in the range 0 to 1
    if mutated_trait < 0:
        mutated_trait = 0
    elif mutated_trait > 1:
        mutated_trait = 1

    return mutated_trait
