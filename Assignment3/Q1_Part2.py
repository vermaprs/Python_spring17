
# coding: utf-8

# # Q1_Part2

# In[109]:

import pandas as pd


# # import data from vehicle collision csv file

# In[125]:

df = pd.read_csv('Data/vehicle_collisions.csv')
df.shape
df.head()


# # Create empty DataFrames

# In[150]:

from pandas import Series, DataFrame
dfGroup = DataFrame()
dfResult = DataFrame()


# # Group By Column 'Borough', to calculate the count

# In[151]:

dfGroup = df.groupby('BOROUGH').count()


# In[152]:

dfGroup


# # Store result in a new DataFrame and assign data

# In[153]:

dfResult['ONE_VEHICLE_INVOLVED'] = dfGroup['VEHICLE 1 TYPE'] - dfGroup['VEHICLE 2 TYPE']

dfResult['TWO_VEHICLES_INVOLVED'] = dfGroup['VEHICLE 2 TYPE'] - dfGroup['VEHICLE 3 TYPE']

dfResult['THREE_VEHICLES_INVOLVED'] = dfGroup['VEHICLE 3 TYPE'] - dfGroup['VEHICLE 4 TYPE']

dfResult['MORE_VEHICLES_INVOLVED'] = dfGroup['VEHICLE 4 TYPE'] +  dfGroup['VEHICLE 5 TYPE']

dfResult.head()


# In[161]:

dfResult['BOROUGH'] = dfGroup.index
dfResult = dfResult[['BOROUGH','ONE_VEHICLE_INVOLVED','TWO_VEHICLES_INVOLVED','THREE_VEHICLES_INVOLVED','MORE_VEHICLES_INVOLVED']]
dfResult


# # Save data to csv file

# In[48]:

dfResult.to_csv('Q1_Part2.csv', index=False, sep=',')


# In[ ]:




# In[ ]:




# In[ ]:



