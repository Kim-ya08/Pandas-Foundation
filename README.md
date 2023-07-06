# Course-Pandas-Foundation
Course Pandas Foundation - Final Project (Template)

Date: 05 July 2023

Author: Kanokwan H

Course: Pandas Foundation

# import library
	import matplotlib.pyplot as plt
	import numpy as np
	import pandas as pd
# import data
	df = pd.read_csv("sample-store.csv")

# see data frame information using .info()
	df.info()
	<class 'pandas.core.frame.DataFrame'>
	RangeIndex: 9994 entries, 0 to 9993
	Data columns (total 21 columns):
	 #   Column          Non-Null Count  Dtype
	---  ------          --------------  -----
	 0   Row ID          9994 non-null   int64
	 1   Order ID        9994 non-null   object
	 2   Order Date      9994 non-null   object
	 3   Ship Date       9994 non-null   object
	 4   Ship Mode       9994 non-null   object
	 5   Customer ID     9994 non-null   object
	 6   Customer Name   9994 non-null   object
	 7   Segment         9994 non-null   object
	 8   Country/Region  9994 non-null   object
	 9   City            9994 non-null   object
	 10  State           9994 non-null   object
	 11  Postal Code     9983 non-null   float64
	 12  Region          9994 non-null   object
	 13  Product ID      9994 non-null   object
	 14  Category        9994 non-null   object
	 15  Sub-Category    9994 non-null   object
	 16  Product Name    9994 non-null   object
	 17  Sales           9994 non-null   float64
	 18  Quantity        9994 non-null   int64
	 19  Discount        9994 non-null   float64
	 20  Profit          9994 non-null   float64
	dtypes: float64(4), int64(2), object(15)
	memory usage: 1.6+ MB

# TODO - convert order date and ship date to datetime in the original dataframe
	df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
	df['Ship Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')

	<class 'pandas.core.frame.DataFrame'>
	RangeIndex: 9994 entries, 0 to 9993
	Data columns (total 21 columns):
	 #   Column          Non-Null Count  Dtype
	---  ------          --------------  -----
	 0   Row ID          9994 non-null   int64
	 1   Order ID        9994 non-null   object
	 2   Order Date      9994 non-null   datetime64[ns]
	 3   Ship Date       9994 non-null   datetime64[ns]
	 4   Ship Mode       9994 non-null   object
	 5   Customer ID     9994 non-null   object
	 6   Customer Name   9994 non-null   object
	 7   Segment         9994 non-null   object
	 8   Country/Region  9994 non-null   object
	 9   City            9994 non-null   object
	 10  State           9994 non-null   object
	 11  Postal Code     9983 non-null   float64
	 12  Region          9994 non-null   object
	 13  Product ID      9994 non-null   object
	 14  Category        9994 non-null   object
	 15  Sub-Category    9994 non-null   object
	 16  Product Name    9994 non-null   object
	 17  Sales           9994 non-null   float64
	 18  Quantity        9994 non-null   int64
	 19  Discount        9994 non-null   float64
	 20  Profit          9994 non-null   float64
	dtypes: datetime64[ns](2), float64(4), int64(2), object(13)
	memory usage: 1.6+ MB
# TODO - count nan in postal code column
	df['Postal Code'].isna().sum()
# TODO - filter rows with missing values
	df[df['Postal Code'].isna()]
# TODO - Explore this dataset
	# filter top 10 products from high total profit
	df.groupby('Product Name')['Profit'].sum().sort_values(ascending = False ).head(10).round(2)

	Product Name
	Canon imageCLASS 2200 Advanced Copier                                          25199.93
	Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind     7753.04
	Hewlett Packard LaserJet 3310 Copier                                            6983.88
	Canon PC1060 Personal Laser Copier                                              4570.93
	HP Designjet T520 Inkjet Large Format Printer - 24" Color                       4094.98
	Ativa V4110MDD Micro-Cut Shredder                                               3772.95
	3D Systems Cube Printer, 2nd Generation, Magenta                                3717.97
	Plantronics Savi W720 Multi-Device Wireless Headset System                      3696.28
	Ibico EPK-21 Electric Binding System                                            3345.28
	Zebra ZM400 Thermal Label Printer                                               3343.54
	Name: Profit, dtype: float64

