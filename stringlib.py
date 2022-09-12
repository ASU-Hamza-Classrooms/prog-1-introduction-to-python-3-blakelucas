#!/bin/python3

#Add the following functions:
#
#reverseStr - takes as input a string and returns the reverse of it
def reverseStr(word):
    return word[::-1]

#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
def containsWord(containingStr, containedStr):
    if containedStr.lower() in containingStr.lower():
        return "Yes"
    else:
        return "No"

#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise  
def isPalindrome(word):
    rev = reverseStr(word).lower()
    if rev == word:
        return "Yes"
    else:
        return "No"

#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
def upperCaseStr(word):
    return word.upper()

