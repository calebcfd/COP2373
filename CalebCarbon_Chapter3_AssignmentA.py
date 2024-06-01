
#Function main() houses two functions called verified_cost() and catalogue(). catalogue() uses a while loop to recieve and store user inputs until the user types 'quit'.
#verified_cost() is used by catalogue() to ensure a user's input can be converted to an integer or a float, and if not, it prompts the user to try again.
#After catalogue() is called, the user inputs are stored in variable 'list'. Three new variables 'total', 'highest', and 'lowest' are then calculated using the reduce() method and printed to the user.
#If the user ends catalogue() before inputing any values, calculating variables 'total', 'highest', and 'lowest' are skipped and the user is notified that the program has ended.



#Import regular expressions and functools.
import re
import functools

#Define main().
def main():


    #Define verified_cost(), which ensures that inputs can be converted to integers or floats.
    def verified_cost():

        #Variable 'amount' stores user input.
        amount = input("Enter expense amount using digits. Exclude special characters:")

        #This if/else statement uses the isdigit() method to check if input can be converted to an integer or float. If conversion is impossible, recur the function to prompt another input.
        if amount.isdigit():

            amount = int(amount)
            return amount
        
        #The replace method is used to check for only one decimal point. Addidtional decimals will cause the isdigit() method to return False.
        elif amount.replace('.', '', 1).isdigit():

            amount = float(amount)
            return amount
        
        else:
            print("Please use only digits and decimals to input expense amount")
            return verified_cost()


    #Define catalogue(), which will store user inputs and return them when halted by the user.
    def catalogue():

        #Variable 'expenses' will store inputs as a 2D list.
        expenses = []

        #This while loop asks for user inputs until broken by the input 'quit', insensitive to case.
        while True:
            
            #Variable 'type' stores expense type, or ends user input cycle if 'quit' is entered, insensitive to case. 
            type = input("Enter expense type, or type 'quit' to finish entering expenses:")

            #Use a regular expression to check if 'type' starts and ends with 'quit'. If so, findall() will have a length of one and the while loop will break.
            if len(re.findall("(?i)^quit$", type)) == 1:
                break

            #Use verified_cost() to get user input and convert it to an integer or float.
            cost = verified_cost()

            #Append the expense type and cost to 'expenses'
            expenses.append([type, cost])
        
        return expenses

    #Call catalogue() and store the results in variable 'list'.
    list = catalogue()

    #If variable 'list' is not empty, proceed to calculate and display expenses. If not, notify the user that the program is closing.
    if len(list) >= 1:

        #Variable 'total' uses the reduce() method and a lambda function to sum all expenses.
        total = functools.reduce(lambda a, b: [ "placeholder", a[1]+b[1] ], list)

        #Convert total from a list to a number.
        total = total[1]

        #Variable 'highest' uses the reduce() method and a lambda function to find the highest of all expenses.
        highest = functools.reduce(lambda a, b: a if a[1] > b[1] else b, list)

        #Variable 'lowest' uses the reduce() method and a lambda function to find the lowest of all expenses.
        lowest = functools.reduce(lambda a, b: a if a[1] < b[1] else b, list)

        #Print variables 'total', 'highest', and 'lowest' to the user, formatting to be easily readable.
        print("Total of expenses is: {:.2f}".format(total))

        print("Highest expense is {type} at ${cost:.2f} ".format(type=highest[0], cost=highest[1]))

        print("Lowest expense is {type} at ${cost:.2f} ".format(type=lowest[0], cost=lowest[1]))

    else:
        print("Program terminated.")

#Call main().
main()
