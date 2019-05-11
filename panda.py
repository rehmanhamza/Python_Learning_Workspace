import numpy as np
import pandas as pd
#data = np.array([['','Col1','Col2'],['Row1',1,2],['Row3',3,4]])
#print (pd.DataFrame(data=data[1:,1:],index=data[1:,0],columns=data[0,1:]))

stats = pd.read_csv('C:\\Users\\Humxa\\Desktop\\Atom\\Python\\DemographicData.csv')
#print stats
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']
# print stats[21:26]  # will print rows from 21 till 25, this format is only for printing rows
#print stats.head()
#print stats.tail()
#print stats.info()
#print stats.describe()
#print stats.describe().transpose()

# Task

# [start at the very end ':' go the beginning ':', -1 represents in the reverse order ]
#print stats[::-1]

print stats[0::20]
