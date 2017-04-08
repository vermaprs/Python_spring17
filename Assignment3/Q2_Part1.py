
# coding: utf-8

# # Q2_Part1

# In[2]:

import pandas as pd


# # import data from employee compensation csv file

# In[5]:

df = pd.read_csv('Data/employee_compensation.csv')
df.shape
df.head()


# # Create empty DataFrames

# In[6]:

from pandas import Series, DataFrame
dfGroup = DataFrame()
dfRequired = DataFrame()
dfResult = DataFrame()


# # Group By Column 'Organization Group', 'Department' group and find mean

# In[39]:

dfGroup = df.groupby(['Organization Group', 'Department']).mean().reset_index()
dfGroup.head()


# In[68]:

dfRequired = dfGroup[['Organization Group', 'Department','Total Compensation']]
dfRequired.head()


# # sort from max to min based on total compensation

# In[107]:

dfResult = dfRequired.sort_values(['Organization Group','Total Compensation'], ascending=[True,False])
dfResult.head()


# # Save data to csv file

# In[109]:

dfResult.to_csv('Q2_Part1.csv',index = False, sep=',')


# In[ ]:



