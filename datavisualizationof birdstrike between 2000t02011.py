import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = r"C:\Users\HP\Downloads\Bird Strikes data.xlsx"  
data = pd.ExcelFile(file_path)
bird_strikes_data = data.parse('Bird Strikes')
bird_strikes_data['FlightDate'] = pd.to_datetime(bird_strikes_data['FlightDate'], errors='coerce')
bird_strikes_data['Year'] = bird_strikes_data['FlightDate'].dt.year
def plot_strikes_per_year(data):
    yearly_data = data.groupby('Year').size()
    plt.figure(figsize=(12, 6))
    yearly_data.plot(kind='bar', color='skyblue')
    plt.title('Number of Bird Strikes Per Year (2000-2011)', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Bird Strikes', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
#Top 10 aircraft models with bird strikes
def plot_top_aircraft(data):
    top_aircraft = data['Aircraft: Make/Model'].value_counts().head(10)
    plt.figure(figsize=(12, 6))
    top_aircraft.plot(kind='bar', color='orange')
    plt.title('Top 10 Aircraft Models with Bird Strikes', fontsize=14)
    plt.xlabel('Aircraft Make/Model', fontsize=12)
    plt.ylabel('Number of Bird Strikes', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
#Top 50 airports with bird strike incidents
def plot_top_airports(data):
    top_airports = data['Airport: Name'].value_counts().head(50)
    plt.figure(figsize=(12, 6))
    top_airports.plot(kind='bar', color='green')
    plt.title('Top 50 Airports with Bird Strikes', fontsize=14)
    plt.xlabel('Airport Name', fontsize=12)
    plt.ylabel('Number of Bird Strikes', fontsize=12)
    plt.xticks([], [])  # Avoid cluttering with too many labels
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
#Yearly cost incurred due to bird strikes
def plot_yearly_cost(data):
    cost_yearly = data.groupby('Year')['Cost: Total $'].sum()
    plt.figure(figsize=(12, 6))
    cost_yearly.plot(kind='line', marker='o', color='red')
    plt.title('Yearly Cost Incurred Due to Bird Strikes (2000-2011)', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Total Cost ($)', fontsize=12)
    plt.grid(axis='both', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
#Time of day analysis
def plot_time_of_day(data):
    time_of_day = data['Conditions: Sky'].value_counts()
    plt.figure(figsize=(8, 5))
    time_of_day.plot(kind='bar', color='purple')
    plt.title('Conditions of the Sky During Bird Strikes', fontsize=14)
    plt.xlabel('Condition', fontsize=12)
    plt.ylabel('Number of Bird Strikes', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
#Bird strikes by altitude
def plot_altitude_distribution(data):
    altitude_data = data['Altitude bin'].value_counts()
    plt.figure(figsize=(8, 5))
    altitude_data.plot(kind='bar', color='teal')
    plt.title('Bird Strikes by Altitude', fontsize=14)
    plt.xlabel('Altitude Bin', fontsize=12)
    plt.ylabel('Number of Bird Strikes', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
#Bird strikes by phase of flight
def plot_phase_of_flight(data):
    phase_data = data['Phase of flight'].value_counts()
    plt.figure(figsize=(10, 6))
    phase_data.plot(kind='bar', color='brown')
    plt.title('Bird Strikes by Phase of Flight', fontsize=14)
    plt.xlabel('Phase of Flight', fontsize=12)
    plt.ylabel('Number of Bird Strikes', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
#Impact of warnings
def plot_warnings(data):
    warnings_data = data['Pilot warned of birds or wildlife?'].value_counts()
    plt.figure(figsize=(6, 6))
    warnings_data.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['gold', 'lightblue'])
    plt.title('Were Pilots Warned About Birds?', fontsize=14)
    plt.ylabel('')
    plt.tight_layout()
    plt.show()
plot_strikes_per_year(bird_strikes_data)
plot_top_aircraft(bird_strikes_data)
plot_top_airports(bird_strikes_data)
plot_yearly_cost(bird_strikes_data)
plot_time_of_day(bird_strikes_data)
plot_altitude_distribution(bird_strikes_data)
plot_phase_of_flight(bird_strikes_data)
plot_warnings(bird_strikes_data)
