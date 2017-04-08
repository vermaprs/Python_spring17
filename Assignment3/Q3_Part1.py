
# coding: utf-8

# # Q3_Part1

# In[4]:

import pandas as pd


# # import data from vehicle collision csv file

# In[5]:

df = pd.read_csv('Data/cricket_matches.csv')
df.head()


# In[24]:

from pandas import Series, DataFrame
dfGroup = DataFrame()
dfRequired = DataFrame()
dfResult = DataFrame()


# # Filter condition: Team hosts and win the game

# In[25]:

dfRequired = df[df['home'] == df['winner']]
dfRequired.head()


# # check which innings played, innings 1 or 2

# In[32]:

dfRequired['score'] = np.where(dfRequired['home'] == dfRequired['innings1'], dfRequired['innings1_runs'], dfRequired['innings2_runs'])
dfRequired.head()


# In[35]:

dfRequired = dfRequired['score'].groupby(dfRequired['home']).sum()
dfRequired.head()


# In[ ]:




# In[ ]:



