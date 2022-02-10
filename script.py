#class Player: health, stash size, money,  # class Drugs: drugs, prices #title screen #instructions #class City #main screen with menu showing inv.. stash and current inv. #class LoanShark #class Police #random occurances #how long to win #
import random

cities = ["West Palm Beach", "Boynton Beach",
          "Boca Raton", "Lake Worth", "Pahokee", "Belle Glade"]


class Player:

    def __init__(self):
        self.money = 2000
        self.stash_size = 100
        self.health = 100
        self.drugs = {}
        self.guns = 0
        self.bank = 0
        self.debt = -5000
        self.location = 0
        self.game_over = False

    def switch_location(self, new_location):
        if new_location != self.location:
            self.location = new_location

    def buy_drugs(self, drug, quantity, cost_per_quantity):
        if drug not in self.drugs.keys():
            self.drugs[drug] = 0
        self.drugs[drug] += quantity
        self.money -= (cost_per_quantity * quantity)

    def sell_drugs(self, drug, quantity, price_per_quantity):
        if self.drugs[drug] > 0:
            self.drugs[drug] -= quantity
            self.money += (quantity * price_per_quantity)

    def take_damage(self, damage):
        if self.health > 0:
            self.health -= damage
            self.game_over()

    def game_over(self):
        if self.health <= 0:
            self.game_over = True


# drugs is a random price between min and max, prices change in different cities and on different days.
class Drugs:
    cocaine = random.randint(15000, 30000)
    herion = random.randint(5000, 14000)
    acid = random.randint(1000, 4500)
    weed = random.randint(300, 900)
    speed = random.randint(70, 250)
    ludes = random.randint(10, 60)

    def __init__(self, city):
        self.city = ""

# 6 cities to travel between, as you move to each city 1 game day will pass


class City:

    def __init__(self):
        pass

# The Loan Sharks - will try to kill you after so many days of non payment, interest builds eavh day


class Cartel:

    def __init__(self, name):
        self.name = name


class Police:

    def __init__(self, name):
        self.name = name
        self.deputies = random.randint(1, 9)


############################
def title_screen():
    print("\n         Drug Wars\n")
    print("         A Game Based On\n")
    print("         The Palm Beach Drug Market\n\n")
    print("         Inspired by the 1984 'Drug Wars' game\n")
    print("         By Jeof Petty\n")
    instructions_choice = input("Do You Want Instructions? ")
    instructions_choice = instructions_choice.lower()
    while "y" not in instructions_choice and "n" not in instructions_choice:
        instructions_choice = input(
            "Do You Want Instructions? Type 'y' or 'n' ")
        instructions_choice = instructions_choice.lower()
    return instructions_choice


def instructions(instructions_choice):
    if instructions_choice == 'n':
        return
    print("""\n
    This is a game of buying, selling, and fighting. The object of the game is 
    to pay off your debt to the Cartel. Then, make as much money as you 
    can in a 1 month period. If you deal too heavily in drugs, you might 
    run into the police! Your main drug stash will be in West Palm Beach.
    The prices of drugs per unit are:

            Cocaine         15,000 - 30,000
            Heroin          5,000 - 14,000
            Acid            1,000 - 4,500
            Weed            300 - 900
            Speed           70 - 250
            Ludes           10 - 60
    \n""")
    input("(Hit Any Key To Start Game)")
    return


def game_loop(user):
    while user.game_over == False:
        pass


#######
user = Player()
choice = title_screen()
instructions(choice)
