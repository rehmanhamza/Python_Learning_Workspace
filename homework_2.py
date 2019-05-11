import numpy as np
revenue = np.array([14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50])
expenses = np.array([12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96])

profit=revenue-expenses
print type(profit)#=np.array(profit)

print "Profit =\n", profit
print "\n"

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
profit_margin_round=[]
for i in profit_margin:
	profit_margin_round.append(round(i*100, 2))

profit_margin_round=np.array(profit_margin_round)
print type(profit_margin_round)
print "Profit Margin =", profit_margin_round

mean_profit=np.mean(profit_after_tax)
print "\nMean Profit after Tax =", mean_profit

good_months=[]
bad_months=[]
best_month=[]
worst_month=[]

#returning months that have -ve profits
#for i,j in enumerate(profit):
for i in profit_after_tax:
	good_months.append(i > mean_profit)
	bad_months.append(i < mean_profit)
	best_month.append(i == max(profit_after_tax))
	worst_month.append(i == min(profit_after_tax))

print "Good Months =", good_months
print "Bad Months =", bad_months
print "Best Month =", best_month
print "Worst Month =", worst_month