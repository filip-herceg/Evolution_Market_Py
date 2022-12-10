from subjects.Subject import Subject


class Bank(Subject):
    bank_list = []
    # Can give loans for interest
    # Owns and sells Items of dead Humans for ½ price
    # Wants to maximize profit as well
    # Has determined personality
    # Can have contracts with other Subjects

    def __init__(self, name: str = None, money: float = 1000):
        super().__init__(money, name)
        Bank.bank_list.append(self)


    @classmethod
    def list_banks(cls):
        return cls.bank_list
