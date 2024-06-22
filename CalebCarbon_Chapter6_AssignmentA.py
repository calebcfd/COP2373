#This program propts the user for a phone number, social security number, and zip code.
#Then it uses a function to validate the information by comparing it to a regular expression and notifies the user of the result.

#Import regular expressions.
import re


#Functions val_phone(), val_ssn(), and val_zip() take an argument and compare it to a regular expression. If there is a match, they return True, if not, False.
def val_phone(str_phone):

    #This regular expression allows for optional parenthesis around the area code and either dashes or spaces to separate groups.
    phone = re.findall('^\(?\d{3}\)?[\s-]\d{3}[\s-]\d{4}$', str_phone)

    return True if len(phone) else False
    

def val_ssn(str_ssn):

    #This regular expression excludes numbers with only zeros in a given group, the number 666 and numbers greater than 899 in the first group, and requires dahses between groups.
    ssn = re.findall('^([001-665]|[667-899]){3}-[01-99]{2}-[0001-9999]{4}$', str_ssn)

    return True if len(ssn) else False

    
def val_zip(str_zip):

    #This regular expression allows for basic 5 digit area codes or 9 digit hyphenated area codes.
    zip = re.findall('\d{5}(-\d{4})?$', str_zip)

    return True if len(zip) else False


#Function main() gets user input, useses functions val_phone(), val_ssn(), and val_zip() to validate it, and notifies the user of the result.
def main():
    
    #Get user input, and store as variables user_phone, user_ssn, and user_zip.
    user_phone = input("Enter phone number:")

    user_ssn = input("Enter social security number:")

    user_zip = input("Enter zip code")


    #If the user's input is verified, they will be notified that their input was valid.
    #If not, the user will be notified their input was not valid.
    if val_phone(user_phone):
        print(user_phone, " is a valid phone number.")
    else:
        print(user_phone, " is not a valid phone number")

    if val_ssn(user_ssn):
        print(user_ssn, " is a valid social security number.")
    else:
        print(user_ssn, " is not a valid social security number")

    if val_zip(user_zip):
        print(user_zip, " is a valid zip code.")
    else:
        print(user_zip, " is not a valid zip code")


#Call main()
main()
