class Subject:
    # This attribute represents the name of the subject, which could be used to identify and distinguish it from other subjects.
    name: str

    # This attribute represents the amount of currency that a human has to spend on buying and selling items.
    money: float
    #isBank: bool

    # This attribute represents the items that a human owns, such as cars, houses, or other valuable assets.
    possessions: int


    def __init__(self):
        isBank = self.__check_bank()

    def __check_bank(self):  # works!
        if type(self).__name__ == "Bank":
            return "true"
        return "false"

    # This method allows the subject to purchase items from the market, using its money and possessions.
    def buy(self):
        pass

    # This method allows the subject to sell items to the market, in exchange for money or other possessions.
    def sell(self):
        pass

    # This method allows the subject to interact with other subjects, such as by trading items or exchanging
    # information.
    def interact(self):
        pass

    def check_possessions(self):
        # Create an empty list to store the subject's possessions
        possessions = []

        # Iterate over the list of all possessions in the simulation
        for possession in all_possessions:
            # If the possession's owner is the subject, add the possession to the list
            if possession.owner == self:
                possessions.append(possession)

        # Return the list of possessions
        return possessions
