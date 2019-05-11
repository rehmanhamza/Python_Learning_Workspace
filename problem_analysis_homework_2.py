import numpy as np
revenue = np.array([14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50])
expenses = np.array([12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96])

profit=revenue-expenses
print type(profit)#=np.array(profit)

print "Profit =\n", profit
print "\n"

#returning months that have -ve profits
for i,j in enumerate(profit):
	if j<0:
		print i+1

tax=[]
for i in profit:
	tax.append(round(i*0.3,2))
tax=np.array(tax)
print "Tax =", tax
print "\n"

print "\nProfit after Tax\n"
profit_after_tax=profit-tax
print profit_after_tax

profit_margin=profit_after_tax/revenue
print "Profit Margin =", profit_margin