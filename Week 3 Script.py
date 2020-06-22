# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 14:59:43 2015

@author: jml
"""

import pandas
import numpy
import seaborn
import scipy
import matplotlib.pyplot as plt

data = pandas.read_csv('gapminder.csv', low_memory=False)

data['internetuserate'] = data['internetuserate'].convert_objects(convert_numeric=True)
data['urbanrate'] = data['urbanrate'].convert_objects(convert_numeric=True)
data['incomeperperson'] = data['incomeperperson'].convert_objects(convert_numeric=True)

data['incomeperperson']=data['incomeperperson'].replace(' ', numpy.nan)

data_clean=data.dropna()

print ('association between urbanrate and internetuserate')
print (scipy.stats.pearsonr(data_clean['urbanrate'], data_clean['internetuserate']))

print ('association between incomeperperson and internetuserate')
print (scipy.stats.pearsonr(data_clean['incomeperperson'], data_clean['internetuserate']))
