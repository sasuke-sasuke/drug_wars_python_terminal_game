#class Player: health, stash size, money,  # class Drugs: drugs, prices #title screen #instructions #class City #main screen with menu showing inv.. stash and current inv. #class LoanShark #class Police #random occurances #how long to win #
from random import randrange, randint

cities = ["West Palm Beach", "Boynton Beach",
          "Boca Raton", "Lake Worth", "Pahokee", "Belle Glade"]


class Player:

    def __init__(self):
        self.money = 2000
        self.trench_coat = 100
        self.health = 100
        self.day = 1
        self.max_day = 31
        self.drugs = {"cocaine": 0, "herion": 0,
                      "acid": 0, "weed": 0, "speed": 0, "ludes": 0}
        self.stash = {"cocaine": 0, "herion": 0,
                      "acid": 0, "weed": 0, "speed": 0, "ludes": 0}
        self.guns = 0
        self.bank = 0
        self.debt = 5500
        self.location = "West Palm Beach"
        self.game_over = False

# switch_location takes in new_location, drugs object anc cartel object
    def switch_location(self, new_location, drugs, cartel):
        if new_location != self.location:
            self.location = new_location
            drugs.cities_drug_prices()
            self.advance_one_day(cartel)

    def add_drugs_to_trench_coat(self, drug, quantity):
        if self.trench_coat > 0 + quantity:
            self.trench_coat -= quantity
            #self.drugs[drug] += quantity

    def take_drugs_from_trench_coat(self, drug, quantity):
        if self.trench_coat <= 100 - quantity:
            self.trench_coat += quantity
            #self.drugs[drug] -= quantity

    def buy_drugs(self, drug, quantity, cost_per_quantity):
        if drug not in self.drugs.keys():
            self.drugs[drug] = 0
        self.drugs[drug] += quantity
        self.money -= (cost_per_quantity * quantity)
        self.add_drugs_to_trench_coat(quantity)

    def sell_drugs(self, drug, quantity, price_per_quantity):
        if self.drugs[drug] > 0:
            self.drugs[drug] -= quantity
            self.money += (quantity * price_per_quantity)
            self.take_drugs_from_trench_coat(quantity)

    def take_damage(self, damage):
        if self.health > 0:
            self.health -= damage
            self.game_over()

    def game_over(self):
        if self.health <= 0 or self.day == 32:
            self.game_over = True

    def bought_gun(self, num_of_guns):
        self.guns += num_of_guns

    def deposit_money(self, amount):
        if amount <= self.money:
            self.bank += amount
            self.money -= amount

    def withdrawl_money(self, amount):
        if amount <= self.bank:
            self.money += amount
            self.bank - + amount

    def add_drugs_stash(self, drug, amount):
        for key in self.drugs.keys():
            if key == drug and self.drugs[drug] > 0 + amount:
                self.take_drugs_from_trench_coat(amount)
                self.stash[drug] += amount

    def remove_drugs_stash(self, drug, amount):
        for key in self.stash.keys():
            if key == drug and self.stash[drug] > 0 + amount:
                self.add_drugs_to_trench_coat(amount)
                self.stash[drug] -= amount

    def advance_one_day(self, cartel):
        if self.day <= self.max_day:
            self.day += 1
            if self.debt > 0:
                self.debt = cartel.interest_accumulation()
                cartel.loan_days += 1
        else:
            self.game_over()

    def game_over(self):
        score = self.money * 2
        self.game_over = True
        return int(score / 1000000)


# drugs is a random price between min and max, prices change in different cities and on different days.
class Drugs:
    # drug_price_ranges from index 0: cocaine, herion, acid, weed, speed, ludes
    drug_price_ranges = [[15000, 30000], [5000, 14000],
                         [1000, 4500], [300, 900], [70, 250], [10, 60]]

    def __init__(self, current_city):
        self.cities = cities
        self.current_city = current_city
        self.prices_in_city = {"cocaine": 0, "herion": 0,
                               "acid": 0, "weed": 0, "speed": 0, "ludes": 0}

    def random_drug_price(self, drug, min, max):
        if len(str(min)) >= 4:
            price = randrange(min, max, 100)
            self.prices_in_city[drug] = price
        else:
            price = randrange(min, max, 2)
            self.prices_in_city[drug] = price
        return price

    def cities_drug_prices(self):
        index = 0
        for drug in self.prices_in_city.keys():
            price = self.random_drug_price(
                drug, self.drug_price_ranges[index][0], self.drug_price_ranges[index][1])
            self.prices_in_city[drug] = price
            index += 1


