#This program prompts the user to enter any umber of sentences, then it uses a regular expression to capture each sentence and a for loop to repeat them back to the user individually. 

#Import regular expressions
import re

#Define main()
def main():

    #Get input from user.
    s = input("Enter your sentances: ")

    #This regular expression matches sentences, even those begining in numbers.
    pat = r'[A-Z\d].*?[.!?](?= [A-Z]|\s\d|$)'

    #Match all sentences and store them in a list.
    m = re.findall(pat, s, flags=re.DOTALL | re.MULTILINE)

    #Print the number of sentences to the user.
    print("There are {n} sentances".format(n = len(m)))

    #Print each sentence back to the user.
    for x in m:

        print(x)

#Call main()
main()