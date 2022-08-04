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



###################################################
# Tuples Data Type - Cannot be Changed unlike List
###################################################

# Create Tuples using ()
tupleA = (1, 2, 4, 8, 9, 56)
print(tupleA)
emptyTuple = ()      # Empty Tuple
print(emptyTuple)
t1 = (1,)            # Tuple with Single element
print(t1)
print(type(t1))
tupleB = ("JAVA", "Python", 23, 4.5, False, 23, "Python")
print(tupleB)

s = tupleB.index("Python")
t = tupleB.count(23)
print(s)
print(t)

# tupleB[1] = "PHP"         #Can't change Tuple items


####################################
# List and Tuple Practice Exercises
####################################

# Write a Python program, to store values in a List provided by a User

l1 = input("Enter the 1st Input:")
l2 = input("Enter the 2nd Input:")
l3 = input("Enter the 3rd Input:")
l4 = input("Enter the 4th Input:")
l5 = input("Enter the 5th Input:")
l6 = input("Enter the 6th Input:")
l7 = input("Enter the 7th Input:")

listOfValues = [l1, l2, l3, l4, l5, l6, l7]

print(listOfValues)


# Write a Python program, to accept values in a List provided by a User and Sort
# Typecasting to int from string (Which is default Data Type)
s1 = int(input("Enter the 1st Input:"))
s2 = int(input("Enter the 2nd Input:"))
s3 = int(input("Enter the 3rd Input:"))
s4 = int(input("Enter the 4th Input:"))
s5 = int(input("Enter the 5th Input:"))
s6 = int(input("Enter the 6th Input:"))
List = [s1, s2, s3, s4, s5, s6]
List.sort()
print(List)

# Check that a Tuple cannot be changed

tupleCheck = (23, 45.5, "Saeem")
tupleCheck [0] = 75         # Throws an error as expected

# Write a Python Program to sum of all the elements in a List

item1 = int(input("Enter the 1st Input:"))
item2 = int(input("Enter the 2nd Input:"))
item3 = int(input("Enter the 3rd Input:"))
item4 = int(input("Enter the 4th Input:"))
item5 = int(input("Enter the 5th Input:"))
item6 = int(input("Enter the 6th Input:"))

listItem = [item1, item2, item3, item4, item5, item6]

print(sum(listItem))

# Write a Pythin Program, to count the number of zero in the given Tuple

tupleZeroCount = (7, 0, 8, 0, 0, 9)
print(tupleZeroCount.count(0))



######################
# Dictionary & Sets
######################

myDictionary = {
    "fast": "Usain Bolt",
    "genius": "Albert Einstein",
    "fittest": "Mr. Olympia",
    "marks": [1, 2, 5],
    "dictionarywithinadictionary": {'Mr. Olympia': 'Arnold'},
    1: 2

}
print(type(myDictionary))   # Printing the 'Type' Dictionary
print(myDictionary)         # Printing the content of the Dictionary
m = (list(myDictionary))    # Changing the 'type' from 'dict' to 'list' using Typecasting
print(type(m))              # Printing the new 'type' of the Dictionary, which is now 'List'


#####################
# Dictionary Methods
#####################

print(myDictionary.keys())      # Prints the keys of the Dictionary
print(myDictionary.values())    # Prints the values of the Dictionary
print(myDictionary.items())     # Prints the [key, values] (all contents) of the Dictionary

myDictionary.update({"fast": "Saeem Khan"})
myDictionary.update({"genius": "SDK"})

dictionaryUpdate = {
    "slow": "Mr. Slow",
    "medium": "Mr. Medium",
    "Average Marks": [81.8, 92.9, 85, True]
}
myDictionary.update(dictionaryUpdate)       # Updates the Dictionary by adding key-value pairs from "dictionaryUpdate"

print(myDictionary.items())

print(myDictionary.get("medium"))      # Prints value associated with key "medium"

print(myDictionary["medium"])          # Prints value associated with key "medium"

print(myDictionary.get("medium2"))     # Will return None as "medium2" is not present in the Dictionary

print(myDictionary["medium2"])         # Will throw an error as "medium2" is not present in the Dictionary




