# The Loan Sharks - will try to kill you after so many days of non payment, interest builds eavh day


class Cartel:
    loan_days = 0
    loan_days_max = 8

    def __init__(self):
        self.name = "Wendy Bryde"
        self.loan_amount = 5500
        self.loan_max = 250000
        self.health = 100
        self.interest = 0.20  # in percentage

    def loan_money(self, user, loan_amount):
        if self.loan_amount <= self.loan_max:
            self.loan_amount += loan_amount
            user.money += loan_amount
            user.debt += loan_amount
            self.loan_days += 1

    def repay_loan(self, user, repay_amount):
        if self.loan_amount >= 0:
            self.loan_amount -= repay_amount
            user.money -= repay_amount
            user.debt -= repay_amount
            if user.debt == 0:
                self.loan_days = 0

    def interest_accumulation(self):
        if self.loan_amount > 0:
            self.loan_amount += self.loan_amount * self.interest
        return int(self.loan_amount)


class Police:

    def __init__(self, name):
        self.name = name
        self.deputies = randint(1, 9)
        self.health = 100


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


def game_menu(user):

    print(
        "\n     DATE: Jan {date}, 1984                         TRENCH COAT POCKETS     {pockets}".format(date=user.day, pockets=user.trench_coat))
    print("""
 ==============================================================================
||       STASH       ||      """+user.location+"""     ||      TRENCH COAT         ||
|=============================================================================|
|       COCAINE                  """+str(user.stash["cocaine"])+""" ||      COCAINE                       """+str(user.drugs["cocaine"])+"""    |
|       HERION                   """+str(user.stash["herion"])+""" ||      HERION                        """+str(user.drugs["herion"])+"""    |
|       ACID                     """+str(user.stash["acid"])+""" ||      ACID                          """+str(user.drugs["acid"])+"""    |
|       WEED                     """+str(user.stash["weed"])+""" ||      WEED                          """+str(user.drugs["weed"])+"""    |
|       SPEED                    """+str(user.stash["speed"])+""" ||      SPEED                         """+str(user.drugs["speed"])+"""    |
|       LUDES                    """+str(user.stash["ludes"])+""" ||      LUDES                         """+str(user.drugs["ludes"])+"""    |
|                                  ||                                         |
|       BANK                     """+str(user.bank) + """ ||      GUNS                          """+str(user.guns)+"""    |
|       DEBT                  """+str(user.debt)+""" ||      CASH                       """+str(user.money)+"""    |
 =============================================================================
            """.format(current_city=user.location))


def cartel(user, cartel):
    choice = input("\nDo you want to visit the Cartel(loan shark): ")
    if choice == "y":
        repay_amount = input("\nHow much do you want to repay? ")
        try:
            repay_amount = int(repay_amount)
            cartel.repay_loan(user, repay_amount)
        except:
            repay_amount = 0
        borrow_amount = input("\nHow much do you want to borrow? ")
        try:
            borrow_amount = int(borrow_amount)
            cartel.loan_money(user, borrow_amount)
        except:
            borrow_amount = 0


def stash(user):
    choice = input("\nDo you wish to transfer drugs to/from your stash? ")
    if choice == "y":
        drug = input("\nWhich drug do you want to transfer? ")
        choice = input("\nAdd to stash or remove? (Pick add or remove) ")
        if choice[0].lower() == "a":
            if drug[0].lower() in ["c", "h", "a", "w", "s", "l"]:
                amount = input("\nHow much do you wish to transfer? ")
                try:
                    amount = int(amount)
                    user.add_drugs_stash(drug, amount)
                except:
                    print("\nNo changes to stash")
        if choice[0] == "r":
            amount = input("\nHow much do you want to remove? ")
            try:
                amount = int(amount)
                user.remove_drugs_stash(drug, amount)
            except:
                print("\nNo changes made to stash")


