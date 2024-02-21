# Import library
import pandas as pd
import numpy as np

#Taking csv file
#Online shopping data
df = pd.read_csv("/MLpract2/onlineshop.csv")
df.head()

# Unique function is used....
df['Number'].is_unique

# Set Number column as Index....
df = df.set_index('Number')
df.head()

#Location function
df.loc[31]

df.loc[30:, 'Location'].head(10)

#Rename of Columns names....
new_column_names = {"Coupon_Status": "Coupon"}
   
data = df.rename(columns=new_column_names)
data.columns

#Display informaion about dataset
df.info()