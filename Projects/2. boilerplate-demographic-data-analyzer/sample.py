import pandas as pd

df = pd.read_csv('adult.data.csv')
df.info()
lower_education = ((df['education']!='Bachelors') &(df['education']!='Masters')&(df['education']!='Doctorate')).sum()
print(lower_education)