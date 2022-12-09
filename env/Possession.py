from abc import ABC


class Possession(ABC):
    # Needs to contain/do:
    # - Has a Type (→Comparable!)
    # - Has a Name
    # - Can be owned
    # - Can be produced / OR is randomly given
    # - Can be consumed / break (True / False + When?)
    # - Quality / Productivity / Efficiency
    # - Can have fixed / variable costs

    def __init__(self, name, value, condition=1.0, owner=None, quality=1.0):
        # Represents the name of the possession, which could be used to identify and distinguish it from other
        # possessions.
        self.name = name

        # Represents the value of the possession, which could be used to track its financial worth or usefulness.
        self.value = value

        # Represents the condition of the possession, which could be used to track its state (e.g. damaged, broken)
        self.condition = max(0.0, min(1.0, condition))

        # Represents the owner of the possession, which could be used to track who currently possesses it
        self.owner = owner

        # Represents the quality of the possession, which could be used to track its durability or lifespan.
        self.quality = quality

    def use(self):
        # Use the possession (e.g. consume its resources, or activate its functionality)
        pass

    def repair(self):
        # Repair the possession (e.g. restore its condition, or fix its damage)
        pass

    def transfer(self, subject):
        # Transfer the possession to another subject (e.g. trade or gift it)
        pass

    # Create an empty list to store all the possessions
    all_possessions = []

    # Define a function to create a new possession
    @staticmethod
    def create_possession(name, value):
        # Create a new possession instance
        possession = Possession(name, value)

        # Add the possession to the global list
        Possession.all_possessions.append(possession)

        # Return the possession instance
        return possession
