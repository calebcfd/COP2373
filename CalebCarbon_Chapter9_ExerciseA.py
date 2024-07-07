
#This program defines a class called BankAcc.
#Then a separate function called test_function walks the user through creating a new instance of the class and using each of the class' methods.

#Define new class.
class BankAcc:
    
    #__init__ method takes arguments name, number, amount, and rate and sets them to properties of the same name.
    def __init__(self, name, number, amount, rate):

        self.name = name
        self.number = number
        self.amount = amount
        self.rate = rate

    #__str__ method formats class properties in a readable manner.
    def __str__(self):

        return f"Account Name: {self.name}\nAccount Number: {self.number}\nAccount Balance: ${self.amount:.2f}\nInterst Rate: %{self.rate*100}"

    #Method set_rate() gets user input and converts it to a float. The input is divided by 100 to make it a percentage and then set as the interest rate.
    def set_rate(self):
        
        new_rate = float(input("Enter the new yearly interest rate as a number. \nFor example, to set intrest rate to 5%, enter 5: "))
        new_rate = new_rate/100

        self.rate = new_rate

    #Method withdraw() prompts the user for a number, subtracts it from the account balance, and notifies the user of the process.
    def withdraw(self):

        withdrawn = float(input("Enter amount to withdraw as a number. Exclude special characters like '$': "))

        self.amount = self.amount - withdrawn

        print("${:.2f} withdrawn. Balance is now ${:.2f}".format(withdrawn, self.amount))

    #Method withdraw() prompts the user for a number, adds it to the account balance, and notifies the user of the process.
    def deposit(self):

        deposited = float(input("Enter amount to deposit as a number. Exclude special characters like '$': "))

        self.amount = self.amount + deposited

        print("${:.2f} deposited. Balance is now ${:.2f}.".format(deposited, self.amount))

    #Method get_balance() prints the balance to the user and returns the account balance number.
    def get_balance(self):

        print("Balance is ${:.2f}.".format(self.amount))

        return self.amount

    #Method calc_interest() prompts the user for a number of days, calculates the amount of interest as variable interest, and prints it to the user.
    def calc_interest(self):

        days = int(input("Calculate interest for how many days: "))

        interest = self.amount*self.rate*(days/365)

        print("In {} days, ${:.2f} in interest will accrue.".format(days, interest))


#Function test_function() guides the user through making a BankAcc class instance and using each of the class' methods on it.
def test_function():

    #This section of print statements informs the user what processes are about to take place
    print("This is the test function for the BankAcc class.")
    print("Follow the prompts to make an account and view it as a string.")
    print("Then, each method will be used to set the interest rate, withdraw, deposit, check balance, and calculate interest.")
    print("Finally, review your account with the new object string.")

    #These variables take input from the user and are used to make a new BankAcc class.
    name = input("Enter a name for the account: ")

    number = input("Enter a number for the account: ")

    amount = float(input("Enter the starting balance for the account as a number. Exclude special characters like '$': "))

    rate = float(input("Enter the yearly interest rate as a number. \nFor example, to set intrest rate to 5%, enter 5: "))

    #Variable rate is divided by 100 to make a percentage.
    rate = rate/100

    #A new BankAcc instance is created as new_acc.
    new_acc = BankAcc(name, number, amount, rate)

    #Use the BankAcc __str__ method to print the class object to the user.
    print(new_acc)

    #Individually go through each of the class' methods.
    new_acc.set_rate()

    new_acc.withdraw()

    new_acc.deposit()

    new_acc.get_balance()

    new_acc.calc_interest()

    #Print the class object to the user with the changes they have made.
    print(new_acc)


#Call test_function()
test_function()

    