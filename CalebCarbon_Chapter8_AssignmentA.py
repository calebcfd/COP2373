import csv


#Define write()
def write():

    #Get input for the number of entries.
    n = int(input("How many entries will you make? Enter an integer: "))

    #Initialize output for later use.
    output = []

    #For as many times as the user specified in variable n, get input for first_name, last_name, and exam1-3, then append to output as a list.
    for x in range(n):

        first_name = input("Enter student first name: ")

        last_name = input("Enter student last name: ")

        exam1 = input("Enter first exam grade as an integer: ")

        exam2 = input("Enter second exam grade as an integer: ")

        exam3 = input("Enter third exam grade as an integer: ")

        output.append([first_name, last_name, exam1, exam2, exam3])

    #Open grades.csv as grades in append mode, specifying newline as an empty string to prevent empty lines by default.
    with open('grades.csv', 'a', newline='') as grades:

        #Create a writer
        csv_writer = csv.writer(grades)
        
        #Append an empty string to put the writer on a new line.
        csv_writer.writerow('')

        #Write each item in output as a line in grades.csv.
        for line in output:

            csv_writer.writerow(line)


#Define read()
def read():

    #Open grades.csv in read mode as grades.
    with open('grades.csv', 'r') as grades:

        #Create a reader.
        csv_reader = csv.reader(grades)

        #Print each following line in grades.csv, following the table format.
        for line in csv_reader:

            print('| {:15} | {:15} | {:6} | {:6} | {:6} |'.format(*line)) 


#Call write() and read()
write()
read()