
import pandas as pd
pd.set_option('display.max_columns', 100)

college = pd.read_csv('pandas_intro/data/college.csv')
college_idx = college.set_index('instnm')

emp = pd.read_csv('pandas_intro/data/employee.csv')
emp_idx = emp.set_index('title')



# ### Exercise 1
# What is the median SAT Math score (satmtmid) for **The University of Texas at Dallas**?
college_idx.loc['The University of Texas at Dallas']['satmtmid']



# ### Exercise 2
# What state (stabbr) has the 5th highest total undergraduate population (ugds) and what is that population?
college[['stabbr', 'ugds']].groupby('stabbr').max().sort_values(by = 'ugds', ascending = False).iloc[4]



# ### Exercise 3: Which columns in college dataset contain missing value? What are their missing rate(%)?
na_cols = college.columns[college.isna().any()]
miss_rate = college[[col for col in na_cols]].isna().mean()
miss_rate



# ### Exercise 4: Is there statistical significant difference between average md_earn_wne_p10 (Median Earnings 10 years after enrollment) for schools in Texas and California?
import scipy.stats as st

# Extract only colleges from TX/CA and their corresponding md_earn_wne_p10s and drop NaN values
tx_subtbl = college_idx.loc[college_idx['stabbr'] == 'TX', ['md_earn_wne_p10']].dropna()
ca_subtbl = college_idx.loc[college_idx['stabbr'] == 'CA', ['md_earn_wne_p10']].dropna()

# Convert values in column 'md_earn_wne_p10' into numeric and drop NaN values
tx10 = pd.to_numeric(tx_subtbl['md_earn_wne_p10'], errors = 'coerce').dropna()
ca10 = pd.to_numeric(ca_subtbl['md_earn_wne_p10'], errors = 'coerce').dropna()

t, p = st.ttest_ind(tx10, ca10, equal_var = False)
print('t = {0: .20f}; p = {1: .20f}'.format(t,p))
print('z-score = {}'.format(st.norm.cdf(t)))



# ### Exercise 5. Find the mean and standard deviation of math and verbal SAT score for men-only, women-only, and non gender specific universities.
college.groupby(['menonly','womenonly']).agg({'satvrmid': ['mean', 'std']})



# ### Exercise 6. Find the top 3 universities with largest numbers of undergraduate students for each state
college.groupby('stabbr')['ugds'].nlargest(n = 3).to_frame().head(9)



# ### Exercise 7. Generate a DataFrame for the ratios of (number of employees of specific gender and race/total number of employees) for all race-gender combinations.
emp_count = emp.groupby(['gender', 'race']).agg({'title': 'count'})
list = []
for i in emp_count['title'].tolist():
    list.append(i/sum(emp_count['title'].tolist()))
emp_count['rate'] = list
emp_count.drop(columns = 'title').pivot_table(index = 'gender', columns = 'race')



# ### Exercise 8. Use `pd.melt()` to unpivot table `pv3` to the format of `pv4` in exampel above.
pv3 = emp.pivot_table(index='gender', columns='race', 
                      values='salary', aggfunc='mean').round(-3).reset_index()

pv4 = pd.melt(pv3, id_vars = 'gender', value_vars = pv3.columns[1:], value_name = 'mean_salary')


