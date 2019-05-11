counter=1
while counter<10:
	print counter
	counter=counter+1

for i in range(5):
	print "Hello",i

print range(5)

a=[1,1100,11000]
for j in a:
	if j==1:
		print "In j==1"
		print "Equals ",j
	elif j==1100:
		print "In j==1100"
		print "Equals ",j
	elif j==11000:
		print"In j==11000"
		print "Equals ",j
	else:
		print "Sorry no match for j in a"

import numpy as np
from numpy.random import randn
x=randn()
if x>1:
	print "Greater than 1"
else:
	print "Less than 1"

y=range(1,99,49)
print y

import numpy as np
data=np.arange(0,20)
print data

data=np.reshape(data,(5,4),order='C')
print data
print data[2][2]