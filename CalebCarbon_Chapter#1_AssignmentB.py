#This script reads from a file of answers and prints a random one when asked a question.
#A while loop will continuously prompt the user to ask questions until they type 'quit' to break the loop.

#The random module is needed to select a random index from the list of answers.
import random

#Define main function.
def main():

    #Open txt file of answers in read mode.
    file = open("8ball_responses.txt", "r")

    #Create list responses to hold answers.
    responses = []

    #For each line in the answers file, append it to the responses list.
    for line in file:
        responses.append(line)

    #This while loops prompts the user to ask questions until they type 'quit'
    while True:

        #Variable question stores user input
        question = input("Ask a yes or no question, or type 'quit' to close the program")

        #Question is converted to lowercase so that inputs like 'Quit' or 'QUIT' will also break the while loop.
        question = question.lower()

        #If the user inputs 'quit', break the loop. If not, print a random response.
        if question == "quit":
            break
        else:
            print(responses[random.randrange(1,len(responses))])

#Call main()
main()