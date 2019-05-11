import matplotlib.pyplot as plt
input_func=raw_input
passk='aaa'
passkey=input_func('Enter Password: ')
if passkey==passk:
	print('Access Granted')
else:
	print('Access Denied')


year=[1950,1970,1990,2010]
pop=[2.516,3.692,5.263,6.972]

plt.plot(year,pop)
if passkey==passk:
	plt.show()
else:
	plt.clf()
	print('You Entered Wrong, sorry no plot to show')