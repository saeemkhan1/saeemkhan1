##################
# Add two numbers
##################

a = input("Input 1st Number:")
a = int(a)

b = input("Input 2nd Number:")
b = int(b)

print("Sum of the two numbers is =", a+b)

c = a + b
print(type(c))

############################################
# Find remainder when 2 numbers are divided
############################################

d = input("Input 1st Number:")
d = int(d)

e = input("Input 2nd Number:")
e = int(e)
f = d % e
print("The Reminder is", f)

############################################################
#Compare 2 numbers to check if one is bigger than the other
############################################################

x = input("Input 1st Number:")
x = int(x)

y = input("Input 2nd Number:")
y = int(y)
z = x > y

print(z)


#############################
# Find Average of two number
#############################

q = input("Input 1st Number:")
q = int(q)

w = input("Input 2nd Number:")
w = int(w)
avg = ((q+w)/2)

print("The average of the two number is:" , avg)


#############################
#Find the square of a numbers
#############################

s = input("Input Number:")
s = int(s)
square = s*s
print("The square of the number is:", square)


#################
# String Slicing
#################
name = input("Enter your String here:")
print(name[2])
print(name[2:10])
print(name[-1])


#####################################
# Slicing with Skip value in Strings
#####################################

skippingName = input("Enter Name to Slice:")
print(skippingName[0::2])

#######################
# String Functions
######################

story = input("Enter you String here:")
print(len(story))
print(story.endswith("saeem"))   # String ending with some certain character
print(story.count("s"))     # Counts the number of times it appears
print(story.capitalize())   # Capitalizes the first alphabet


#######################
# String Practice
#######################

# Write a program to display a user name followed by "Good Afternoon"

greetingName = input("Enter Name:")
print(greetingName + "! " "Good Afternoon")


# Write a program to Write a letter with a template
'''Dear <Name>
You are selected 
<Date>'''

from datetime import date

today = date.today()

name = input("Enter Name:")

print("Dear ", name, "\n You are selected!" "\n", today)


# Write a Program to detect double space in a string

inputString = input("Input String: ")
detectString = inputString.__contains__("  ")
detectString = inputString.find("  ")

#Replace with Single space
detectString = inputString.replace("  ", " ")
print(detectString)



###########################################################
# Create a List using [], A list can contain any data type
###########################################################

listA = [9, 2, 4, 54, 6]
# Print a list using print() function
print(listA[2])
# Access List using list index, Update a list
listA[0] = "Saeem"
print(listA)

listB = [1.5, True, "SDK", 12, "Python", "Java", 32, 55.655]
print(listB)

# List slicing
print(listB[0:4])


# List Methods
listC = [9, 2, "Saeem", 54, 6]
listC.sort()                # Sorts the List
listC.reverse()             # Reverses the List
listC.append(45)            # Appends at the end of the List
listC.insert(2, "Saeem")    # Inserts "Saeem" at index 2
listC.remove(54)            # Removes 54 from the List
listC.pop(2)                # Removes items from Index 2

print(listC)














