def accountNumberValidation(accountNumber):

    if accountNumber:

        try:
            int(accountNumber)

            if len(str(accountNumber)) == 10:

                return True

        except ValueError: 
            return False
        except TypeError:
            return False
    return False

def isNumber(input):
    if input:
        try:
            float(input)
            return True
        except ValueError:
            print("Input should be a number")
            return False
    else:
        print("This is a required field")
        return False