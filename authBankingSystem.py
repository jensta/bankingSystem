#Inializing the system
import random
import validation
import database
from getpass import getpass

from datetime import datetime
now = datetime.now()



def init():
    print("******** Welcome to Bank Python ******** ")

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S \n")
    print("Current Date and Time ", dt_string)
    
    haveAccount = int(input("Do you have an account with us? Please enter [1]'YES' or [2]'NO' \n"))

    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("Invalid Option")
        init()

def login(): #Needs account number and password

    print("******** Login ********  \n")

    userAccountNumber = (input("What is your account number? \n"))

    isValidAccountNumber = validation.accountNumberValidation(userAccountNumber)

    if isValidAccountNumber: 

        password = getpass("What is your password \n")

        user = database.authUser(userAccountNumber, password)
        
        if user:
            database.authCreate(user)
            bankOperation(user)

        print("Invalid account number or password\n Remember! You must have a REGISTERED account")
        login()
    
    else:
        print("Account Number Invaild: check that you have 10 digits and only intergers")
        init()
    

def register(): #Collecting First and Last Name, Email and Password

    print("******** Register for a New Account ******** \n")

    email = input("What is your email address? \n")
    firstName = input("What is your first name? \n")
    lastName = input("What is your last name? \n")
    password = getpass("What would you like your password to be? \n")

    accountNumber = getAccountNumber()

    isUserCreated = database.create(accountNumber, firstName,  lastName, email,  password, {"Balance" : 0})

    if isUserCreated:
        print("Your account has been created \n")
        print("Your accout number is: %d \n" % accountNumber)

        login()
    else: 
        print("Something went wrong, please try again")
        register()



def bankOperation(user): #Provides bank operations

    print("******** Welcome %s %s ********" % (user[0], user[1]))

    
    selectedOption = int(input("What would you like to do?\n[1] Deposit\n[2] Withdraw\n[3] Report Complaint\n[4] Logout\n[5] Exit\n"))
     
    if(selectedOption == 1):
        depositOperation(user)
    elif(selectedOption == 2):
        withdrawlOperation(user)
    elif(selectedOption == 3):
        complain(user)
    elif(selectedOption == 4):
        logout(user)
    elif(selectedOption == 5):
        exit()
    else: 
        print("Invalid Option")
        bankOperation(user)

def depositOperation(user): 

    confirmDeposit = int(input('\n Would you like to continue with your Deposit?\n[1] Continue with Deposit\n[2] Logout\n[3] Exit\n'))
    if(confirmDeposit == 1):
        print(f"You have ${user['Balance']} in your account")
        while True:
            amountDeposit = input("How much would you like to deposit? \n")
            if validation.isNumber(amountDeposit):
                amountDeposit = float(amountDeposit)
                break
                
        user["Balance"] = user["Balance"] + amountDeposit
        database.update(user)
        print(f"Your new balance is ${user['Balance']}")
    elif(confirmDeposit == 2):
        logout(user)
    elif(confirmDeposit == 3):
        exit()
    else:
        print("Invalid Option")
        depositOperation(user)

def withdrawlOperation(user):

    confirmWithdrawl = int(input('Would you like to continue with your Withdrawl?\n[1] Continue with Withdrawl\n[2] Logout\n[3] Exit\n'))
    if(confirmWithdrawl == 1):
         print(f"You have ${user['Balance']} in your account")

    while True:
        amountWithdrawn = input("How much would you like to withdraw? \n")
        if validation.isNumber(amountWithdrawn):
            amountWithdrawn = float(amountWithdrawn)
            break

    if(amountWithdrawn <= user["Balance"]):
        user["Balance"] = user["Balance"] - amountWithdrawn
        database.update(user)
        print(f"Take your cash. Your new balance is ${user['Balance']}")
        
    elif(amountWithdrawn > user["Balance"]):
        print(f"You do not have enough money in your account for this withdrawal, please select a number smaller than {user['Balance']}")
        withdrawlOperation(user)
    elif(confirmWithdrawl == 2):
        logout(user)
    elif(confirmWithdrawl == 3):
        exit()
    else:
        print("Invalid Option")
        withdrawlOperation(user)
    
def complain(user):
    confirmComplaint = int(input('Would you like to continue with your Complaint?\n[1] Continue with Complaint\n[2] Logout\n[3] Exit\n'))
    if(confirmComplaint == 1):
        complaint = input('What is the issue you would like to report?\n')
        print('You have stated " %s " \nThank you for contacting us, we will get back to you within 24 hours about the issue you have reported.' % complaint)
        exit()
    elif(confirmComplaint == 2):
        logout(user)
    elif(confirmComplaint == 3):
        exit()
    else:
        print('Invalid Option')      
        complain(user)      
                
def getAccountNumber(): #Provides account number to register function
    return random.randrange(1111111111,9999999999)

def logout(user):
    database.authDelete(user)
    login()

### ACTUAL BANKING SYSTEM ###

init()