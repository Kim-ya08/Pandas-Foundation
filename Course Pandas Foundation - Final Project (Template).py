# -*- coding: utf-8 -*-

# -- Project --

# # Final Project - Analyzing Sales Data
# 
# **Date**: 05 July 2023
# 
# **Author**: Kanokwan H
# 
# **Course**: `Pandas Foundation`


# import data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv("sample-store.csv")

# preview top 5 rows
df.head()

# shape of dataframe
df.shape

# see data frame information using .info()
df.info()

# We can use `pd.to_datetime()` function to convert columns 'Order Date' and 'Ship Date' to datetime.


# example of pd.to_datetime() function
pd.to_datetime(df['Order Date'].head(), format='%m/%d/%Y')

# TODO - convert order date and ship date to datetime in the original dataframe
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
df['Ship Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')

df.info()

# TODO - count nan in postal code column
df['Postal Code'].isna().sum()

# TODO - filter rows with missing values
df[df['Postal Code'].isna()]

# TODO - Explore this dataset on your owns, ask your own questions
# filter top 10 products from high total profit
df.groupby('Product Name')['Profit'].sum().sort_values(ascending = False ).head(10).round(2)

# ## Data Analysis Part
# 
# Answer 10 below questions to get credit from this course. Write `pandas` code to find answers.


# TODO 01 - how many columns, rows in this dataset
df.shape
# 21 columns, 9994 rows

# TODO 02 - is there any missing values?, if there is, which colunm? how many nan values?
#df.info()
df.isna().sum()
# Postal Code has 11 nan values.

# TODO 03 - your friend ask for `California` data, filter it and export csv for him
california = df[df['State'] == 'California']
california.to_csv('california.csv')

# TODO 04 - your friend ask for all order data in `California` and `Texas` in 2017 (look at Order Date), send him csv file
cal_tex = df[((df['State'] == 'Texas') | (df['State'] == 'California')) & 
             (df['Order Date'].dt.year == 2017)]
cal_tex.to_csv('cal_tex.csv')

# TODO 05 - how much total sales, average sales, and standard deviation of sales your company make in 2017
sales_2017 = df[(df['Order Date'].dt.year == 2017)]

total_sales = sales_2017['Sales'].sum().round(2)
avg_sales = sales_2017['Sales'].mean().round(2)
std_sales = sales_2017['Sales'].std()#.round(2)

print(f'Total = {total_sales}\nAverage = {avg_sales}\nStandard deviation = {std_sales}')

# TODO 06 - which Segment has the highest profit in 2018
sales_2018 = df[(df['Order Date'].dt.year == 2018)]
sales_2018.groupby('Segment')['Profit'].sum().sort_values(ascending = False).head(1)

# TODO 07 - which top 5 States have the least total sales between 15 April 2019 - 31 December 2019
top5_least = df[((df['Order Date'] > '2019-4-15') & (df['Order Date'] < '2019-12-31'))]
top5_least.groupby('State')['Sales'].sum().sort_values().head()

# TODO 08 - what is the proportion of total sales (%) in West + Central in 2019 e.g. 25% 
sales_2019 = df[(df['Order Date'].dt.year == 2019)]
region_2019 = sales_2019.groupby('Region')['Sales'].sum().reset_index()

#display(region_2019)
sum_all = region_2019['Sales'].sum()
print('Total sales in 2019 =', sum_all)

regions = ['West', 'Central']
west_cen = region_2019[region_2019['Region'].isin(regions)]
#west_cen = region_2019[(region_2019['Region'] == 'West') | (region_2019['Region'] == 'Central')]
sum_w_c = west_cen['Sales'].sum()
print(f'Proportion of total sales (%) in West + Central in 2019 = {sum_w_c/sum_all*100:.2f}%')

# TODO 09 - find top 10 popular products in terms of number of orders vs. total sales during 2019-2020
sales_19_20 = df[(df['Order Date'].dt.year >= 2019) & (df['Order Date'].dt.year <= 2020)]

no_of_orders = sales_19_20.groupby('Product Name')['Sales'].agg(['count','sum'])\
                .reset_index().sort_values('count',ascending = False).head(10)
no_of_orders = no_of_orders.reset_index()

top10 = no_of_orders[['Product Name','count','sum']]
top10.columns= ['Product Name', 'number of orders', 'total sales']
print("top 10 popular products in terms of number of orders vs. total sales during 2019-2020")
#display(top10)

#print("top 10 popular products in terms of total sales during 2019-2020")
#total_sales_19_20 = sales_19_20.groupby('Product Name')['Sales'].sum().sort_values(ascending = False).head(10).reset_index()
#display(total_sales_19_20)

# TODO 10 - plot at least 2 plots, any plot you think interesting :)

# 1st plot : Group by Segment and sum profit
df.groupby('Segment')['Profit'].sum().plot(kind='bar',color = ['salmon', 'orange', 'gold'])

plt.title('Group by Segment and sum profit')
plt.ylabel('Total profit')
plt.xlabel('Segment')
plt.show()
#year = list(df['Order Date'].dt.year.unique())

ship_mode = df[['Order ID','Ship Mode']].drop_duplicates()
ship_mode = ship_mode['Ship Mode'].value_counts().plot(kind ='bar', color = ['#EDB120', '#7E2F8E', '#D95319', '#A2142F'])
plt.title('Number of ordes group by ship mode')
plt.ylabel('Number of orders')
plt.xlabel('Ship Mode')
plt.show()

# TODO Bonus - use np.where() to create new column in dataframe to help you answer your own questions
#find product that sold one time in 2017
freq_prod = df['Product Name'].value_counts().sort_values().reset_index()
freq_prod.columns = ['Product Name', 'freq']
freq_prod
#count frequency of each product

#merge freq. with df
merg = pd.merge(df, freq_prod, on = 'Product Name')

merg['Order Date'] = pd.to_datetime(merg['Order Date'], format='%m/%d/%Y')
#add new column freq. = 1 and order date in 2017
merg['no_longer_sale'] = np.where((merg['freq'] == 1) & (merg['Order Date'].dt.year < 2018) ,True, False )

#filter column no_longer_sale = True
pro_freq_1 = merg.query('no_longer_sale == True ')
pro_freq_1[['Order Date', 'Product Name','freq']].sort_values('Order Date')
print(pro_freq_1)
