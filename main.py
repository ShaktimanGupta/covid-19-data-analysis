# COVID-19 Data Analysis Project
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('covid_19_data.csv')  # Replace with your dataset path

# Basic information
print(data.head())
print(data.info())

# Cleaning
data = data.rename(columns={'Country/Region': 'Country'})
data['Date'] = pd.to_datetime(data['ObservationDate'])

# Group by Country
country_data = data.groupby('Country')[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()

# Top 10 countries by confirmed cases
top_countries = country_data.sort_values('Confirmed', ascending=False).head(10)

# Plotting
plt.figure(figsize=(12, 6))
plt.bar(top_countries['Country'], top_countries['Confirmed'], color='skyblue')
plt.title('Top 10 Countries by Confirmed COVID-19 Cases')
plt.xlabel('Country')
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=45)
plt.show()

# Fatality rate
country_data['Fatality Rate (%)'] = (country_data['Deaths'] / country_data['Confirmed']) * 100
print(country_data[['Country', 'Fatality Rate (%)']].sort_values('Fatality Rate (%)', ascending=False).head(10))
