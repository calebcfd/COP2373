#Function main() asks for a user input and uses a for each loop to compare it against a list of 30 known spam keywords.
#Then it notifies the user of how many keywords were found, the likelihood the input message is spam, and the keywords found.

#Define main()
def main():
    
    #Flags is a list of keywords often included in spam emails.
    flags = ["Act now!", "Apply now!", "Call now!", "Don't hesitate!", "For only", "Get started now", "Limited time", "Great offer",
             "Instant", "Now only", "Offer expires", "Once in a lifetime", "Order now", "Order today", "Special promotion", "Urgent",
             "While supplies last", "Bonus", "All new", "Amazing", "Certified", "Congratulations", "Fantastic deal", "For free", "Guaranteed",
             "Outstanding value", "Risk free", "Satisfaction guaranteed", "Free", "Free!"]
    
    #Counter tracks the number of spam keywords found.
    counter = 0

    #Used will store the found spam keywords.
    used = []

    #Mail stores user input
    mail = input("Copy your email here to ckeck for spam:")

    #This for loop checks the user input for each spam indicator in the flags list, and if found, increments the counter by 1 and appends the keyword to the used list.
    for phrase in flags:

        #The .find() method is case sensitive to better match spam typography.
        if mail.find(phrase) != -1:

            counter += 1
            used.append(phrase)

    #Liklihood uses a chain of ternary operators to evaluate the possibility of spam based on how many keywords were found.
    likelihood = "unlikely to be" if counter == 0 else "possibly" if counter == 1 else "likely to be" if counter == 2 else "certainly"

    #Join the list of used keywords into a string.
    used_string = ", ".join(used)

    #Print to the user how many keywords were found, the liklihood of spam, and what keywords used indicated spam.
    print("Your email contained {0} keywords indicative of spam, and is {1} spam".format(counter, likelihood))
    print('The phrases used that indicate spam are: ' + used_string)

#Call main()
main()