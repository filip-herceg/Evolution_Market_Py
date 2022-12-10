from typing import List

import env.Debt as Debt
import env.Possession
import subjects.Bank as Bank


class Subject:
    # This attribute represents the name of the subject, which could be used to identify and distinguish it from
    # other subjects.
    name: str

    # This attribute represents the amount of currency that a human has to spend on buying and selling items.
    money: float

    # This attribute represents the items that a human owns, such as cars, houses, or other valuable assets.
    possessions: List[env.Possession]

    def __init__(self, name: str = None, money: float = 100):
        self.debts: List[Debt] = []
        self.name = name
        self.money = money

    def __check_bank(self):
        # Check if the subject is a Bank instance
        return isinstance(self, Bank.Bank)

    # Can transfer money to another subject
    def transfer_money(self, subject: 'Subject', amount: float):
        # Check if the subject is a Bank instance
        if self.__check_bank():
            # Check if the bank has enough money to transfer
            if self.money >= amount:
                # Transfer money
                self.money -= amount
                subject.money += amount
            else:
                print("Insufficient funds")
        else:
            # Check if the subject has enough money to transfer
            if self.money >= amount:
                # Transfer money
                self.money -= amount
                subject.money += amount
            else:
                print("Insufficient funds")
