class Subject:
    isBank = bool

    def __init__(self):
        isBank = self.__check_bank()

    def __check_bank(self):  # works!
        if type(self).__name__ == "Bank":
            return "true"
        return "false"
