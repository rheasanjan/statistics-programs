''' Auhtor: Rhea Sanjan
Created date: 16th May 2018 

T test on medical data

two sample t test-> used to determine if two population means are equal 
In this program, I have used one sample t test  '''

import pandas as pd
import numpy as np
from scipy import stats
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt

df = pd.read_excel('rename.xlsx',sheet_name='Sheet1')


#print df.head()
# print("Column headings:")
#print(df.columns)
# for i in df.index:
#     print df['POST OPERATIVE COMPLICATIONS'][i]
#descriptives for all columns -> includes count,unique,top,freq,mean,std,min,25%,50%,75%,max-> for all datatypes.
# print df.describe(include='all')
#
# #only for numeric data types
# print df.describe()



# print df.groupby('SEX').mean()
pain_yes = df[df['POST OPERATIVE COMPLICATIONS']=='YES']
no = df[df['POST OPERATIVE COMPLICATIONS']=='NO']
# print male,female
#t test

print stats.ttest_ind(pain_yes['AGE'],no['AGE'])
#output ->Ttest_indResult(statistic=-1.3207011076318629, pvalue=0.19197304714730534)
