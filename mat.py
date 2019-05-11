import matplotlib.pyplot as plt
import numpy as np

g=np.array([3.54,3.13])
cr=np.array([16,18])
cgpa=np.array([g[0]*cr[0], g[1]*cr[1]])
cgpa1=cgpa[0]+cgpa[1]
cgpa1/=(cr[0]+cr[1])
cgpa1=float(cgpa1)
print ("CGPA = ", round(cgpa1,2))
g=((g[0]+g[1])/8)*100
print ("CGPA Percentage = ",g)