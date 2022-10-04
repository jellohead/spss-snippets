# pandas pivot_table syntax:

# pandas.pivot_table (
#     data,
#     values=None,
#     index=None,
#     columns=None,
#     aggfunc=’mean’,
#     fill_value=None,
#     margins=False,
#     dropna=True,
#     margins_name=’All’,
#     observed=False
#     )


# create a data set to work with
import pandas as pd
import numpy as np

df = pd.DataFrame({'First Name': ['Aryan', 'Rohan', 'Riya', 'Yash', 'Siddhant', ],
                   'Last Name': ['Singh', 'Agarwal', 'Shah', 'Bhatia', 'Khanna'],
                   'Type': ['Full-time Employee', 'Intern', 'Full-time Employee',
                            'Part-time Employee', 'Full-time Employee'],
                   'Department': ['Administration', 'Technical', 'Administration',
                                  'Technical', 'Management'],
                   'YoE': [2, 3, 5, 7, 6],
                   'Salary': [20000, 5000, 10000, 10000, 20000]})

df


# pivot table that calculates averages
output = pd.pivot_table(data=df,
                        index=['Type'],
                        columns=['Department'],
                        values='Salary',
                        aggfunc='mean')
output

# pivot table with multiple aggregation functions
output = pd.pivot_table(data=df,
                        index=['Type'],
                        values='Salary',
                        aggfunc=['sum', 'mean', 'count'])
output

# Calculate row and column totals (margins)
output = pd.pivot_table(data=df, index=['Type'],
                        values='Salary',
                        aggfunc=['sum', 'mean', 'count'],
                        margins=True,
                        margins_name='Grand Total')
output

# found this tidbit at https://www.codecademy.com/learn/stats-summary-statistics-for-categorical-data/modules/stats-summary-statistics-for-categorical-data/cheatsheet
# looks promising

cagetories = ["strongly disagree", "disagree",
              "neutral", "agree" and "strongly agree"]
df.response = pd.Categorical(df.response, categories, ordered=True)
median_value = np.median(df["response"].cat.codes)
median_text = categories[int(median_value)]

# calculate counts of values for a column in a dataframe:
df['column_name'].value_counts()

# normalize to avoid misleading proportions
df.value_counts(normalize=True)

outcome = np.array([True, False, True, True, False, False, False, False, True])

# proportion of true values:
print(np.mean(outcome))  # output: 0.44444

# number of true values:
print(np.sum(outcome))  # output: 4


# end of example code from this site
