# -*- coding: utf-8 -*-
"""EDA_DA-1_21BDS0148

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c_wY5k8yFRgdP96u9xfOc8bGQcTOl6Yk
"""



"""EDA DA-1 21BDS0148 Amogh Vardhan Kona

github link- https://github.com/amogh-vardhan/EDA_DA_21BDS0148

colab link - https://colab.research.google.com/drive/1c_wY5k8yFRgdP96u9xfOc8bGQcTOl6Yk?usp=sharing
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
AmogVardhanKona = pd.read_csv('eda_data_21BDS0148.csv')

roll_number_last4_0148 = 148

# dataFrame 1: Fname - state, statecode, year
AmogVardhanKona1 = {
    'state': ['NY', 'FL', 'MI', 'TX', 'UT'],
    'statecode': [35, 10, 23, 44, 45],
    'year': [1967, 1967, 1967, 1967, 1967]
}
df1_0148 = pd.DataFrame(AmogVardhanKona1)

# dataFrame 2: Lname - consumption, price, eprice
AmogVardhanKona2 = {
    'consumption': [313656, 9430, 302472, 201407, 38935],
    'price': [1.42, 2.26, 0.98, 0.87, 0.68],
    'eprice': [2.98, 2.16, 2.32, 2.19, 2.25]
}
df2_0148 = pd.DataFrame(AmogVardhanKona2)

# Show both DataFrames
print("DataFrame 1 (Fname):")
print(df1_0148)

print("\nDataFrame 2 (Lname):")
print(df2_0148)

# 1. Append (rows): Append df2 to df1 using pd.concat()
df_append_0148 = pd.concat([df1_0148, df2_0148], ignore_index=True)
print("\nDataFrame after Appending df2 to df1 using pd.concat():")
print(df_append_0148)

# 2. Concatenate: Concatenate df1 and df2 by columns (aligning them side by side)
df_concat_0148 = pd.concat([df1_0148, df2_0148], axis=1)
print("\nDataFrame after Concatenating df1 and df2:")
print(df_concat_0148)

# 3. Merge: Merge df1 and df2 on index (since there's no common column)
df_merge_0148 = pd.merge(df1_0148, df2_0148, left_index=True, right_index=True)
print("\nDataFrame after Merging df1 and df2 on index:")
print(df_merge_0148)

# 4. Join: Join df1 and df2 on the index
df_join_0148 = df1_0148.join(df2_0148)
print("\nDataFrame after Joining df1 and df2 on the index:")
print(df_join_0148)

# Display the first few rows of the dataframe
print("Original DataFrame:")
print(AmogVardhanKona.head())

# Insert the first record
first_record_0148 = {
    'rownames': 0,
    'state': 'Amogh Vardhan Kona',
    'statecode': 148,
    'year': 148,
    'consumption': 148,
    'price': 148,
    'eprice': 148,
    'oprice': np.nan,
    'lprice': np.nan,
    'heating': np.nan,
    'income': np.nan
}

# Convert the first record to a DataFrame and concatenate it with the existing DataFrame
first_record_df_0148 = pd.DataFrame([first_record_0148])
AmogVardhanKona = pd.concat([first_record_df_0148, AmogVardhanKona], ignore_index=True)

# Display the updated dataframe
print("\nUpdated DataFrame with First Record:")
print(AmogVardhanKona.head())

# Check if there exists any NA (missing values) in the dataset
any_na_0148 = AmogVardhanKona.isna().any().any()
print(f"\nDoes the dataset contain any missing values? {any_na_0148}")

# Finding the missing summaries of the dataset (summary of missing values per column)
missing_summary_0148 = AmogVardhanKona.isna().sum()
print("\nMissing Values Summary (per column):")
print(missing_summary_0148)

# Find the total number of NA (missing values) in the dataset
total_na_0148 = AmogVardhanKona.isna().sum().sum()
print(f"\nTotal number of missing values in the dataset: {total_na_0148}")

# Count the total number of complete cases in oprice and lprice
complete_cases_0148 = AmogVardhanKona[['oprice', 'lprice']].notna().all(axis=1).sum()
print(f"\nTotal number of complete cases in oprice and lprice: {complete_cases_0148}")

# Proportion of missing and complete data
prop_missing_0148 = AmogVardhanKona.isna().mean()
prop_complete_0148 = 1 - prop_missing_0148
print("\nProportion of Missing Values per Column:")
print(prop_missing_0148)
print("\nProportion of Complete Values per Column:")
print(prop_complete_0148)

# Display the missing values per column for each observation
# Create a missing data heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(AmogVardhanKona.isna(), cbar=False, cmap='viridis')
plt.title("21BDS0148 - Missing Data Heatmap")
plt.show()

# Performing row-wise deletion (drop rows with any missing values)
AmogVardhanKona_cleaned_0148 = AmogVardhanKona.dropna()

# Display the cleaned dataframe
print("\nDataFrame after Row-wise Deletion (NaN Rows Removed):")
print(AmogVardhanKona_cleaned_0148.head())

# Check the number of rows before and after row deletion
print(f"\nNumber of rows before deletion: {len(AmogVardhanKona)}")
print(f"Number of rows after deletion: {len(AmogVardhanKona_cleaned_0148)}")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the Dataset
AmogVardhanKona = pd.read_csv("eda_data_21BDS0148.csv")

# Step 2: Convert all column names to lowercase
AmogVardhanKona.columns = AmogVardhanKona.columns.str.lower()

# Step 3: Replace '?' with NaN for all columns
AmogVardhanKona.replace('?', np.nan, inplace=True)

# Step 4: Display the number of rows and columns in the dataset
print("Dimensions of the dataset:", AmogVardhanKona.shape)

# Step 5: Display the header or attribute names from the dataset
print("Column names:", AmogVardhanKona.columns)

# Step 6: Display the structure of the dataset (info)
print("Structure of the dataset:")
AmogVardhanKona.info()

# Step 7: View the first 3 and last 3 rows of the dataset
print("First 3 rows of the dataset:")
print(AmogVardhanKona.head(3))

print("Last 3 rows of the dataset:")
print(AmogVardhanKona.tail(3))

# Step 9: Displaying Summary Statistics
print("Summary Statistics of the dataset:")
print(AmogVardhanKona.describe())

# Step 10: Data Cleaning

# 10.1 Find out the number of values that are not numeric in 'price', 'consumption', and 'eprice'
non_numeric_price_0148 = AmogVardhanKona['price'].apply(pd.to_numeric, errors='coerce').isna().sum()
non_numeric_consumption_0148 = AmogVardhanKona['consumption'].apply(pd.to_numeric, errors='coerce').isna().sum()
non_numeric_eprice_0148 = AmogVardhanKona['eprice'].apply(pd.to_numeric, errors='coerce').isna().sum()

print(f"Non-numeric values in 'price': {non_numeric_price_0148}")
print(f"Non-numeric values in 'consumption': {non_numeric_consumption_0148}")
print(f"Non-numeric values in 'eprice': {non_numeric_eprice_0148}")

# 10.2 Setting the missing value in 'price' to the mean and converting to numeric
AmogVardhanKona['price'] = pd.to_numeric(AmogVardhanKona['price'], errors='coerce')
mean_price_0148 = AmogVardhanKona['price'].mean()
AmogVardhanKona['price'].fillna(mean_price_0148, inplace=True)

# Step 11: Compute Measures of Central Tendency and Dispersion for 'consumption' Column

# 11.1 Central Tendency: Mean, Median, Mode
mean_consumption_0148 = AmogVardhanKona['consumption'].mean()
median_consumption_0148 = AmogVardhanKona['consumption'].median()
mode_consumption_0148 = AmogVardhanKona['consumption'].mode()[0]

print(f"Mean of consumption: {mean_consumption_0148}")
print(f"Median of consumption: {median_consumption_0148}")
print(f"Mode of consumption: {mode_consumption_0148}")

# 11.2 Dispersion: Standard Deviation and Variance
sd_consumption_0148 = AmogVardhanKona['consumption'].std()
var_consumption_0148 = AmogVardhanKona['consumption'].var()

print(f"Standard Deviation of consumption: {sd_consumption_0148}")
print(f"Variance of consumption: {var_consumption_0148}")

# 11.3 Quartile Ranges and IQR
consumption_quantiles_0148 = AmogVardhanKona['consumption'].quantile([0.25, 0.5, 0.75])
iqr_consumption_0148 = consumption_quantiles_0148[0.75] - consumption_quantiles_0148[0.25]

print(f"Quartiles of consumption:\n{consumption_quantiles_0148}")
print(f"Interquartile Range (IQR) of consumption: {iqr_consumption_0148}")

# Step 12: Calculate Correlation Between Price and Consumption
cor_price_consumption = AmogVardhanKona[['price', 'consumption']].corr().iloc[0, 1]
print(f"Correlation between price and consumption: {cor_price_consumption}")

# Step 13: Univariate Analysis (Plots)

# 13.1 Distribution Plot: Histogram for consumption
plt.figure(figsize=(8, 6))
plt.hist(AmogVardhanKona['consumption'], bins=20, color='lightblue', edgecolor='black')
plt.title('21BDS0148 - Consumption Distribution Plot')
plt.xlabel('Consumption')
plt.ylabel('Frequency')
plt.show()

# Histogram for consumption using Seaborn
sns.histplot(AmogVardhanKona['consumption'], kde=False, bins=20, color='lightblue')
plt.title('21BDS0148 - Consumption Distribution Plot')
plt.xlabel('Consumption')
plt.ylabel('Frequency')
plt.show()

# 13.2 Distribution Plot Histogram for price
plt.figure(figsize=(8, 6))
plt.hist(AmogVardhanKona['price'], bins=20, color='lightgreen', edgecolor='black')
plt.title('21BDS0148 - Price Distribution Plot')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# 13.3 Distribution Plot Density for price
plt.figure(figsize=(8, 6))
sns.kdeplot(AmogVardhanKona['price'], shade=True, color='purple')
plt.title('21BDS0148 - Price Density Plot')
plt.xlabel('Price')
plt.ylabel('Density')
plt.show()

# 13.4 Distribution Plot (Histogram + Density for price)
plt.figure(figsize=(8, 6))
sns.histplot(AmogVardhanKona['price'], kde=True, bins=20, color='lightgreen', line_kws={'color': 'purple'})
plt.title('21BDS0148 - Price Histogram and Density Plot')
plt.xlabel('Price')
plt.ylabel('Frequency/Density')
plt.show()

# 13.5 Boxplot for price
plt.figure(figsize=(8, 6))
sns.boxplot(x=AmogVardhanKona['price'], color='lightblue')
plt.title('21BDS0148 - Price Boxplot')
plt.xlabel('Price')
plt.show()

# 13.6 Display a Barplot for 'state' (Vertical and Horizontal)
# Vertical Barplot
plt.figure(figsize=(12, 6))
sns.countplot(x='state', data=AmogVardhanKona, palette='Blues')
plt.title('21BDS0148 - Barplot of States')
plt.xlabel('State')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Horizontal Barplot
plt.figure(figsize=(8, 10))
sns.countplot(y='state', data=AmogVardhanKona, palette='Blues')
plt.title('21BDS0148 - Barplot of States')
plt.xlabel('Count')
plt.ylabel('State')
plt.show()

# 13.7 Display Pie Plot for State
state_counts = AmogVardhanKona['state'].value_counts()
plt.figure(figsize=(10, 8))
plt.pie(state_counts, labels=state_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2'))
plt.title('21BDS0148 - Pie Chart for States')
plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
plt.show()

# 13.8 Display Dot Plot for 'price'
plt.figure(figsize=(10, 6))
sns.stripplot(x=AmogVardhanKona['price'], color='purple', jitter=True, size=6)
plt.title('21BDS0148 - Dot Plot for Price')
plt.xlabel('Price')
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
AmogVardhanKona = pd.read_csv('eda_data_21BDS0148.csv')

# Step 1: Replace '?' with NaN (if applicable)
AmogVardhanKona.replace('?', np.nan, inplace=True)

# Step 2: Convert columns that should be numeric to numeric, coercing errors to NaN
numeric_columns = ['consumption', 'price', 'eprice', 'oprice', 'lprice', 'heating', 'income']
for col in numeric_columns:
    AmogVardhanKona[col] = pd.to_numeric(AmogVardhanKona[col], errors='coerce')

# Step 3: Handle missing values after conversion to numeric (impute missing values)
numeric_cols_0148 = AmogVardhanKona.select_dtypes(include=['float64', 'int64']).columns
AmogVardhanKona[numeric_cols_0148] = AmogVardhanKona[numeric_cols_0148].fillna(AmogVardhanKona[numeric_cols_0148].mean())

# Step 4: Handle missing values in non-numeric columns by using the mode (most frequent value)
non_numeric_cols_0148 = AmogVardhanKona.select_dtypes(exclude=['float64', 'int64']).columns
for col in non_numeric_cols_0148:
    AmogVardhanKona[col] = AmogVardhanKona[col].fillna(AmogVardhanKona[col].mode()[0])

# Step 5: Check for remaining missing values
print("Missing values after imputation:\n", AmogVardhanKona.isna().sum())

# Bivariate and Multivariate Analysis

# 1. Categorical vs Categorical: Stacked Bar Plot (state vs year)
plt.figure(figsize=(12, 6))
sns.countplot(data=AmogVardhanKona, x="state", hue='year', dodge=False, palette='Set2')
plt.title("21BDS0148 - Stacked Bar Plot: State vs Year")
plt.xlabel('State')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 2. Categorical vs Quantitative: Bar Plot (Price vs State)
plt.figure(figsize=(12, 6))
sns.barplot(data=AmogVardhanKona, x='state', y='price', palette='Set2')
plt.title("21BDS0148 - Bar Chart: Price vs State")
plt.xlabel('State')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Quantitative vs Quantitative: Scatter Plot (Price vs Consumption)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=AmogVardhanKona, x='price', y='consumption', hue='state', palette='Set2')
plt.title("21BDS0148 - Scatter Plot: Price vs Consumption")
plt.xlabel('Price')
plt.ylabel('Consumption')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 4. Quantitative vs Quantitative: Heatmap (Correlation matrix)
numeric_data_0148 = AmogVardhanKona.select_dtypes(include=['number'])
corr_matrix_0148 = numeric_data_0148.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix_0148, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("21BDS0148 - Heatmap of Correlation Matrix")
plt.tight_layout()
plt.show()

# 5. Categorical vs Quantitative: Density Plot (Price vs State)
plt.figure(figsize=(10, 6))
sns.kdeplot(data=AmogVardhanKona, x='price', hue='state', fill=True, palette='Set2')
plt.title("21BDS0148 - Density Plot: Price vs State")
plt.xlabel('Price')
plt.ylabel('Density')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 6. Categorical vs Quantitative: Box Plot (Price vs State)
plt.figure(figsize=(12, 6))
sns.boxplot(data=AmogVardhanKona, x='state', y='price', palette='Set2')
plt.title("21BDS0148 - Box Plot: Price vs State")
plt.xlabel('State')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""#Time Series"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.linear_model import LinearRegression

# Load the dataset
file_path = 'eda_data_21BDS0148.csv'  # Update with your file path if needed
data = pd.read_csv(file_path)


# Convert year column into datetime format
data['year'] = pd.to_datetime(data['year'], format='%Y')

# Set year as the index for time series analysis
data.set_index('year', inplace=True)

ny_data = data[data['state'] == 'NY']

#1. Decomposition Plot
decomposition = seasonal_decompose(ny_data['consumption'], model='additive')
decomposition.plot()
plt.suptitle("21BDS0148 - Trend and Residuals (Yearly Data)")
plt.show()

# 2. Plot the dataset (consumption over time)
ny_data['consumption'].plot(title="21BDS0148 - NY Consumption Dataset")
plt.xlabel('Year')
plt.ylabel('Consumption')
plt.show()

# 3. Time Series Plot (consumption over time)
plt.figure(figsize=(10, 6))
plt.plot(ny_data.index, ny_data['consumption'])
plt.title("21BDS0148 - Time Series Plot of NY Consumption")
plt.xlabel('Year')
plt.ylabel('Consumption')
plt.show()

# 4. Linear Regression to identify trends in consumption
ny_data['time'] = np.arange(len(ny_data))
X = ny_data['time'].values.reshape(-1, 1)
y = ny_data['consumption']

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

plt.figure(figsize=(10, 6))
plt.plot(ny_data.index, ny_data['consumption'], label='Consumption')
plt.plot(ny_data.index, y_pred, color='red', label='Linear Trend Line')
plt.title("21BDS0148 - NY Consumption with Linear Trend Line")
plt.xlabel('Year')
plt.ylabel('Consumption')
plt.legend()
plt.show()

# 5. Cycle across years (monthly seasonality detection)
print("\nCycle across the years:")
print(ny_data.index.to_period('M').month)  # Cycle (months)

# 6. Make the dataset stationary
# a. Log transformation
ny_data['log_consumption'] = np.log(ny_data['consumption'])

plt.figure(figsize=(10, 6))
plt.plot(ny_data.index, ny_data['log_consumption'])
plt.title("21BDS0148 - Log Transformation of NY Consumption")
plt.xlabel('Year')
plt.ylabel('Log of Consumption')
plt.show()

# b. Differencing to make the data stationary
ny_data['stationary_consumption'] = ny_data['log_consumption'].diff().dropna()

plt.figure(figsize=(10, 6))
plt.plot(ny_data.index[1:], ny_data['stationary_consumption'][1:])
plt.title("21BDS0148 - Stationary Series (Differenced Log)")
plt.xlabel('Year')
plt.ylabel('Differenced Log of Consumption')
plt.show()

# 7. Box plot across months for seasonal effect
ny_data['month'] = ny_data.index.month  # Extract month from datetime index

plt.figure(figsize=(10, 6))
sns.boxplot(x=ny_data['month'], y=ny_data['consumption'])
plt.title("21BDS0148 - Box Plot Across Months for Seasonal Effect")
plt.xlabel('Month')
plt.ylabel('Consumption')
plt.show()

"""# Module-4"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, skew, kurtosis

