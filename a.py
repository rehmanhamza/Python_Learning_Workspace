# Electronics Lab
import matplotlib.pyplot as plt
v=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]
i=[0.01,0.02,0.03,0.04,0.59,5.9,12.8,13.01]
plt.plot(v,i)
plt.xlabel("V")
plt.ylabel("I (mA)")
plt.title("Grpah for Forward Bias Current")
plt.show()
plt.clf()

vr=[1.75,4.8,5,10,15,20,25,27]
ir=[5.14,6,6.4,7,8,8.3,9.4,9.8]
plt.plot(vr,ir)
plt.xlabel("V")
plt.ylabel("I (nA)")
plt.title("Graph for Reverse Bias Current")
plt.show()