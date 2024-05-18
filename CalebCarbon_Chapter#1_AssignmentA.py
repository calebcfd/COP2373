
#This script uses a while loop and an accululator to track customer inputs until a total of 20 is reached.
#Non-integer inputs are filtered out by trying the int() function and excepting ValueErrors.
#If/else statements are used to limit user inputs between 1 and 4.

#Define main function.
def main():

    #Variable tickets_sold will act as the accumulator.
    tickets_sold = 0

    #Variable total_sales tracks the number of successful orders.
    total_sales = 0

    #This while loop uses tickets_sold to continuously prompt users to buy tickets untill 20 are sold.
    while tickets_sold < 20:

        #Here, a try/except statement tries to convert user input to an integer. If the user input a character string instead, they will recieve an error notice.
        try:
            request = int(input(str(20 - tickets_sold) + " tickets remain. How many, up to four, would you like?"))
        except ValueError:
            print("Please input an integer when requesting tickets.")

        #This if statement checks if the user input is between 1 and 4, and if there are enough tickets left to fulfill the order.
        if request > 0 and request < 5 and tickets_sold + request <= 20:

            #If the above condition is true, update tickets_sold, total_sales, and notify the user.
            tickets_sold += request
            total_sales += 1
            print("Order successful! " + str(request) + " tickets purchased.")

        #If the user input is an integer that does not satisfy sale conditions, notify the user.
        elif type(request) == int:
            print("The requested number of tickets are not available. Please try again.")

    #When all tickets are sold, the while loop will complete and this print statement will notify the user of total buyers.
    print("All tickets are sold out. There were", total_sales, "total buyers")

#Call main()
main()
