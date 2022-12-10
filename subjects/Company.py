import subjects
from env.Possession import Possession
import subjects.Subject


class Company(Possession, subjects.Subject.Subject):
    # Need to contain/do:
    # Can produce products
    # Can consume material
    # Can hire/fire Subjects
    # MUST pay Employees
    # Can bankrupt
    # Can be owned by a Subject
    # Can be owned by a Company

    # create a __init__ method which sets a name, the owner, the money
    def __init__(self, name: str = None, money: float = 1000, owner: subjects.Subject.Subject = None):
        self.name = name
        self.money = money
        self.owner = owner
        self.possessions = []
