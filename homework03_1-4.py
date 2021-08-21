#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
pd.set_option('display.max_columns', 100)

college = pd.read_csv('pandas_intro/data/college.csv')
college_idx = college.set_index('instnm')


# In[24]:


college.head(2)


# In[25]:


college_idx.head(2)


# ### Exercise 1
# What is the median SAT Math score (satmtmid) for **The University of Texas at Dallas**?

# In[23]:


college_idx.loc['The University of Texas at Dallas']['satmtmid']


# ### Exercise 2
# What state (stabbr) has the 5th highest total undergraduate population (ugds) and what is that population?

# In[48]:


college[['stabbr', 'ugds']].groupby('stabbr').max().sort_values(by = 'ugds', ascending = False).iloc[4]


# ### Exercise 3: Which columns in college dataset contain missing value? What are their missing rate(%)?

# In[26]:


na_cols = college.columns[college.isna().any()].tolist()
na_cols


# In[27]:


miss_rate = [college[na_cols[i]].isna().mean() for i in range(len(na_cols))]
miss_rate


# ### Exercise 4: Is there statistical significant difference between average md_earn_wne_p10 (Median Earnings 10 years after enrollment) for schools in Texas and California?

# In[181]:


# you might find the following function useful to converts data to numeric
# pd.to_numeric()

# example code for p-value calculation if you'd like to calculate z-scores
import scipy.stats as st
# st.norm.cdf(-1.506666)

# you may also find the following function useful
# st.ttest_ind()


# In[247]:


# Extract only colleges from TX/CA and their corresponding md_earn_wne_p10s and drop NaN values
tx_subtbl = college_idx.loc[college_idx['stabbr'] == 'TX', ['md_earn_wne_p10']].dropna()
ca_subtbl = college_idx.loc[college_idx['stabbr'] == 'CA', ['md_earn_wne_p10']].dropna()


# In[249]:


# Convert values in column 'md_earn_wne_p10' into numeric and drop NaN values
tx10 = pd.to_numeric(tx_subtbl['md_earn_wne_p10'], errors = 'coerce').dropna()
ca10 = pd.to_numeric(ca_subtbl['md_earn_wne_p10'], errors = 'coerce').dropna()


# In[251]:


t, p = st.ttest_ind(tx10, ca10, equal_var = False)
print('t = {0: .20f}; p = {1: .20f}'.format(t,p))
print('z-score = {}'.format(st.norm.cdf(t)))

