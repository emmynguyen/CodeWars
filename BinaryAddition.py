#Binary Addition

#Task: Implement a function that adds two numbers together
#and returns their sum in binary. The conversion can be done
#before, or after the addition. 

#Output: THe binary number returned should be a string.

#Prompt user to input two numbers
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

#Create a function
def add_binary(a,b):
    total_sum = a + b
    bin_sum = bin(total_sum)
    print("Equivalent Binary Number: ",bin_sum[2:])
    return a, b

#Call the function
add_binary(a,b)