# main.py

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# Optional: set Seaborn style
sns.set(style="whitegrid")

# ---------------------- Step 1: Fetch Data ----------------------

def fetch_covid_data():
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        raise Exception("Failed to fetch data. Try again later.")

# ---------------------- Step 2: Clean Data ----------------------

def clean_data(df):
    df = df[[
        "country", "cases", "todayCases", "deaths", "todayDeaths",
        "recovered", "active", "critical", "population"
    ]]
    df["casesPerMillion"] = (df["cases"] / df["population"]) * 1e6
    df = df.sort_values(by="cases", ascending=False)
    return df

# ---------------------- Step 3: Visualizations ----------------------

def plot_top_10_cases(df):
    top10 = df.head(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x="cases", y="country", data=top10, palette="Reds_d")
    plt.title("Top 10 Countries with Most Covid-19 Cases")
    plt.xlabel("Total Cases")
    plt.ylabel("Country")
    plt.tight_layout()
    plt.savefig("top10_cases.png")
    plt.show()

def plot_deaths_vs_recovered(df):
    plt.figure(figsize=(10,6))
    sns.scatterplot(x="deaths", y="recovered", data=df, hue="country", legend=False)
    plt.title("Covid-19: Deaths vs Recovered")
    plt.xlabel("Total Deaths")
    plt.ylabel("Total Recovered")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("deaths_vs_recovered.png")
    plt.show()

def plot_world_map(df):
    fig = px.choropleth(df,
                        locations="country",
                        locationmode="country names",
                        color="cases",
                        hover_name="country",
                        color_continuous_scale="OrRd",
                        title="Global Covid-19 Cases")
    fig.write_html("world_map.html")
    fig.show()

# ---------------------- Step 4: Save Summary ----------------------

def save_summary(df):
    df.to_csv("covid_summary.csv", index=False)

# ---------------------- Main Program ----------------------

def main():
    print("Fetching data...")
    raw_df = fetch_covid_data()

    print("Cleaning data...")
    cleaned_df = clean_data(raw_df)

    print("Creating visualizations...")
    plot_top_10_cases(cleaned_df)
    plot_deaths_vs_recovered(cleaned_df)
    plot_world_map(cleaned_df)

    print("Saving data summary...")
    save_summary(cleaned_df)

    print("All tasks completed successfully!")

if __name__ == "__main__":
    main()
