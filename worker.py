#!/bin/python3

from stringlib import *

#Add a Worker class to this file.
class Worker:
    def __init__(self, inputStr):
        self.inputStr = inputStr

#The Worker class constructor needs to take as input
#a string.  It will set its own data member to that string.

#Add methods to the Worker class that are equivalent to
#functions in the stringlib module.  These methods will
#not take a string as input (except for the containsWord
#method, which will take the contained string parameter).  Instead,
#these methods will operate on the Worker class data member. 
#Your method can call the needed function in the stringlib
#module.
    def reverseStr(self):
        return reverseStr(self.inputStr)
 
    def containsWord(self, containedStr):
        return containsWord(self.inputStr, containedStr)

    def isPalindrome(self):
        return isPalindrome(self.inputStr)

    def upperCaseStr(self):
        return upperCaseStr(self.inputStr)

