# l. print first 7 records fiom employees file
# 2. print all employee names in alphabetical order
# 3. find the name of the employee with highest salary
# 4. list the names of male employees
# 5. to which all teams employees belong
import pandas as pd

df = pd.read_csv("employee.csv")

print(df.head(7))

print(df['name'].sort_values(ascending=False))

# print(df['salary'].max())

indx = df['salary'].idxmax()
highest_salary_emp  = df.loc[indx,'name']
print(highest_salary_emp)

# max_salary = df['salary'].max()
# print(df[df['salary']==max_salary]['name'])

print(df[df['gender'] == 'male']['name'])

print(df['team'].unique())