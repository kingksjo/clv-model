z# %%
import pandas as pd

# %% [markdown]
# ##### We import the file from the local directory.

# %%
df = pd.read_csv("C:/Users/User/Desktop/MLAI/clv-model/eda/ecommerce_data.csv")

# %% [markdown]
# ##### Load the first twenty rows of the dataset to get a general idea of the dataset.

# %%
df.head(20)

# %% [markdown]
# ##### Review the Country column and identify missing values

# %%
missing_count = df["Country"].isnull().sum()
print("Missing Country values:", missing_count)

# %% [markdown]
# ##### The percentage of missing countries

# %%
missing_percentage = df["Country"].isnull().mean() * 100 
print("Missing Country values:", missing_count)
print("Percentage missing:", round(missing_percentage, 2), "%")

# %% [markdown]
# ##### Basically, we cannot drop the missing data from about 1,339 countries because doing so would result in a significant loss of data and could affect the accuracy of the results. We will investigate before trying to fill this missing values with 'unknown'

# %% [markdown]
# ##### Rows with missing Country values

# %%
missing_country = df[df["Country"].isnull()]
missing_country.head(10)

# %%
missing_count = df["Country"].isna().sum()
print("Missing Country values:", missing_count)

# %% [markdown]
# ##### Count customers with distinct missing country values

# %%
print("Customers with missing Country:", df.loc[df["Country"].isna(), "CustomerID"].nunique())


# %% [markdown]
# 
# ##### Find customers with missing countries who also have at least one known country elsewhere in the dataset

# %%
known_country_customers = df.loc[
    df["Country"].notna(), "CustomerID"
].unique()
recoverable = df.loc[
    df["Country"].isna()
    & df["CustomerID"].isin(known_country_customers),
    "CustomerID"
].nunique()

print("Customers potentially recoverable:", recoverable)

# %% [markdown]
# ##### This code displays all rows with missing countries, checks other columns for missing countries and checks missing-value counts in these rows

# %%
missing_country = df[df["Country"].isna()]

print(missing_country.head(10).to_string(index=False))
print(missing_country.isna().sum())


# %% [markdown]
# #####  The Country column contains 1,339 missing values affecting 281 distinct customers. The available columns are CustomerID, InvoiceDate, Quantity, UnitPrice, TotalAmount, Country, and ProductCategory. Checking CustomerID did not identify any customers whose countries could be confirmed from other records, and the remaining columns do not provide sufficient information to determine the actual countries. Therefore, I will not make assumptions about the missing values or replace them with the mode. Instead, I will preserve the records and fill the missing Country values with 'Unknown' to indicate that the countries cannot be determined from the available data. If reliable information becomes available from the original data source, the missing values can be updated accordingly.

# %%
df["Country"] = df["Country"].fillna("Unknown")

print("Missing Country values after:", df["Country"].isna().sum())
print("Total rows:", len(df))


# %%
df.head(20)

# %% [markdown]
# ### Conclusion
# 
# ##### The Country column contains 1,339 missing values, representing 16.32% of the 8,205 records and affecting 281 distinct customers. Checking CustomerID did not identify any affected customers whose countries could be recovered from other records. The remaining columns do not reliably establish their actual countries. Therefore, the records will be retained, and missing Country values will be labelled "Unknown" to preserve the dataset without inventing country information.

# %% [markdown]
# 


