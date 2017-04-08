
# coding: utf-8
# Q1_Part 1
# 

# In[109]:

import pandas as pd


# # import data from vehicle collision csv file

# In[110]:

df = pd.read_csv('/Users/prashantverma/Documents/PythonBackup/Data/vehicle_collisions.csv')
df.shape
df.head()


# # create dataframe for the result

# In[143]:

from pandas import Series, DataFrame
dfResult = DataFrame()


# # Filter the data for the year '2016'

# In[144]:

df2016 = df[df['DATE'].apply(lambda x: x.split('/')[2] == '16')]
df2016.head()
df2016.shape


#  # Filter the data for ManHattan

# In[145]:

df_Manhattan = df2016[df2016.BOROUGH == 'MANHATTAN']
df_Manhattan.head()


# # Filter the data for 'NYC'

# In[146]:

dfResult['NYC'] = df2016['DATE'].apply(lambda x: int(x.split('/')[0]))
dfResult.head()


# # Count data for 'NYC' on month Basis

# In[132]:

dfResult = dfResult.apply(pd.value_counts, sort=False)
dfResult.sort_index()
dfResult


# In[147]:

dfResult['ManHattan'] = df_Manhattan['DATE'].apply(lambda x: int(x.split('/')[0]))
dfResult.head()


# # Count data for 'ManHattan' on month Basis

# In[160]:

Result = dfResult.apply(pd.value_counts, sort=False)
res = DataFrame()
res = Result.sort_index()
res


# # Calculate Percentage between Manhattan & NYC

# In[161]:

res['Percentage'] = (res['ManHattan'] / res['NYC'])*100
res


# # Convert Month format from Digit to Letters

# In[162]:

import datetime
res1 = res.rename(index=lambda x: datetime.datetime.strptime(str(x),'%m').strftime('%d/%b/%Y').split('/')[1])
res1


# # Create Month Column

# In[165]:

res['Month'] = res1.index
res


# # Arrange column sequence

# In[174]:

res = res[['Month', 'NYC', 'ManHattan', 'Percentage']]
res


# # Save data to a csv file

# In[176]:

res.to_csv('Q1_Part1.csv',index=False,sep=',')


# In[ ]:



