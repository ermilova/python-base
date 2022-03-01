BUY = "buy"
FILL = "fill"
TAKE = "take"
REMAINING = "remaining"
EXIT = "exit"
BACK = "back"


class StockItem:

    def __init__(self, store):
        self.store = store

    def fill(self):
        print(self.fill_question())
        x = int(input())
        self.store += x

    def dec(self, x):
        if self.store < x.store:
            raise Exception()
        self.store -= x.store

    def contain(self, x):
        return self.store >= x.store

    def get(self):
        return self.store


class Milk(StockItem):

    def __repr__(self):
        return "{} ml of milk".format(self.store)

    def fill_question(self):
        return "Write how many ml of milk you want to add:"


class Water(StockItem):

    def __repr__(self):
        return "{} ml of water".format(self.store)

    def fill_question(self):
        return "Write how many ml of water you want to add:"


class Beans(StockItem):

    def __repr__(self):
        return "{} g of coffee beans".format(self.store)

    def fill_question(self):
        return "Write how many grams of coffee beans you want to add:"


class Cups(StockItem):

    def __repr__(self):
        return "{} disposable cups".format(self.store)

    def fill_question(self):
        return "Write how many disposable cups of coffee you want to add:"


class Money(StockItem):

    def __repr__(self):
        return "${} of money".format(self.store)

    def make_empty(self):
        self.store = 0


COFFEE = []
COFFEE.append({"water": Water(250), "milk": Milk(0), "beans": Beans(16),
               "cups": Cups(1), "money": Money(-4)})
COFFEE.append({"water": Water(350), "milk": Milk(75), "beans": Beans(20),
               "cups": Cups(1), "money": Money(-7)})
COFFEE.append({"water": Water(200), "milk": Milk(100), "beans": Beans(12),
               "cups": Cups(1), "money": Money(-6)})


class CoffeeMachine:

    def __init__(self):
        self.storage = {"water": Water(400),
                        "milk": Milk(540),
                        "beans": Beans(120),
                        "cups": Cups(9),
                        "money": Money(550)}

    def __str__(self):
        str_ = ""
        for item in self.storage:
            str_ += self.storage[item].__repr__() + "\n"
        return str_

    def check(self, coffee_type):
        for key in self.storage:
            if not self.storage[key].contain(coffee_type[key]):
                print(f"Sorry, not enough {key}!")
                return False
        print("I have enough resources, making you a coffee!")
        return True

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        user_input = input()
        if user_input != BACK:
            drink_type = int(user_input) - 1
            if self.check(COFFEE[drink_type]):
                for key in self.storage:
                    self.storage[key].dec(COFFEE[drink_type][key])

    def fill(self):
        for key in self.storage:
            if key != "money":
                self.storage[key].fill()

    def take(self):
        print("I gave you $" + str(self.storage["money"].get()))
        self.storage["money"].make_empty()
        return machine


machine = CoffeeMachine()
while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == BUY:
        machine.buy()
    elif action == FILL:
        machine.fill()
    elif action == TAKE:
        machine.take()
    elif action == REMAINING:
        print(machine)
    else:
        break
