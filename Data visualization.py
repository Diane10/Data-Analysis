#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


# In[4]:


file = pd.read_csv('gapminder.csv')


# In[5]:


files = file[['country',"incomeperperson", "alcconsumption", "femaleemployrate", "lifeexpectancy", "employrate"]]
data = files.copy()


# In[6]:


data= data.replace(0, np.NaN)
data = data.dropna()


# In[7]:


data


# In[8]:


data.isnull().sum()


# In[9]:


data.dtypes


# In[10]:


data['alcconsumption'] = pd.to_numeric(data['alcconsumption'], errors='coerce')
data['incomeperperson'] = pd.to_numeric(data['incomeperperson'], errors='coerce')
data['femaleemployrate'] = pd.to_numeric(data['femaleemployrate'], errors='coerce')
data['lifeexpectancy'] = pd.to_numeric(data['lifeexpectancy'], errors='coerce')
data['employrate'] = pd.to_numeric(data['employrate'], errors='coerce')


# In[11]:


data.dtypes


# In[12]:


#lifeexpectancy rate
print("first values for life expectancy:")
lifeexpectancyfreq = pd.concat(dict(counts = data["lifeexpectancy"].value_counts(sort=False, dropna=False), percentages = data["lifeexpectancy"].value_counts(sort=False, dropna=False, normalize=True)), axis=1)
print(lifeexpectancyfreq.head(15))

#income per person
print("first values for capita GDP:")
gdp_freq = pd.concat(dict(counts = data["incomeperperson"].value_counts(sort=False, dropna=False), percentages = data["incomeperperson"].value_counts(sort=False, dropna=False, normalize=True)), axis=1)
print(gdp_freq.head(5))


# In[13]:


print("first values for capita GDP:")
gdp_freq = pd.concat(dict(counts = data["incomeperperson"].value_counts(sort=False, dropna=False), percentages = data["incomeperperson"].value_counts(sort=False, dropna=False, normalize=True)), axis=1)
print(gdp_freq.head(5))


# In[14]:


#make new categorical variable to label income per person in 4 categories
#calculate frequency in bins
print('Income per person in categories')
data['incomelabel'] =pd.cut(data.incomeperperson,4,labels=['low','medium','high','very high'])
income_freq = pd.concat(dict(counts = data["incomelabel"].value_counts(sort=False, dropna=False),
                                   percentages = data["incomelabel"].value_counts(sort=False, dropna=False,
                                                                                       normalize=True)),
                            axis=1)
print("Frequency distribution - income per person:\n", income_freq)


#What are the countries with high and very high GDP? Order by income
print('Countries with high and very high GDP')
highincome = data[(data['incomelabel'] == 'high') | (data['incomelabel'] == 'very high') ]
print(highincome.loc[:, ['country', 'incomeperperson', 'incomelabel']].sort_values(by='incomelabel', ascending=False))


# In[15]:


print('Countries by country')
country_counts = data.groupby('country').size()
print(country_counts)
print('\n')

print('GDP Statistics by country')
gdp_mean = data.groupby('country')['incomeperperson'].agg([np.mean, np.median, len])
print(gdp_mean)

print('employment rate by country')
employment_mean = data.groupby('country')['employrate'].agg([np.mean, np.median, len])
print(employment_mean)

print('life expectancy by country')
lifeexpectancy_mean = data.groupby('country')['lifeexpectancy'].agg([np.mean, np.median, len])
print(lifeexpectancy_mean)


# In[16]:


plt.figure(figsize=(14, 7))
sns.distplot(data['incomeperperson'], bins=10, kde=False)
plt.xlabel('Income per person')
plt.title('Capita GDP Per Person')
plt.show()


# In[17]:


plt.figure(figsize=(14, 7))
sns.distplot(data['lifeexpectancy'].dropna())
plt.xlabel('life expectancy per country')
plt.title('Percentage oflife expectancy')
plt.show()


# In[18]:


plt.figure(figsize=(14, 7))
sns.distplot(data['employrate'].dropna())
plt.xlabel('employment rate')
plt.title('employrate')
plt.show()


# In[19]:


fig = plt.figure(figsize=(16,4))
sns.regplot(x="lifeexpectancy", y="incomeperperson", fit_reg=True, data=data);
plt.xlabel('life expectancy');
plt.ylabel('capita GDP');
plt.title('Scatterplot for the association between Internet usage and income level');


# In[20]:


plt.figure(figsize=(14, 7))
sns.countplot(x='incomelabel', data=data)
plt.ylabel('Count')
plt.xlabel('Income per person')


# In[21]:


sns.factorplot(x='country', y='lifeexpectancy', data=data, kind='bar', size=7, aspect=2)
plt.ylabel('life expectancy')
plt.xlabel('country')


# In[27]:


# using ols function for calculating the F-statistic and associated p value
model1 = smf.ols(formula='lifeexpectancy ~ C(incomeperperson)', data=data)
results1 = model1.fit()
print (results1.summary())


# In[29]:



sub2 = data[['lifeexpectancy', 'incomeperperson']].dropna()

print ('means for numcigmo_est by major depression status')
m1= sub2.groupby('lifeexpectancy').mean()
print (m1)

print ('standard deviations for numcigmo_est by major depression status')
sd1 = sub2.groupby('lifeexpectancy').std()
print (sd1)
#i will call it sub3
sub3 = data[['incomeperperson', 'employrate']].dropna()

model2 = smf.ols(formula='employrate ~ C(incomeperperson)', data=sub3).fit()
print (model2.summary())

print ('means for numcigmo_est by major depression status')
m2= sub3.groupby('incomeperperson').mean()
print (m2)

print ('standard deviations for numcigmo_est by major depression status')
sd2 = sub3.groupby('incomeperperson').std()
print (sd2)

mc1 = multi.MultiComparison(sub3['employrate'], sub3['incomeperperson'])
res1 = mc1.tukeyhsd()
print(res1.summary())


# In[ ]:




