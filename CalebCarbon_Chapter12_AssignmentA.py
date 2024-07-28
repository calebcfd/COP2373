import numpy as np
import csv
import math

#This program reads data from a csv file as a numpy array. Statistics are caluculated and printed to the user.

#Function main() reads the csv file and converts it to an array. Then, it organizes the data and passes it to the stats() function to perform calculations.
#The stats() function returns the data and it is printed to the user.
def main():

    #Read the csv file, and make a numpy array out of it.
    with open('grades.csv', 'r') as f:

        #Variable reader is a csv reader of the grades file.
        reader = csv.reader(f)

        #Variable data hold the value of the grades file.
        data = list(reader)

        #Variable arr is the nump arr of the grades file.
        arr = np.array(list(data))

        #Print the first three rows to the user.
        print("First three rows of grades table: ")
        print(arr[0:3],"\n")

        #Variable filt_arr holds all row values as integers.
        filt_arr = arr[:, 2:]
        filt_arr = np.int_(filt_arr)

        
        #Variable exams is a list that holds each exam as another list.
        exams = []

        #This loop populates exams.
        for x in range(len(filt_arr[0])):
            exams.append(filt_arr[:, x])

        #Variable n is the accumlator that counts the number of exams.
        n = 0

        #For each exam, call stats() to get it's statistics, and print them to the user.
        for x in exams:
            n += 1
            exam_stats = stats(x)

            print("Exam",n,"Statistics:")
            print("Score Mean: ", exam_stats[0])
            print("Score Median: ", exam_stats[1])
            print("Standard Deviation: {0:.2f}".format(exam_stats[2]))
            print("Score Minimum: ", exam_stats[3])
            print("Score Maximum: ", exam_stats[4])
            print()


        #Variable all_values holds all values of all exams.
        all_values = []

        #This for loop populates all_values.
        for x in filt_arr:
            for y in x:
                all_values.append(y)


        #Call stats on all_values and print statistics for all exams.
        exam_stats = stats(all_values)

        print("All Exam Statistics:")
        print("Score Mean: ", exam_stats[0])
        print("Score Median: ", exam_stats[1])
        print("Standard Deviation: {0:.2f}".format(exam_stats[2]))
        print("Score Minimum: ", exam_stats[3])
        print("Score Maximum: ", exam_stats[4])
        
        

        

        

#Function stats() takes a list and returns the mean, median, standard deviation, minimum value, and maximum value of values in that list.
def stats(exam):

    #Variables mean, low, and high ititialize at certain values.
    mean = 0
    low = 100
    high = 0

    #This for loop modifies the values of mean, low, and high untill low and high are the lowest and highest values in exam, and mean is the sum.
    for x in exam:

        mean += x
        if x < low: low = x
        if x > high: high = x

    #Devide mean by the length of exam to get the average.
    mean = mean/len(exam)


    #If the exam has an odd length, the middle number is the median.
    if len(exam) % 2:
        median = exam[math.floor(len(exam)/2)]

    #If the exam has an even length, the median is the average of the middle two values.
    else:
        median = (exam[int(len(exam)/2)] + exam[int(len(exam)/2+1)])/2


    #Variable dev represents the standard deviation in the set.
    dev = 0

    for x in exam:

        dev += (x - mean)**2

    dev = dev/(len(exam)-1)

    dev = math.sqrt(dev)

    #Return the statistics.
    return [mean, median, dev, low, high]




#Call main()
main()


