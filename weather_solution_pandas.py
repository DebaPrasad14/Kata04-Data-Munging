
# coding: utf-8

# In[69]:


import pandas as pd
from collections import OrderedDict

file = 'C:/Users/devD/Desktop/smartcode/ShanMukha/weather.dat'  # file location

#below mydict contains values with headers in dict form
with open(file) as f:
    headers = f.readline().split()
    mydict = [OrderedDict(zip(headers,d.split())) for d in f.readlines()]

df = pd.DataFrame(mydict[1:])   # creating a dataframe
cols = ['MxT', 'MnT'] 
for col in cols:
    df[col] = df[col].map(lambda x: str(x).lstrip('*').rstrip('*')).astype(float) # removing extra characters from value

df['spread'] = df['MxT'] - df['MnT']    # finding diff between MxT & MnT = spread
# mydict[1:]
minv = df['spread'].min()    # getting minimum value in that spread column
df


# In[73]:


df[['Dy']][df['spread']==minv]   # finding the day where spreaf = minv

