class CoffeeMachine():
    def __init__(self, water=400, milk=540, coffee_beans=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money
        
    def user_input(self):
        while True:
            action = input(
                "Write action (buy, fill, take, remaining, exit):\n")

            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.remaining()
            elif action == "exit":
                exit()

    def buy(self):
        coffee_type = input(
            "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

        if coffee_type == "1":
            if self.water >= 250 and self.coffee_beans >= 16 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffee_beans -= 16
                self.money += 4
                self.cups -= 1
            else:
                if self.water < 250:
                    print("Sorry, not enough water!")
                elif self.coffee_beans < 16:
                    print("Sorry, not enough coffee beans!")
                elif self.cups <= 0:
                    print("Sorry, not enough cups!")

        elif coffee_type == "2":
            if self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.money += 7
                self.cups -= 1
            else:
                if self.water < 350:
                    print("Sorry, not enough water!")
                elif self.milk < 75:
                    print("Sorry, not enough milk!")
                elif self.coffee_beans < 20:
                    print("Sorry, not enough coffee beans!")
                elif self.cups <= 0:
                    print("Sorry, not enough cups!")

        elif coffee_type == "3":
            if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.money += 6
                self.cups -= 1
            else:
                if self.water <= 350:
                    print("Sorry, not enough water!")
                elif self.milk < 75:
                    print("Sorry, not enough milk!")
                elif self.coffee_beans < 12:
                    print("Sorry, not enough coffee beans!")
                elif self.cups <= 0:
                    print("Sorry, not enough cups!")

        elif coffee_type == "back":
            self.user_input()

    def fill(self):

        self.water += int(
            input("Write how many ml of water do you want to add:\n"))
        self.milk += int(
            input("Write how many ml of milk do you want to add:\n"))
        self.coffee_beans += int(
            input("Write how many grams of coffee beans do you want to add:\n"))
        self.cups += int(
            input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0

    def remaining(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee_beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")

newMachine = CoffeeMachine()
newMachine.user_input()
