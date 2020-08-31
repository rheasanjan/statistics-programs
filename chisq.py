''' Author: Rhea Sanjan
Created date: 17th May 2018

Chi square test for independence 
- Compares two categorical values from the same population 
- Need a contingency table(two way cross tab) for this test 
- A very small chi square value means the variables are related 
- In this program, one-way and two-way cross tabs are created '''


import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
import scipy.stats as scs

df = pd.read_excel("rename.xlsx",sheet_name="Sheet1")

# # Find the critical value for 95% confidence*
# crit = scs.chi2.ppf(q=0.95,df =1)
# print "Critical value",crit

#CROSS TABS -> ONE WAY TABLES
freq1 = pd.crosstab(index=df['SEX'],columns='count')
#print freq1
freq2 = pd.crosstab(index=df['STONE'],columns='count')
#print freq2[0:2]
#two way TABLES
two_way = pd.crosstab(index=df['STONE'],columns=df['SEX'])
print two_way
#this function takes a two-way table as argument
op = scs.chi2_contingency(two_way)
print "chi-square statistic-> X^2",op[0]
print "p value",op[1]
print "degree of freedom",op[2]
print "expected frequencies",op[3]
