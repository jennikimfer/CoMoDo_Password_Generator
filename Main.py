from random import randint, choice
from enum import Enum
import string

def findPassLength():
    #print("reached findPassLength")
    length = randint(10, 25)
    #print(length)
    return length

def checkValid(password):
    file = open("passwords", "r")
    contents = file.read()
    if (password in contents):
        return False
    return True

def addContent(passList, len, types):
    #print("reached addContent")
    while (True):
        num = randint(0, len-1)
        if (passList[num] == None):
            if (types == 0):
                passList[num] = choice(string.ascii_lowercase)
            elif (types == 1):
                passList[num] = choice(string.ascii_uppercase)
            elif (types == 2):
                passList[num] = choice(string.digits)
            elif (types == 3):
                passList[num] = choice(string.punctuation)
            return passList

def findNumContent(len):
    lower = randint(2, len-6)
    len = len-lower
    #print("lower: " + str(lower))
    upper = randint(2, len-4)
    len = len-upper
    #print("upper: " + str(upper))
    num = randint(2, len-2)
    len = len-num
    #print("num: " + str(num))
    char = len
    #print("char: " + str(char))
    return [lower, upper, num, char]

# 2 uppercase, lowercase, special char, number
def generatePass():
    while True:
        len = findPassLength()
        #print(len)
        passList = [None] * len
        numContent = findNumContent(len)
        for i in range(4):
            for j in range(numContent[i]):
                addContent(passList, len, i)
        password = passList[0]
        #print("password: " + password)
        for i in range(len-1):
            password = password + passList[i+1]
        #print("password: " + password)
        if (checkValid(password)):
            return password
    

print("")
print("Welcome to password generator!")
#TODO excludeTemp = input("Type any unusable special characters")
password = generatePass()
file = open("passwords", "a")
file.write(password + "\n")
print("Here is your password: " + password)
print("")