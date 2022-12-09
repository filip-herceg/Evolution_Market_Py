import random
from typing import Dict

import env.Item
import env.Possession
import subjects.Bank


class Subject:
    # This attribute represents the name of the subject, which could be used to identify and distinguish it from
    # other subjects.
    name: str

    # This attribute represents the amount of currency that a human has to spend on buying and selling items.
    money: float
    # isBank: bool

    # This attribute represents the items that a human owns, such as cars, houses, or other valuable assets.
    possessions: int

    def __init__(self, name: str, personality: Dict[str, float]):
        self.name = name
        self.personality = personality

    def __check_bank(self):
        # Check if the subject is a Bank instance
        if isinstance(self, subjects.Bank.Bank):
            return "true"
        return "false"

        # This method allows the subject to purchase items from the market, using its money and possessions.

    def buy(self, item: env.Item.Item):
        # Use the subject's personality traits to determine how much they are willing to pay for the item
        price = item.value * (1 + self.personality["greed"] - self.personality["frugality"])

        # If the subject has enough money to buy the item, make the purchase
        if self.money >= price:
            self.possessions.append(item)
            self.money -= price
            print(f"{self.name} bought {item.name} for ${price:.2f}.")
        else:
            print(f"{self.name} doesn't have enough money to buy {item.name}.")

    # This method allows the subject to sell items to the market, in exchange for money or other possessions.
    def sell(self, item: env.Item.Item):
        # Use the subject's personality traits to determine how much they are willing to sell the item for
        price = item.value * (1 - self.personality["greed"] + self.personality["frugality"])

        # If the subject has the item to sell, make the sale
        if item in self.possessions:
            self.possessions.remove(item)
            self.money += price
            print(f"{self.name} sold {item.name} for ${price:.2f}.")
        else:
            print(f"{self.name} doesn't have {item.name} to sell.")

    # This method allows the subject to interact with other subjects, such as by trading items or exchanging
    # information.
    def interact(self):
        # Use the subject's personality traits to determine how much they are willing to interact with other subjects
        if random.random() < self.personality["extroversion"]:
            # If the subject is willing to interact, choose a random subject to interact with
            subject = random.random.choice(self.all_subjects)
            print(f"{self.name} interacted with {subject.name}.")
        else:
            print(f"{self.name} didn't interact with anyone.")

    def check_possession(self):
        # Create an empty list to store the subject's possessions
        possessions = []

        # Iterate over the list of all possessions in the simulation
        for possession in self.all_possessions:
            # If the possession's owner is the subject, add the possession to the list
            if possession.owner == self:
                possessions.append(possession)

        # Return the list of possessions
        return possessions

    # make the all possessions list
    all_possessions: env.Possession.Possession = []
    # make the all subjects list
    all_subjects: subjects.Subject.Subject = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name
