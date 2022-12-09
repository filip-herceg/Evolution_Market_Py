import subjects.Subject


class Item:
    # This attribute represents the name of the item, which could be used to identify and distinguish it from other
    # items.
    name: str

    # This attribute represents the value of the item, which could be used to determine how much it is worth in the
    # market.
    value: float

    # This attribute represents the type of the item, which could be used to classify it as a physical item, stock,
    # or currency.
    type: str

    # This attribute represents the owner of the item, which could be used to track who possesses the item in the
    # simulation.
    owner: subjects.Subject.Subject

    def __init__(self, name: str, value: float, type: str):
        # Set the name, value, and type of the item
        self.name = name
        self.value = value
        self.type = type

    def buy(self, subject: subjects.Subject):
        # Check if the subject has enough money to buy the item
        if subject.money >= self.value:
            # Transfer the item to the subject and reduce their money by the item's value
            self.owner = subject
            subject.money -= self.value
            # Return True to indicate that the purchase was successful
            return True
        # Return False to indicate that the purchase failed
        return False

    def sell(self, subject: subjects.Subject):
        # Check if the item's owner is the subject
        if self.owner == subject:
            # Transfer the item to the subject and increase their money by the item's value
            self.owner = subject
            subject.money += self.value
            # Return True to indicate that the sale was successful
            return True
        # Return False to indicate that the sale failed
        return False

    def transfer(self, subject: subjects.Subject):
        # Transfer the item to the subject
        self.owner = subject
        # Return True to indicate that the transfer was successful
        return True