# Data Analysis Part
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
	std_sales = sales_2017['Sales'].std()
	
	print(f'Total = {total_sales}\nAverage = {avg_sales}\nStandard deviation = {std_sales:.2f}')
	
	Total = 484247.5
	Average = 242.97
	Standard deviation = 754.05
# TODO 06 - which Segment has the highest profit in 2018
	sales_2018 = df[(df['Order Date'].dt.year == 2018)]
	sales_2018 = sales_2018.groupby('Segment')['Profit'].sum().sort_values(ascending = False).head(1)
	print(sales_2018)
 
			Profit
	Consumer 	28460.1665
# TODO 07 - which top 5 States have the least total sales between 15 April 2019 - 31 December 2019
	top5_least = df[((df['Order Date'] > '2019-4-15') & (df['Order Date'] < '2019-12-31'))]
	top5_least = top5_least.groupby('State')['Sales'].sum().sort_values().head()
	print(top5_least)
					Sales
	New Hampshire			49.05
	New Mexico			64.08
	District of Columbia		117.07
	Louisiana			249.8
	South Carolina			502.48
# TODO 08 - what is the proportion of total sales (%) in West + Central in 2019 e.g. 25% 
	sales_2019 = df[(df['Order Date'].dt.year == 2019)]
	region_2019 = sales_2019.groupby('Region')['Sales'].sum().reset_index()
	print(region_2019)
 
 	Region	Sales
	0	Central	147429.3760
	1	East	180685.8220
	2	South	93610.2235
	3	West	187480.1765
	
	sum_all = region_2019['Sales'].sum()
	print('Total sales in 2019 =', sum_all)
	
	regions = ['West', 'Central']
	west_cen = region_2019[region_2019['Region'].isin(regions)]
	#west_cen = region_2019[(region_2019['Region'] == 'West') | (region_2019['Region'] == 'Central')]
	sum_w_c = west_cen['Sales'].sum()
	print(f'Proportion of total sales (%) in West + Central in 2019 = {sum_w_c/sum_all*100:.2f}%')
 	
	Total sales in 2019 = 609205.598
	Proportion of total sales (%) in West + Central in 2019 = 54.97%
 


# TODO 09 - find top 10 popular products in terms of number of orders vs. total sales during 2019-2020
	sales_19_20 = df[(df['Order Date'].dt.year >= 2019) & (df['Order Date'].dt.year <= 2020)]
	
	no_of_orders = sales_19_20.groupby('Product Name')['Sales'].agg(['count','sum'])\
	                .reset_index().sort_values('count',ascending = False).head(10)
	no_of_orders = no_of_orders.reset_index()
	top10 = no_of_orders[['Product Name','count','sum']]
	top10.columns= ['Product Name', 'number of orders', 'total sales']
	print("top 10 popular products in terms of number of orders vs. total sales during 2019-2020")
	print(top10)
	
	top 10 popular products in terms of number of orders vs. total sales during 2019-2020
	                                      Product Name  number of orders  total sales
	0                                Easy-staple paper                27     1481.728
	1                                          Staples                24      462.068
	2                                  Staple envelope                22      644.936
	3                          Staples in misc. colors                13      357.164
	4                                   Staple remover                12      204.512
	5                          Storex Dura Pro Binders                12      176.418
	6               Chromcraft Round Conference Tables                12     7965.053
	7  Global Wood Trimmed Manager's Task Chair, Khaki                11     2793.086
	8                          Avery Non-Stick Binders                11      122.128
	9                       Staple-based wall hangings                10      233.392
