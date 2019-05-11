input=raw_input # assign input word to raw_input function in order to take input from user, it will save time by not typing 'raw_input' everytime
from math import pi
radius = input("Enter Radius: ")
radius=int(radius)
print "Area of Circle", 2*pi*(radius*radius)

a=[1,0,3,4,5]
a.append(6)
print a
a.sort()
print a
a.reverse()
print a


name=input("Enter Name: ")
print "Hi ", name.upper()
age=input("Enter Age: ")
age=int(age)  # type casting is neccesary in Python as all variables are taken as strings by default
if(age==20):
    print "We have the same age : ", age
else:
    print "I am 20 Years old."
print type(age)

my_name = "Hamza Rehman"
my_age = 20
my_weight = 80
my_eyes = "Green"
my_hair = "Blackish Brown"

print "My name is %s." % (my_name)
print "I am %d years old." % (my_age)
print "I weigh %d kg." % (my_weight)
print "I have %s eyes and %s hair." % (my_eyes, my_hair)

print "If I add %d and %d I get %d." % (my_age, my_weight, my_age+my_weight) 

user_name=input("Enter Name: ")
user_age=input("Enter age: ")
user_age=int(user_age)

print "Your name is %s" % (user_name)
print "Your are %d years old" % (user_age)
print name +" "+user_name

x = "There are %d days in month of December." % 31
print x

print "I said: %r" % (x)
print "And I repeat %r" % (x)

days = "\nMonday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\nSunday"
months = "\nJan\nFeb\nMar\nApr\nMay\nJune\nJuly\nAug\nSep\nOct\nNov\nDec"

print days
print months

if(type(days)==type(months)==type(user_name)==type(my_name)):
    print "They have same type as 'str'"
else:
    print "Error 404"
