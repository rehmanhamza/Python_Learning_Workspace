import matplotlib.pyplot as plt
import numpy as np
money=np.array([62095,80000,80000,130000,80000,75000])
print 'Median = ',np.median(money)
print 'Average = ', np.average(money)
if np.median(money) > np.average(money):
	print 'Median is Greater'
else:
	print 'Average is Greater'
money1=[62095,80000,80000,130000,80000,75000]
month=['September, 17', 'October, 17', 'December, 17', 'February, 18', 'March, 18', 'May, 18']
plt.scatter(money1, month)
plt.xlabel("Money")
plt.ylabel("Month")
plt.title("RIA Transaction Report")
plt.show()