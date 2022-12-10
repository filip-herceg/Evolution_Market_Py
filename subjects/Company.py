from env.Possession import Possession
from subjects.Subject import Subject


class Company(Possession, Subject):
    company_list = []
    # Need to contain/do:
    # Can produce products
    # Can consume material
    # Can hire/fire Subjects
    # MUST pay Employees
    # Can bankrupt
    # Can be owned by a Subject
    # Can be owned by a Company

    # create a __init__ method which sets a name, the owner, the money
    #
    def __init__(self, value, owner: Subject = None, name: str = None):
        super().__init__(value, name)
        self.name = name
        self.money = 0
        self.owner = owner
        self.possessions = []
        Company.company_list.append(self)

    @classmethod
    def list_companies(cls):
        return cls.company_list
