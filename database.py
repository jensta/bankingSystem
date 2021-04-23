import os
import validation

userDBPath = "data/userRecord/"
authSessionPath = "data/authSession/"

def create(userAccountNumber,  firstName, lastName, email, password, balance):

    userData = firstName + ',' + lastName + ','+ email + ','+ password + ',' + str(0)

    if doesAccountNumberExist (userAccountNumber):
        return False

    if doesEmailExist (email):
        print("User already exists")
        return False

    completionStatus = False

    try:
        f =open(userDBPath + str(userAccountNumber) + ".txt", "x")

    except FileExistsError:
        doesFileContainData = read(userDBPath + str(userAccountNumber) + ".txt")
        if not doesFileContainData:
            delete(userAccountNumber) 
        #delete file if it already exists
        #delete(accountNumber)
        
    else: 
        f.write(str(userData))
        completionStatus = True

    finally:
        f.close()
        return completionStatus

    

def update(user):
    f = open(userDBPath + str(user[0]) + ".txt", "w")
    f.write(str(user))
    f.close()
    return True

def read(userAccountNumber):
    
    isValidAccountNumber = validation.accountNumberValidation(userAccountNumber)
    try:

        if isValidAccountNumber:
            f = open(userDBPath + str(userAccountNumber) + ".txt", "r")

        else:
            f = open(userDBPath + userAccountNumber, "r")

    except FileNotFoundError:
        print("File Not Found")

    except FileExistsError:
        print("User does not exist")

    except TypeError:
        print("Invalid Account Number Format") 

    else:
        return f.readline()

    return False


def delete(userAccountNumber):
    print("Delete User Record")

    isDeleteSuccessful = False

    if os.path.exists(userDBPath + str(userAccountNumber) + ".txt"):

        try:
            os.remove(userDBPath + str(userAccountNumber) + ".txt")
            isDeleteSuccessful = True

        except FileNotFoundError:
            print("User Not Found")

        finally:
            return isDeleteSuccessful

def doesEmailExist(email):

    allUsers = os.listdir(userDBPath)

    for user in allUsers:
        userList = str.split(read(user), ",")
        if email in userList:
            return True
    return False

def doesAccountNumberExist(accountNumber):

    allUsers = os.listdir(userDBPath)

    for user in allUsers:
        if user == str(accountNumber) + ".txt":
            return True
    return False


def authUser(accountNumber, password):

    if doesAccountNumberExist(accountNumber):
        
        user = str.split(read(accountNumber), ",")

        if password == user[3]:
            return user

    return False

def authCreate(user):
    f = open(authSessionPath + str(user[0]) + ".txt", "x")
    f.close()

def authDelete(user):
    os.remove(authSessionPath + str(user[0]) + ".txt")