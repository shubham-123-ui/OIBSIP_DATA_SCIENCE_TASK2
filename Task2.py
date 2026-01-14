# Unemployment Analysis with Python

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Admin\Desktop\Unemployment in India.csv")

# Rename columns for easy access (optional but recommended)
df.columns = df.columns.str.strip()

print(df.head())
print(df.info())

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Drop missing values
df.dropna(inplace=True)

plt.figure()
plt.plot(df['Date'], df['Estimated Unemployment Rate (%)'])
plt.title("Unemployment Rate Over Time in India")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.show()

region_avg = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()

plt.figure()
region_avg.plot(kind='bar')
plt.title("Average Unemployment Rate by Region")
plt.xlabel("Region")
plt.ylabel("Unemployment Rate (%)")
plt.show()


plt.figure()
plt.plot(df['Date'], df['Estimated Labour Participation Rate (%)'])
plt.title("Labour Participation Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Labour Participation Rate (%)")
plt.show()

plt.figure()
plt.plot(df['Date'], df['Estimated Employed'])
plt.title("Employment Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Employed People")
plt.show()

print("Highest Unemployment Rate:", df['Estimated Unemployment Rate (%)'].max())
print("Lowest Unemployment Rate:", df['Estimated Unemployment Rate (%)'].min())
print("Average Unemployment Rate:", df['Estimated Unemployment Rate (%)'].mean())
