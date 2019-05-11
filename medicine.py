#import numpy as np
input_func=raw_input
times_bought_panadol=0
times_bought_despirin=0
headache_data=['Panadol', 'Despirin', times_bought_panadol, times_bought_despirin]
print "Avaliable Medicine for Headache\n", headache_data[:2]
#while (True):
	med=input_func("Enter Your choice for medicine as prescribed by Doctor: ")
	#med=str(med)
	for i in headache_data:
		if i==med:
			print "Medicine Found!"
			if med=='Panadol':
				times_bought_panadol=times_bought_panadol+1
				print "times_bought_panadol = ",times_bought_panadol
				print "You Purchased ",headache_data[0]
			if med=='Despirin':
				times_bought_despirin=times_bought_despirin+1
				print "times_bought_despirin = ", times_bought_despirin
				print "You Purchased ",headache_data[1]
		if med!='Panadol' and med!='Despirin':
			print "Medicine Not Found!"
			break