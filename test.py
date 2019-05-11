import numpy as np

a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

import matplotlib.pyplot as plt
year=[1950,1970,1990,2010]
pop=[2.516,3.692,5.263,6.972]

plt.plot(year,pop)
plt.show()
plt.clf()

plt.scatter(year,pop)
plt.show()
plt.clf()

semester=["1st", "2nd"]
gpa=[3.56,3.13]
plt.xlabel("Semester")
plt.ylabel("GPA")
plt.title("Grade Curve")
plt.plot(semester,gpa)
plt.show()
plt.clf()

plt.xlabel("Semester")
plt.ylabel("GPA")
plt.title("Grade Curve")
plt.scatter(semester,gpa)
plt.show()
plt.clf()