class Possession():
    # Needs to contain/do:
    # - Has a Type (→Comparable!)
    # - Has a Name
    # - Can be owned
    # - Can be produced / OR is randomly given
    # - Can be consumed / break (True / False + When?)
    # - Quality / Productivity / Efficiency
    # - Can have fixed / variable costs

    def __init__(self, possession_type, name, value, condition=1.0, owner=None, quality=1.0):
        self.type = possession_type
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

    # Set the owner of the possession
    def set_owner(self, new_owner):
        self.owner = new_owner

    def transfer(self, new_owner):
        # Remove the possession from the old owner's possessions
        self.owner.possessions.remove(self)

        # Set the new owner of the possession
        self.owner = new_owner

        # Add the possession to the new owner's possessions
        self.owner.possessions.append(self)
