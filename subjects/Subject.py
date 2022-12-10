from typing import List
from env.Debt import Debt
from env.Possession import Possession
from subjects.Bank import Bank


class Subject:
    # Create a class attribute to store the instances of the class
    subject_list = []

    def __init__(self, money: float = 100, name: str = None):
        self.debts: List[Debt] = []
        self.name = name
        self.money = money
        Subject.subject_list.append(self)

    def __check_bank(self):
        # Check if the subject is a Bank instance
        return isinstance(self, Bank)

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

    # Can transfer a possession to another subject
    def transfer_possession(self, subject: 'Subject', possession: Possession):
        # Check if the subject owns the possession
        if possession.owner == self:
            # Transfer possession
            possession.owner = subject
        else:
            print("The subject does not own the possession")

    @classmethod
    def list_subjects(cls):
        return cls.subject_list
