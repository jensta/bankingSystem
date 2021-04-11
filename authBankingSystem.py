#Initializing the system
import random
from datetime import datetime
now = datetime.now()

database = {} #dictionary

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

    userAccountNumber = int(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for accountNumber, userDetails in database.items():
        if(accountNumber == userAccountNumber):
            if(userDetails[3]== password):
                bankOperation(userDetails)

    print("Invalid account number or password\n Remember! You must have a REGISTERED account")
    login()
    

def register(): #Collecting First and Last Name, Email and Password

    print("******** Register for a New Account ******** \n")

    email = input("What is your email address? \n")
    firstName = input("What is your first name? \n")
    lastName = input("What is your last name? \n")
    password = input("What would you like your password to be? \n")

    accountNumber = getAccountNumber()

    database[accountNumber] = [firstName, lastName, email, password ]

    print("Your account has been created \n")
    print("Your accout number is: %d \n" % accountNumber)

    login()

def bankOperation(user): #Provides bank operations

    print("******** Welcome %s %s ********" % (user[0], user[1]))
    balance = 70.50
    print("Your starting balance is $%d" % balance)
    
    selectedOption = int(input("What would you like to do?\n[1] Deposit\n[2] Withdraw\n[3] Report Complaint\n[4] Logout\n[5] Exit\n"))
     
    if(selectedOption == 1):
        depositOperation(balance)
    elif(selectedOption == 2):
        withdrawlOperation(balance)
    elif(selectedOption == 3):
        complain()
    elif(selectedOption == 4):
        logout()
    elif(selectedOption == 5):
        exit()
    else: 
        print("Invalid Option")
        bankOperation(user)

def depositOperation(balance): 
    confirmDeposit = int(input('\n Would you like to continue with your Deposit?\n[1] Continue with Deposit\n[2] Logout\n[3] Exit\n'))
    if(confirmDeposit == 1):
        depAmount = int(input("How much would you like to deposit?\n"))
        balance += depAmount
        print('Updated Balance: %d \n Thank you. Have a Nice Day!' % balance)
        exit()
    elif(confirmDeposit == 2):
        logout()
    elif(confirmDeposit == 3):
        exit()
    else:
        print("Invalid Option")
        depositOperation(balance)

def withdrawlOperation(balance):
    confirmWithdrawl = int(input('Would you like to continue with your Withdrawl?\n[1] Continue with Withdrawl\n[2] Logout\n[3] Exit\n'))
    if(confirmWithdrawl == 1):
        witAmount = int(input("How much would you like to withdraw?\n "))
        if(witAmount > balance):
            print("Insufficient Funds")
            exit()
        elif(witAmount <= balance):
            balance -= witAmount
            print('Amount Withdrawn: %d' % witAmount)
            print("Your remaining balance is %d\nThank you, Have a Nice Day" % balance)
            exit()
    elif(confirmWithdrawl == 2):
        logout()
    elif(confirmWithdrawl == 3):
        exit()
    else:
        print("Invalid Option")
        withdrawlOperation(balance)
    
def complain():
    confirmComplaint = int(input('Would you like to continue with your Complaint?\n[1] Continue with Complaint\n[2] Logout\n[3] Exit\n'))
    if(confirmComplaint == 1):
        complaint = input('What is the issue you would like to report?\n')
        print('You have stated " %s " \nThank you for contacting us, we will get back to you within 24 hours about the issue you have reported.' % complaint)
        exit()
    elif(confirmComplaint == 2):
        logout()
    elif(confirmComplaint == 3):
        exit()
    else:
        print('Invalid Option')      
        complain()      
                
def getAccountNumber(): #Provides account number to register function
    return random.randrange(1111111111,9999999999)

def logout():
    login()

### ACTUAL BANKING SYSTEM ###

init()