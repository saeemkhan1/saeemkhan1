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











