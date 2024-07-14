#This program defines the Money class, a subclass of Decimal. Then, it guides the user through through a test function that uses each of the class' methods.


from decimal import Decimal

#Define Money Class
class Money(Decimal):

    #The __new__ and __init__ methods are the same as in the textbook.
    def __new__(cls, v, units='USD'):
        return super(Money, cls).__new__(cls, v)
    
    def __init__(self, v, units='USD'):
        self.units = units

    #Define the dunder methods for add, sub, and mul.
    #Each method takes an argument, converts it into a Decimal, performs the desired operation, and rounds to two decimal places. The resulting Decimal object is called 'product'.
    #Variable product is used to return a new Money object.
    def __add__(self, obj2):

        product = round(Decimal(self) + Decimal(obj2), 2)

        return Money(product, 'USD')
    
    def __sub__(self, obj2):
        
        product = round(Decimal(self) - Decimal(obj2), 2)
        
        return Money(product, 'USD')
    
    def __mul__(self, obj2):
        
        product = round(Decimal(self) * Decimal(obj2), 2)
        
        return Money(product, 'USD')
    

#Define the test function
def test_func():

    #Variable m is the money object used in the test function.
    m = Money('0', 'USD')

    #Inform the user that this is the test function and the starting value is 0.
    print("This is the test function for the Money class")
    print("Your Money object has a starting value of 0 USD")

    #Variable a stores the user input that will be added to m.
    a = input("Enter an amount to add to your Money object: ")

    #Use the __add__ method to perform the operation.
    m += Decimal(a)

    #Notify the user of the new value.
    print("Your Money object is now ", m, m.units)

    #Print a new line for readability.
    print('\n')

    #Variable s stores the user input that will be subtracted from m.
    s = input("Enter an amount to subtract from your Money object: ")

    #Use the __sub__ method to perform the operation.
    m -= Decimal(s)

    #Notify the user of the new value.
    print("Your Money object is now ", m, m.units)

    #Print a new line for readability.
    print('\n')

    #Variable x stores the user input that will multiply the value of m.
    x = input("Enter an amount to multiply your Money object by: ")

    #Use the __mul__ method to perform the operation.
    m *= Decimal(x)

    #Notify the user of the new value.
    print("Your Money object is now ", m, m.units)


#Call the test function.
test_func()


