#Regex Validate PIN code

#Task: ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot
#contain anything but exactly 4 digits or exactly 6 digits.

#Import built-in package to work with Regular Expressions
import re

#Prompt user to input PIN code
pin = input("Enter a PIN code: ")

#Create a function that validates PIN codes
def validate_pin(pin):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:],."')
    if len(pin) == 4 or len(pin) == 6 and (regex.search(pin) == None) and pin.isnumeric():
        if pin >= "0000" and pin <= "9999" or pin >= "000000" and pin <= "999999":
            return True
        else:
            return False
            print("Wrong output for", pin)
    else:
        return False
        print("Wrong output for", pin)

#Call the function
validate_pin(pin)
