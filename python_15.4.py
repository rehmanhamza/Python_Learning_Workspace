x="First Line"
y="Second Line"
print(x)
print(y)
a=[4,3,2,0,1]
a.append(5)
print(a)
a.sort()
print(a)
a.reverse()
print(a)

cars=100
spcae_in_a_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*spcae_in_a_car
average_passengers_per_car=passengers/cars_driven

print "There ara",cars,"cars available"
print "There are only",drivers,"drivers available"
print "There will be",cars_not_driven,"empty cars today"
print "We can transport",carpool_capacity,"people today"
print "We have",passengers,"to carpool today"
print "We need to put about",average_passengers_per_car,"in each car."

input_ftn=raw_input
myName=input_ftn("Please enter your name: ")
myAge=input_ftn("Please enter your age: ")
print "Hello World, my name is",myName,"and I am",myAge,"years old"

import sys
print(sys.version)

from math import pi
var=int(input("Enter radius: "))
area=pi*var**2
print 'The area of cirle is = ', area