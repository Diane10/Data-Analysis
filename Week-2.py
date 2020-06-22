# -*- coding: utf-8 -*-
""" Tuyizere Diane I used the different datasets because The one I have it is quantintative""" 

import pandas
import numpy
import scipy.stats
import seaborn
import matplotlib.pyplot as plt

data = pandas.read_csv('datasets.csv', low_memory=False)

data['TAB12MDX'] = pandas.to_numeric(data['TAB12MDX'], errors='coerce')
data['CHECK321'] = pandas.to_numeric(data['CHECK321'], errors='coerce')
data['S3AQ3B1'] = pandas.to_numeric(data['S3AQ3B1'], errors='coerce')
data['S3AQ3C1'] = pandas.to_numeric(data['S3AQ3C1'], errors='coerce')
data['AGE'] = pandas.to_numeric(data['AGE'], errors='coerce')

sub1=data[(data['AGE']>=20) & (data['AGE']<=30) & (data['CHECK321']==1)]

sub2 = sub1.copy()

sub2['S3AQ3B1']=sub2['S3AQ3B1'].replace(0, numpy.nan)
sub2['S3AQ3C1']=sub2['S3AQ3C1'].replace(0, numpy.nan)

recode1 = {1: 30, 2: 22, 3: 14, 4: 6, 5: 2.5, 6: 1}
sub2['USFREQMO']= sub2['S3AQ3B1'].map(recode1)

ct1=pandas.crosstab(sub2['TAB12MDX'], sub2['USFREQMO'])
print (ct1)

colsum=ct1.sum(axis=0)
colpct=ct1/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs1= scipy.stats.chi2_contingency(ct1)
print (cs1)

sub2["USFREQMO"] = sub2["USFREQMO"].astype('category')
sub2['TAB12MDX'] = pandas.to_numeric(sub2['TAB12MDX'], errors='coerce')

seaborn.factorplot(x="USFREQMO", y="TAB12MDX", data=sub2, kind="bar", ci=None)
plt.xlabel('Days smoked per month')
plt.ylabel('Proportion Nicotine Dependent')

recode2 = {1: 1, 2.5: 2.5}
sub2['COMP1v2']= sub2['USFREQMO'].map(recode2)

ct2=pandas.crosstab(sub2['TAB12MDX'], sub2['COMP1v2'])
print (ct2)

colsum=ct2.sum(axis=0)
colpct=ct2/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs2= scipy.stats.chi2_contingency(ct2)
print (cs2)

recode3 = {1: 1, 6: 6}
sub2['COMP1v6']= sub2['USFREQMO'].map(recode3)

ct3=pandas.crosstab(sub2['TAB12MDX'], sub2['COMP1v6'])
print (ct3)

colsum=ct3.sum(axis=0)
colpct=ct3/colsum
print(colpct)

cs3= scipy.stats.chi2_contingency(ct3)
print (cs3)

recode4 = {1: 1, 14: 14}
sub2['COMP1v14']= sub2['USFREQMO'].map(recode4)

ct4=pandas.crosstab(sub2['TAB12MDX'], sub2['COMP1v14'])
print (ct4)

colsum=ct4.sum(axis=0)
colpct=ct4/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs4= scipy.stats.chi2_contingency(ct4)
print (cs4)

recode5 = {1: 1, 22: 22}
sub2['COMP1v22']= sub2['USFREQMO'].map(recode5)

ct5=pandas.crosstab(sub2['TAB12MDX'], sub2['COMP1v22'])
print (ct5)

colsum=ct5.sum(axis=0)
colpct=ct5/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs5= scipy.stats.chi2_contingency(ct5)
print (cs5)

recode6 = {1: 1, 30: 30}
sub2['COMP1v30']= sub2['USFREQMO'].map(recode6)

ct6=pandas.crosstab(sub2['TAB12MDX'], sub2['COMP1v30'])
print (ct6)

colsum=ct6.sum(axis=0)
colpct=ct6/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs6= scipy.stats.chi2_contingency(ct6)
print (cs6)

recode7 = {2.5: 2.5, 6: 6}
sub2['COMP2v6']= sub2['USFREQMO'].map(recode7)

ct7=pandas.crosstab(sub2['TAB12MDX'], sub2['COMP2v6'])
print (ct7)

colsum=ct7.sum(axis=0)
colpct=ct7/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs7=scipy.stats.chi2_contingency(ct7)
print (cs7)


























