
# coding: utf-8

# # Q2_Part2

# In[2]:

import pandas as pd


# # import data from employee compensation csv file

# In[3]:

df = pd.read_csv('Data/employee_compensation.csv')
df.shape
df.head()


# # Create empty DataFrames

# In[62]:

from pandas import Series, DataFrame
dfCalendar = DataFrame()
dfRequired = DataFrame()
dfResult = DataFrame()


# In[63]:

dfCalendar=df[(df['Year Type']=='Calendar')]
dfCalendar=pd.DataFrame(dfCalendar.groupby(['Employee Identifier','Job Family']).mean())
dfCalendar.head()


# # Filter Overtime rows with value greater than 5% of salaries

# In[73]:

dfRequired=dfCalendar[(dfCalendar['Overtime']>(.05*dfCalendar['Salaries']))]
dfRequired.head()


# # group by and calculate average

# In[75]:

res = dfRequired.groupby([dfRequired.index.get_level_values(1)]).mean()
res = res[['Total Benefits','Total Compensation']]
res['Percent_Total_Benefit']= res['Total Benefits']*100 / res['Total Compensation']
res.head()


# In[ ]:




# In[76]:

dfResult = res.sort_values('Percent_Total_Benefit', ascending=False)
dfResult.head()


# # Save data to csv file

# In[ ]:

dfResult.to_csv('Q2_Part2.csv',index = True, sep=',')

