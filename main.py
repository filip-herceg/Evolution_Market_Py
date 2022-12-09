import env.Possession
import subjects.Human

if __name__ == '__main__':
    human = subjects.Human.Human()
    bank = subjects.Bank.Bank()

    # Create a possession with an initial owner
    possession = env.Possession.Possession("Book", 10)
    possession.owner = human

    # Transfer the possession to a different subject
    possession.transfer(bank)

    # Check the possessions that are owned by a human
    human_possessions = human.check_possessions()

    # Check the possessions that are owned by a bank
    bank_possessions = bank.check_possessions()
