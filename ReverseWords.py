#Create a function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
def reverse_words(text):
    words = text.split(" ") 
    reverseWords = [word[::-1] for word in words]
    newSentence = " ".join(reverseWords)
    return newSentence