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
    if len(pin) == 4 or len(pin) == 6 and (regex.search(pin) == None):
        if pin.isnumeric() and pin.isdigit():
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

#Provided Test Cases

#Test.describe("validate_pin")

#Test.it("should return False for pins with length other than 4 or 6")
#Test.assert_equals(validate_pin("1"),False, "Wrong output for '1'")
#Test.assert_equals(validate_pin("12"),False, "Wrong output for '12'")
#Test.assert_equals(validate_pin("123"),False, "Wrong output for '123'")
#Test.assert_equals(validate_pin("12345"),False, "Wrong output for '12345'")
#Test.assert_equals(validate_pin("1234567"),False, "Wrong output for '1234567'")
#Test.assert_equals(validate_pin("-1234"),False, "Wrong output for '-1234'")
#Test.assert_equals(validate_pin("1.234"),False, "Wrong output for '1.234'")
#Test.assert_equals(validate_pin("00000000"),False, "Wrong output for '00000000'")

#Test.it("should return False for pins which contain characters other than digits")
#Test.assert_equals(validate_pin("a234"),False, "Wrong output for 'a234'")
#Test.assert_equals(validate_pin(".234"),False, "Wrong output for '.234'")
#Test.assert_equals(validate_pin("-123"),False, "Wrong output for '-123'")
#Test.assert_equals(validate_pin("-1.234"),False, "Wrong output for '-1.234'")
#Test.assert_equals(validate_pin("12.0"),False, "Wrong output for '12.0'")
#Test.assert_equals(validate_pin("123 "),False, "Wrong output for '123 '")
#Test.assert_equals(validate_pin("111-"),False, "Wrong output for '111-'")
#Test.assert_equals(validate_pin("123/"),False, "Wrong output for '123/'")
#Test.assert_equals(validate_pin("456:"),False, "Wrong output for '456:'")

#Test.it("should return True for valid pins")
#Test.assert_equals(validate_pin("1234"),True, "Wrong output for '1234'")
#Test.assert_equals(validate_pin("0000"),True, "Wrong output for '0000'")
#Test.assert_equals(validate_pin("1111"),True, "Wrong output for '1111'")
#Test.assert_equals(validate_pin("123456"),True, "Wrong output for '123456'")
#Test.assert_equals(validate_pin("098765"),True, "Wrong output for '098765'")
#Test.assert_equals(validate_pin("000000"),True, "Wrong output for '000000'")
#Test.assert_equals(validate_pin("123456"),True, "Wrong output for '123456'")
#Test.assert_equals(validate_pin("090909"),True, "Wrong output for '090909'")