data = pd.read_csv('eda_data_21BDS0148.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Ensure all columns are numeric (convert non-numeric values to NaN)
data = data.apply(pd.to_numeric, errors='coerce')

# Check column names to confirm their exact names
print("Column names in the dataset:")
print(data.columns)

# 1. Measure of Central Tendency

## Mean (Arithmetic Mean)
mean_values = data.mean()
print("\nMean for each variable:")
print(mean_values)

## Median
median_values = data.median()
print("\nMedian for each variable:")
print(median_values)

## Quantiles (25%, 50%, 75%)
quantile_values = data.quantile([0.25, 0.5, 0.75])
print("\nQuantiles (25%, 50%, 75%) for each variable:")
print(quantile_values)

## Deciles (using pd.qcut)
if 'consumption' in data.columns:
    deciles = pd.qcut(data['consumption'], 10, labels=False) + 1  # Create deciles for 'consumption'
    print("\nDeciles for consumption variable:")
    print(deciles.value_counts())

## Percentiles (10%, 50%, 90%)
percentile_values = data.quantile([0.1, 0.5, 0.9])
print("\nPercentiles (10%, 50%, 90%) for each variable:")
print(percentile_values)

# 2. Measure of Dispersions

## Range (max - min)
range_values = data.max() - data.min()
print("\nRange for each variable:")
print(range_values)

## Interquartile Range (IQR)
iqr_values = data.quantile(0.75) - data.quantile(0.25)
print("\nInterquartile Range (IQR) for each variable:")
print(iqr_values)

## Interdecile Range (90th - 10th percentile)
interdecile_values = data.quantile(0.9) - data.quantile(0.1)
print("\nInterdecile Range for each variable:")
print(interdecile_values)

## Standard Deviation
sd_values = data.std()
print("\nStandard Deviation for each variable:")
print(sd_values)

## Variance
variance_values = data.var()
print("\nVariance for each variable:")
print(variance_values)

## Skewness
skewness_values = data.apply(skew)
print("\nSkewness for each variable:")
print(skewness_values)

## Kurtosis
kurtosis_values = data.apply(kurtosis)
print("\nKurtosis for each variable:")
print(kurtosis_values)

# 3. Frequency Distribution

## Frequency Distribution (Table)
freq_table = data.apply(pd.value_counts)
print("\nFrequency distribution for each variable:")
print(freq_table)

## Histogram
plt.figure(figsize=(10, 8))

# Plot histogram for key numeric variables if they exist in the dataset
if 'consumption' in data.columns:
    plt.subplot(2, 2, 1)
    data['consumption'].hist(color='skyblue', edgecolor='black')
    plt.title('21BDS0148 - Histogram of Consumption')
    plt.xlabel('Consumption')
    plt.ylabel('Frequency')

if 'price' in data.columns:
    plt.subplot(2, 2, 2)
    data['price'].hist(color='lightgreen', edgecolor='black')
    plt.title('21BDS0148 - Histogram of Price')
    plt.xlabel('Price')
    plt.ylabel('Frequency')

if 'income' in data.columns:
    plt.subplot(2, 2, 3)
    data['income'].hist(color='lightcoral', edgecolor='black')
    plt.title('21BDS0148 - Histogram of Income')
    plt.xlabel('Income')
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

## Relative Frequency Distribution
if 'consumption' in data.columns:
    relative_freq_consumption = data['consumption'].value_counts(normalize=True)
    print("\nRelative Frequency Distribution for Consumption:")
    print(relative_freq_consumption)

## Cumulative Frequency Distribution
if 'consumption' in data.columns:
    cumulative_freq_consumption = data['consumption'].value_counts().cumsum()
    print("\nCumulative Frequency Distribution for Consumption:")
    print(cumulative_freq_consumption)

# 4. Categorical Variable Analysis

## Check if 'statecode' column is available
if 'statecode' in data.columns:
    # Pie Plot for state codes
    state_counts = data['statecode'].value_counts()
    plt.figure(figsize=(7, 7))
    state_counts.plot.pie(autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral'], startangle=90)
    plt.title('21BDS0148 - Pie Plot for State Codes')
    plt.ylabel('')
    plt.show()

# Stacked Bar Plot for state vs year if both columns exist
if 'statecode' in data.columns and 'year' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(x='statecode', hue='year', data=data, palette="Set2")
    plt.title("21BDS0148 - Stacked Bar Plot for State Codes and Year")
    plt.xlabel("State Code")
    plt.ylabel("Count")
    plt.show()
else:
    print("Columns 'statecode' or 'year' not found in the dataset.")

# 5. Summary Statistics
mean_values = data.mean()
median_values = data.median()
iqr_values = data.quantile(0.75) - data.quantile(0.25)
sd_values = data.std()
skewness_values = data.apply(skew)
kurtosis_values = data.apply(kurtosis)

summary_stats = pd.DataFrame({
    'Mean': mean_values,
    'Median': median_values,
    'IQR': iqr_values,
    'Standard Deviation': sd_values,
    'Skewness': skewness_values,
    'Kurtosis': kurtosis_values
})
print("\nSummary Statistics for the dataset:")
print(summary_stats)

# 6.. Contingency Tables and Chi-Square Test
if 'statecode' in data.columns and 'year' in data.columns:
    contingency_table_2way = pd.crosstab(data['statecode'], data['year'])
    print("\nContingency Table (Statecode vs Year):")
    print(contingency_table_2way)

    # Chi-Square Test on the 2-way contingency table
    chi2, p, dof, expected = chi2_contingency(contingency_table_2way)
    print(f"\nChi-Square Test Result:\nChi2: {chi2}, P-value: {p}, Degrees of Freedom: {dof}")
    print("Expected Frequencies:")
    print(expected)

    # Row Profile
    row_profile = contingency_table_2way.div(contingency_table_2way.sum(axis=1), axis=0)
    print("\nRow Profile (Proportions per Row):")
    print(row_profile)

    # Column Profile
    column_profile = contingency_table_2way.div(contingency_table_2way.sum(axis=0), axis=1)
    print("\nColumn Profile (Proportions per Column):")
    print(column_profile)

# 7. Scatter Plot: Age vs Fare with Survival Status (using consumption and price as substitutes)
if 'consumption' in data.columns and 'price' in data.columns:
    sns.scatterplot(x='consumption', y='price', hue='statecode', data=data)
    plt.title('Scatter Plot: Consumption vs Price with State Code')
    plt.show()

# 8. Boxplot: Statecode vs Consumption
if 'statecode' in data.columns and 'consumption' in data.columns:
    sns.boxplot(x='statecode', y='consumption', data=data)
    plt.title('Boxplot: State Code vs Consumption')
    plt.show()

# 9. Radar Chart (Sunray Plot) using selected variables
categories = ['consumption', 'price', 'eprice', 'oprice', 'income']
values = [
    data['consumption'].mean(),  # Mean Consumption
    data['price'].mean(),        # Mean Price
    data['eprice'].mean(),       # Mean Effective Price
    data['oprice'].mean(),       # Mean Other Price
    data['income'].mean()        # Mean Income
]

values.append(values[0])

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles.append(angles[0])  # Ensure the loop is closed

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, polar=True)

ax.fill(angles, values, color='skyblue', alpha=0.25)
ax.plot(angles, values, color='blue', linewidth=2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

plt.title("21BDS0148 - Sunray Plot (Radar Chart)")
plt.show()

"""#Module 5"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist, squareform

from sklearn.preprocessing import StandardScaler

data = pd.read_csv('eda_data_21BDS0148.csv')

# Select relevant columns for clustering ('consumption' and 'price')
X = data[['consumption', 'price']].values  # Extract relevant columns

# Feature Scaling - Standardize the data before clustering
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 1. Elbow Method to find the optimal number of clusters
wcss = []  # List to store the within-cluster sum of squares (WCSS)
for i in range(1, 11):  # Try from 1 to 10 clusters
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)  # WCSS is the inertia value

# Plotting the elbow graph to determine the optimal number of clusters
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker='o', color='blue')
plt.title('Elbow Method for Optimal Number of Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()

optimal_clusters = 3

kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', max_iter=300, n_init=10, random_state=42)
y_kmeans = kmeans.fit_predict(X_scaled)

# Plotting the clusters
plt.figure(figsize=(10, 6))
plt.scatter(X_scaled[y_kmeans == 0, 0], X_scaled[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(X_scaled[y_kmeans == 1, 0], X_scaled[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(X_scaled[y_kmeans == 2, 0], X_scaled[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
plt.scatter(X_scaled[y_kmeans == 3, 0], X_scaled[y_kmeans == 3, 1], s=100, c='cyan', label='Cluster 4')
plt.scatter(X_scaled[y_kmeans == 4, 0], X_scaled[y_kmeans == 4, 1], s=100, c='magenta', label='Cluster 5')

# Plot the centroids
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('Consumption (scaled)')
plt.ylabel('Price (scaled)')
plt.legend()
plt.grid(True)
plt.show()

# Perform hierarchical clustering using Ward's method
linkage_matrix = linkage(X_scaled, method='ward')

# Plot dendrogram for hierarchical clustering
plt.figure(figsize=(12, 8))
dendrogram(linkage_matrix)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Euclidean Distance')
plt.show()

X = data[['consumption', 'price']].values

# Standardize the data before clustering
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Function to compute distance matrix and plot dendrogram for a given metric
def hierarchical_clustering(metric, method='average', p=None):
    # Compute distance matrix
    if metric == 'minkowski' and p is not None:
        distance_matrix = pdist(X_scaled, metric=metric, p=p)
    else:
        distance_matrix = pdist(X_scaled, metric=metric)
    distance_matrix = squareform(distance_matrix)

    # display only the first 5 rows and columns of the distance matrix
    print(f"\nDistance Matrix ({metric.capitalize()}):\n", distance_matrix[:5, :5])

    # perform hierarchical clustering
    Z = linkage(X_scaled, method=method, metric=metric)

    # display only the first 5 rows of the linkage matrix
    print(f"\nLinkage Matrix ({metric.capitalize()}):\n", Z[:5])

    # plot dendrogram
    plt.figure(figsize=(10, 6))
    dendrogram(Z)
    plt.title(f'Dendrogram ({metric.capitalize()} Distance)')
    plt.xlabel('Data Points')
    plt.ylabel(f'{metric.capitalize()} Distance')
    plt.show()

# 1. Manhattan Distance (Cityblock)
hierarchical_clustering(metric='cityblock')

# 2. Maximum Distance (Chebyshev)
hierarchical_clustering(metric='chebyshev')

# 3. Canberra Distance
hierarchical_clustering(metric='canberra')

# 4. Binary Distance (Jaccard)
hierarchical_clustering(metric='jaccard')

# 5. Minkowski Distance (p=3)
hierarchical_clustering(metric='minkowski', p=3)

"""#Module 6"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Using 'consumption' and 'price' as numeric columns for PCA
data_numeric = data[['consumption', 'price']]

# Standardizing the data (important for PCA)
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_numeric)

# Perform PCA
pca = PCA()
pca_result = pca.fit_transform(data_scaled)

# Print PCA results - Eigenvalues and loadings
print("\nEigenvalues:")
print(pca.explained_variance_)

print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

print("\nPCA Components:")
print(pca.components_)

# Plot the explained variance ratio (Scree plot)
plt.figure(figsize=(8, 6))
plt.plot(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_, marker='o', linestyle='--')
plt.title("Scree Plot")
plt.xlabel("Principal Component")
plt.ylabel("Explained Variance Ratio")
plt.grid(True)
plt.show()

# Visualizing the first two principal components
plt.figure(figsize=(8, 6))
sns.scatterplot(x=pca_result[:, 0], y=pca_result[:, 1], palette='viridis')
plt.title("PCA - First Two Principal Components")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.show()

# Plot the first two components as a biplot (variables and individuals)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=pca_result[:, 0], y=pca_result[:, 1], color='blue', label='Individuals')

# Plotting the components (loadings) on the same plot
for i, feature in enumerate(data_numeric.columns):
    plt.arrow(0, 0, pca.components_[0][i], pca.components_[1][i], color='red', alpha=0.5)
    plt.text(pca.components_[0][i] * 1.2, pca.components_[1][i] * 1.2, feature, color='red', ha='center', va='center')

plt.title("PCA - Biplot")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.show()

# Summary of PCA results
print("\nSummary of PCA:")
print("Explained Variance (Eigenvalues):", pca.explained_variance_)
print("Explained Variance Ratio:", pca.explained_variance_ratio_)
print("Cumulative Explained Variance:", np.cumsum(pca.explained_variance_ratio_))

# Selecting the first two components (if they explain most of the variance)
n_components = 2
pca_result_selected = pca_result[:, :n_components]

# Visualize the selected PCA components
plt.figure(figsize=(8, 6))
sns.scatterplot(x=pca_result_selected[:, 0], y=pca_result_selected[:, 1], palette='viridis')
plt.title("Selected PCA - First Two Components")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.show()
