# %% [markdown]
# Exploratory Analysis on Sales Data.. by AL

# %%
# import data analysis packages for visualization
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
# import file and create data frame
df = pd.read_csv(
    "C:\\Users\\Zen\\Documents\\PracticeData\\FilteredSalesData.csv")

# %% [markdown]
#  What are the data types  and how many records are there?

# %%
# Shown info for data types of columns
df.info()

# %% [markdown]
# What entries are missing from the region column?

# %%
# limited data output
df.loc[df['Region'].isna()].head(5)

# %%
# Convert date and time columns for analysis, re run info cell to verify checks
df['Date_Shipd'] = pd.to_datetime(df['Date_Shipd'])
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Time_Shipd'] = pd.to_timedelta(df['Time_Shipd'])

# %% [markdown]
# What does the data frame look like?

# %%
# show top 5 rows of data frame to see what data looks like
df.head()

# %% [markdown]
# Who is the Best Salesperson?

# %%
# Create list of salesperon and how many items they sold and total value
df[['SalesPerson', 'Qty_Sold', 'Actual Price']].groupby(
    by=['SalesPerson'], sort=True).sum('count').sort_values(by='Qty_Sold')

# %% [markdown]
# What country are the sales people from?

# %%
# temporaraly set index to get grouping of sales names
df[['Country', 'SalesPerson']].set_index('Country').groupby(
    by=['Country', 'SalesPerson']).count()

# %% [markdown]
# What item sold the most units?

# %%
# List of item qty that sold
df[['Item', 'Qty_Sold']].groupby(
    by=['Item'], sort=True).sum().sort_values(by='Qty_Sold')

# %% [markdown]
# What item brought in the higest gross profits?

# %%
# List of item qty that sold
df[['Item', 'Actual Price']].groupby(by=['Item'], sort=True).sum(
).sort_values(by='Actual Price', ascending=False)

# %% [markdown]
# What country are we shipping the most units to?

# %%
df[['Country', 'Qty_Sold']].groupby(by='Country').sum(
).sort_values(by='Qty_Sold', ascending=False).head(n=5)

# %%
df[['Country', 'Qty_Sold']].groupby(by='Country').sum().sort_values(
    by='Qty_Sold', ascending=False).head(n=5).plot(kind='bar', figsize=(4, 1))

# %% [markdown]
# What country is placing the most orders?

# %%
df[['Country', 'OrderId']].groupby(by=['Country']).count(
).sort_values(by='OrderId', ascending=False,).head(n=5)

# %%
df[['Country', 'OrderId']].groupby(by=['Country']).count().sort_values(
    by='OrderId', ascending=False,).head(n=5).plot(kind='barh', figsize=(4, 2))

# %% [markdown]
# What was the amount of discounts given year over year?

# %%
# Adding a total discount column to df and seeing yearly values
df['total_discount'] = df['Actual Price'] - df['Discount Price']
df[['Order_Date', 'Qty_Sold', 'Actual Price', 'Discount Price',
    'total_discount']].resample(on='Order_Date', rule='YE').sum()

# %% [markdown]
# What are the country discount totals over the years?

# %%
df[['Country', 'Order_Date', 'total_discount']].set_index(['Country']).groupby(
    by='Country').resample(on='Order_Date', rule='YE').sum()

# %% [markdown]
# What are the stats on the total discounts given?

# %%
# df discount stats
df['total_discount'].describe()

# %% [markdown]
# What orders were above the mean discount price and who gave the most discounts?

# %%
df.loc[(df['total_discount'] > 43)].groupby(by='SalesPerson').sum(
    numeric_only=True).sort_values(by='total_discount', ascending=False)

# %%


# %%


# %%


# %%


# %%
