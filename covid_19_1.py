import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

#  Load the CSV file 
# Make sure the CSV is in the same folder or provide full path
file_path = "owid-covid-data.csv" 

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print("CSV file not found. Please check the path and file name.")
    exit()

# Clean column names and check structure
df.columns = df.columns.str.strip()  # Remove leading/trailing spaces
print("Available columns:\n", df.columns)

# Filter for India 
if 'location' not in df.columns:
    print("Column 'location' not found in CSV.")
    exit()

india_df = df[df['location'] == 'India']

# Select and clean columns
columns_needed = ['date', 'total_cases', 'total_deaths', 'new_cases', 'new_deaths']
available_columns = [col for col in columns_needed if col in india_df.columns]

if not available_columns:
    print("Required columns not found. Please verify dataset format.")
    exit()

india_df = india_df[available_columns].dropna()
india_df['date'] = pd.to_datetime(india_df['date'])

# === Step 5: Matplotlib Plot ===
plt.figure(figsize=(12, 6))
plt.plot(india_df['date'], india_df['total_cases'], label='Total Cases', color='blue')
plt.plot(india_df['date'], india_df['total_deaths'], label='Total Deaths', color='red')
plt.xlabel("Date")
plt.ylabel("Count")
plt.title("COVID-19 Trends in India")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

