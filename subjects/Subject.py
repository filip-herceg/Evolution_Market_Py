class Subject:
    # Needs to contain/do:
    # Possess possessions
    # Sell possessions
    # Buy possessions
    # Place bids
    # Can consume items
    # Can manage owned company
    # Can bankrupt

    isBank = bool

    def __init__(self):
        is_bank = self.__check_bank()

    def __check_bank(self):
        if type(self).__name__ == "Bank":
            return "true"
        return "false"
