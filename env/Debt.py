import subjects.Subject as Subject


class Debt:
    def __init__(self, amount: float, time: int, debtor: 'Subject.Subject', creditor: 'Subject.Subject'):
        self.amount = amount
        self.time = time
        self.debtor = debtor
        self.creditor = creditor
        # the debtor cannot be the creditor
        if self.debtor == self.creditor:
            raise Exception("The debtor cannot be the creditor")

    # the debtor can pay the creditor
    # if the debtor has enough money to pay the creditor, the debtor pays the creditor
    # if the debtor does not have enough money to pay the creditor, the debtor cannot pay the creditor
    # if the debtor pays the creditor, the amount of the debt decreases
    # cannot pay more than the amount of the debt
    def pay(self, amount: float):
        # check if the debtor has enough money to pay the creditor
        if self.debtor.money >= amount:

            # if the too much money is paid, the payment amount is set to the amount of the debt
            if self.amount < amount:
                amount = self.amount

            # the debtor pays the creditor
            self.debtor.transfer_money(self.creditor, amount)
            # the amount of the debt decreases
            self.amount -= amount
            # if the amount of the debt is less than or equal to 0, the debt is paid off
            if self.amount == 0:
                self.debtor.debts.remove(self)
                self.creditor.debts.remove(self)

        # if the debtor does not have enough money to pay the creditor, the debtor cannot pay the creditor
        else:
            print("Insufficient funds")
