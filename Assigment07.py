#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   Breana K. Merriweather
# Date:  August 26, 2019
# ChangeLog: 
#-------------------------------------------------#


#1). Create a simple example of how you would use Python Exception Handling.


#Demonstrate handling exceptions

Miles = int(input("Please Enter Total Miles Driven: "))
Gallon = int(input("Please Enter Gallons of Gas Used: "))
MPG = 0
try:
    MPG = int(Miles/Gallon)
except ZeroDivisionError:
    print("Please Try Again.")
print("Your MPG is: ",MPG)


#2). Create a simple example of how you would use Python Pickling.

#import pickle
import pickle

#ask user for personal information
fstName = str(input("Enter your First Name: "))
lstName = str(input("Enter your Last Name: "))
userInfo = [fstName, lstName]
print(userInfo)


#Store data with the pickle.dump 
objFile = open("users.dat", "ab")
pickle.dump(userInfo, objFile)
objFile.close()