def bank(user):
    choice = input("\nDo you wish to visit the bank? ")
    if choice == "y":
        choice = input("\nDo you want to deposit or withdrawl? ")
        if choice[0].lower() == "d":
            deposit_amount = input("How much do you wish to deposit? ")
            try:
                deposit_amount = int(deposit_amount)
                user.deposit_money(deposit_amount)
            except:
                print("\nNo deposit made.")
        if choice[0].lower() == "w":
            withdrawl_amount = input("\nHow much do you wish to withdrawl? ")
            try:
                withdrawl_amount = int(withdrawl_amount)
            except:
                print("\nNo withdrawl made.")

# inputs player class as user and drug class as drugs


def drug_menu(user, drugs, cartel):
    cocaine = drugs.prices_in_city["cocaine"]
    herion = drugs.prices_in_city["herion"]
    acid = drugs.prices_in_city["acid"]
    weed = drugs.prices_in_city["weed"]
    speed = drugs.prices_in_city["speed"]
    ludes = drugs.prices_in_city["ludes"]
    print("\nHey dude, the prices of drugs here are:\n")
    print("""
                    COCAINE     {cocaine}             WEED    {weed}
                    HERION      {herion}              SPEED   {speed}
                    ACID        {acid}              LUDES   {ludes}
    """.format(cocaine=cocaine, weed=weed, herion=herion, speed=speed, acid=acid, ludes=ludes))

    choice = input("\nWill you buy, sell or jet? ")
    while choice[0].lower() not in ['b', 's', 'j']:
        choice = input("\nWill you buy, sell, or jet?(pick 'b', 's' or 'j') ")
    if choice[0].lower() == 'b':
        drug = input("\nWhat will you buy? ")

        amount = input("\n How much {drug} will you buy?(Can afford {afford}) ".format(
            drug=drug, afford=int(user.money / drugs.prices_in_city[drug])))
        try:
            amount = int(amount)
            user.buy_drugs(drug, amount, drugs.prices_in_city[drug])
        except:
            print("\nNo transaction made")

    if choice[0].lower() == 's':
        drug = input("\nWhat will you sell? ")

        amount = int(input("\nHow much {drug} you sell? ".format(drug=drug)))
        try:
            user.sell_drugs(drug, amount, drugs.prices_in_city[drug])
        except:
            print("\nNo sale was made")
    if choice[0].lower() == 'j':
        print("""\n
Where to dude:      1) West Palm Beach      2) Boynton Beach        3) Boca Raton
(Select 1 - 6)      4) Lake Worth           5) Pahokee              6) Belle Glade       
        """)
        travel = int(input("\nWhere do you want to go? "))
        new_city = cities[travel - 1]
        user.switch_location(new_city, drugs, cartel)
        print(user.day)
        print(user.trench_coat)
    else:
        pass


def game(user, drugs, loan_shark):
    already_visited = False
    choice = title_screen()
    instructions(choice)
    while user.game_over == False:
        if user.location == "West Palm Beach" and already_visited == False:
            game_menu(user)
            cartel(user, loan_shark)
            game_menu(user)
            stash(user)
            game_menu(user)
            bank(user)
            already_visited = True
        game_menu(user)
        drug_menu(user, drugs, loan_shark)
        if user.location != "West Palm Beach":
            already_visited = False


# Instantiate player, cartel and drugs
user = Player()
wendy = Cartel()
drugs = Drugs("West Palm Beach")
drugs.cities_drug_prices()
#####################################

game(user, drugs, wendy)

#choice = title_screen()
# instructions(choice)
# game_menu(user)
# stash(user)
# bank(user)
#user.game_over = False
# game_menu(user)
#drug_menu(user, drugs)
# game_menu(user)
#drug_menu(user, drugs)
# print(drugs.prices_in_city)
