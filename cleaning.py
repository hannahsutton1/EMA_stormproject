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

#combining columns for easier interpretation
df['end_date'] = df.apply(lambda row: f"{row['END_DAY']} {row['END_YEARMONTH']}" , axis=1)

print(df['end_date'])

#revert to original format if needed
df['BEGIN_YEARMONTH'] = df['BEGIN_YEARMONTH'].astype(str).str.replace(' ', '')

#make sure day is two digits
df['BEGIN_DAY'] = df['BEGIN_DAY'].astype(str).str.zfill(2)

#combine into YYYYMMDD format
df['begin_date'] = pd.to_datetime(
    df['BEGIN_YEARMONTH'] + df['BEGIN_DAY'],
    format='%Y%m%d',
    errors='coerce'  # avoids crashing on bad data
)

#format as MM/DD/YYYY for easier inspection
df['begin_date_str'] = df['begin_date'].dt.strftime('%m/%d/%Y')

print(df['begin_date'])

#first, revert to original format if needed
df['END_YEARMONTH'] = df['END_YEARMONTH'].astype(str).str.replace(' ', '')

#make sure day is two digits
df['END_DAY'] = df['END_DAY'].astype(str).str.zfill(2)

#combine into YYYYMMDD format
df['end_date'] = pd.to_datetime(
    df['END_YEARMONTH'] + df['END_DAY'],
    format='%Y%m%d',
    errors='coerce'  # avoids crashing on bad data
)

#reformat as MM/DD/YYYY
df['end_date'] = df['end_date'].dt.strftime('%m/%d/%Y')

#check column for accuracy
print(df['end_date'])

#repeat formatting steps for end_date 
# #first, revert to original format if needed
df['END_YEARMONTH'] = df['END_YEARMONTH'].astype(str).str.replace(' ', '')

#make sure day is two digits
df['END_DAY'] = df['END_DAY'].astype(str).str.zfill(2)

#combine into YYYYMMDD format
df['end_date'] = pd.to_datetime(
    df['END_YEARMONTH'] + df['END_DAY'],
    format='%Y%m%d',
    errors='coerce'  # avoids crashing on bad data
)

#reformat as MM/DD/YYYY
df['end_date'] = df['end_date'].dt.strftime('%m/%d/%Y')

#check column for accuracy
print(df['end_date'])

#reformat as begin_date and time
#add time into beginning date column 
#ensure BEGIN_TIME is a string and zero-padded to 4 digits
df['BEGIN_TIME'] = df['BEGIN_TIME'].astype(str).str.zfill(4)

#convert BEGIN_TIME to a timedelta object
df['begin_time_delta'] = pd.to_timedelta(
    df['BEGIN_TIME'].str[:2] + ':' + df['BEGIN_TIME'].str[2:] + ':00'
)

#ensure begin_date is a datetime object
df['begin_date'] = pd.to_datetime(df['begin_date'], errors='coerce')

#add the timedelta to the datetime
df['begin_date_time'] = df['begin_date'] + df['begin_time_delta']

#reformat as MM/DD/YYYY HH:MM:00
df['begin_date_time'] = df['begin_date_time'].dt.strftime('%m/%d/%Y %H:%M')
#check column
print(df['begin_date_time'])

#repeat for end_date
#ensure END_TIME is a string and zero-padded to 4 digits
df['END_TIME'] = df['END_TIME'].astype(str).str.zfill(4)

#convert BEGIN_TIME to a timedelta object
df['end_time_delta'] = pd.to_timedelta(
    df['END_TIME'].str[:2] + ':' + df['END_TIME'].str[2:] + ':00'
)

#ensure begin_date is a datetime object
df['end_date'] = pd.to_datetime(df['end_date'], errors='coerce')

#add the timedelta to the datetime
df['end_date_time'] = df['end_date'] + df['end_time_delta']

#reformat as MM/DD/YYYY HH:MM:00
df['end_date_time'] = df['end_date_time'].dt.strftime('%m/%d/%Y %H:%M')
#check column
print(df['end_date_time'])

#with begininng and end date and date/time columns added, we can remove begin_yearmonth, begin_date, begin_time columns

#remove begin_yearmonth, begin_date, begin_time columns
df = df.drop(['BEGIN_YEARMONTH' , 
              'END_YEARMONTH' , 
              'BEGIN_DAY',
              'END_DAY',
              'BEGIN_TIME' , 
              'END_TIME'],
              axis=1)

df.info()