# TODO 10 - plot at least 2 plots, any plot you think interesting :)

	# 1st plot : Group by Segment and sum profit
 
	df.groupby('Segment')['Profit'].sum().plot(kind='bar',color = ['salmon', 'orange', 'gold'])
	plt.title('Group by Segment and sum profit')
	plt.ylabel('Total profit')
	plt.xlabel('Segment')
	plt.show()
 
![segment](https://github.com/Kim-ya08/Course-Pandas-Foundation/assets/123286529/68e938fb-6654-4624-963a-111e2551b848)

	# 2nd plot : Group by Segment and sum profit
 
	ship_mode = df[['Order ID','Ship Mode']].drop_duplicates()
	ship_mode = ship_mode['Ship Mode'].value_counts().plot(kind ='bar', color = ['#EDB120', '#7E2F8E', '#D95319', '#A2142F'])
	plt.title('Number of ordes group by ship mode')
	plt.ylabel('Number of orders')
	plt.xlabel('Ship Mode')
	plt.show()
 
![ship_mode](https://github.com/Kim-ya08/Course-Pandas-Foundation/assets/123286529/d442940b-8309-4802-830a-b568b65d6b12)

# TODO Bonus - use np.where() to create new column in dataframe to help you answer your own questions
	# Find the products that have sold only once since 2017.
 
	freq_prod = df['Product Name'].value_counts().sort_values().reset_index()
	freq_prod.columns = ['Product Name', 'freq']
	freq_prod
	# count frequency of each product
 
	# merge freq. with df
	merg = pd.merge(df, freq_prod, on = 'Product Name')
	
	merg['Order Date'] = pd.to_datetime(merg['Order Date'], format='%m/%d/%Y')
	# add new column freq. = 1 and order date in 2017
	merg['no_longer_sale'] = np.where((merg['freq'] == 1) & (merg['Order Date'].dt.year < 2018) ,True, False )
	
	# filter column no_longer_sale = True
	pro_freq_1 = merg.query('no_longer_sale == True ')
	pro_freq_1 = pro_freq_1[['Order Date', 'Product Name','freq']].sort_values('Order Date')
	print(pro_freq_1)
 
	 Order Date                                       Product Name  freq
	7886 2017-03-17                                         Xerox 1918     1
	7885 2017-03-17                                         Xerox 1926     1
	8319 2017-03-18  Cisco TelePresence System EX90 Videoconferenci...     1
	8602 2017-06-21                Epson Perfection V600 Photo Scanner     1
	9180 2017-07-26  Logitech Illuminated Ultrathin Keyboard with B...     1
	129  2017-08-27                            Cisco SPA 501G IP Phone     1
	7137 2017-08-29        Jiffy Padded Mailers with Self-Seal Closure     1
	8356 2017-09-07                                  AT&T EL51110 DECT     1
	9119 2017-09-13                     Eldon File Chest Portable File     1
	3242 2017-09-14  Sanitaire Vibra Groomer IR Commercial Upright ...     1
	9927 2017-09-17                     Plantronics Single Ear Headset     1
	1615 2017-09-19  Xerox WorkCentre 6505DN Laser Multifunction Pr...     1
	9972 2017-10-10  Hewlett-Packard Deskjet F4180 All-in-One Color...     1
	7313 2017-10-18                    Avaya IP Phone 1140E VoIP phone     1
	1929 2017-11-04  Canon imageCLASS MF7460 Monochrome Digital Las...     1
	9377 2017-11-04              Hewlett-Packard Deskjet D4360 Printer     1
	9580 2017-11-18                  PNY Rapid USB Car Charger - Black     1
	8153 2017-11-22  Holmes Harmony HEPA Air Purifier for 17 x 20 Room     1
	9348 2017-11-30   Park Ridge Embossed Executive Business Envelopes     1
	465  2017-12-05  Hunt BOSTON Model 1606 High-Volume Electric Pe...     1
	9989 2017-12-19                    RCA ViSYS 25425RE1 Corded phone     1

Final Project from Data Science Bootcamp 8 (DataRockie)
