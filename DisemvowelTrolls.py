#Disemvowel Trolls

#Background: Trolls are attacking your comment section! A common way to deal 
#with this is to remove all of the vowels from the trolls' comments, 
#neutralizing the threat.

#Task: Write a function that takes a string and return a new string with all
#vowels removed.

#Input: "This website is for losers LOL!"
#Output: "Ths wbst s fr lsrs LL!"

#Prompt user to input a string
string = input("Enter comment: ")

#Import built-in package to work with Regular Expressions
import re

#Create a function that returns a new string with vowels removed
def disemvowel(string):
    return re.sub("a|e|i|o|u|A|E|I|O|U", "", string)

#Call the function
disemvowel(string)

#Added test cases
#test.assert_equals(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")
#test.assert_equals(disemvowel("You suck!"), "Y sck!")
#test.assert_equals(disemvowel("This is terrible."), "Ths s trrbl.")
#test.assert_equals(disemvowel("Don't quit your day job."), "Dn't qt yr dy jb.")
#test.assert_equals(disemvowel("Boo!"), "B!")
