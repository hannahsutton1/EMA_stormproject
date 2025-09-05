#import libraries
import pandas as pd
import numpy as np
import matplotlib as plt

#import operating system and print current working directory
import os
print(os.getcwd())

#data at a glance
df = pd.read_csv('stormevent_details.csv')
df.head()
df.info()
df.describe()

#change data type to integer
df['BEGIN_YEARMONTH'] = df['BEGIN_YEARMONTH'].apply(
    lambda x: ' '.join([str(x)[i:i+4] for i in range(0, len(str(x)), 4)])
)

print(df['BEGIN_YEARMONTH'])

df['END_YEARMONTH'] = df['END_YEARMONTH'].apply(
    lambda x: ' '.join([str(x)[i:i+4] for i in range(0, len(str(x)), 4)])
)

print(df['END_YEARMONTH'])

#flip to month/year instead of year/month
df['BEGIN_YEARMONTH'] = df['BEGIN_YEARMONTH'].apply(
    lambda x: f"{str(x)[4:]} {str(x)[:4]}"
)

print(df['BEGIN_YEARMONTH'])

df['END_YEARMONTH'] = df['END_YEARMONTH'].apply(
    lambda x: f"{str(x)[4:]} {str(x)[:4]}"
)

print(df['END_YEARMONTH'])

#combining columns for easier interpretation
df['begin_date'] = df.apply(lambda row: f"{row['BEGIN_DAY']} {row['BEGIN_YEARMONTH']}" , axis=1)

print(df['begin_date'])

#combining columns for easier interpretation
df['end_date'] = df.apply(lambda row: f"{row['END_DAY']} {row['END_YEARMONTH']}" , axis=1)

print(df['end_date'])

