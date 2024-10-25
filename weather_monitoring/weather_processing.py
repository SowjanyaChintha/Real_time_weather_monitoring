import pandas as pd

def process_weather_data(weather_data):
    """Process raw weather data from the API and return structured data."""
    
    if not all(key in weather_data for key in ['name', 'main', 'weather', 'dt']):
        print("Invalid weather data received:", weather_data)
        return None

    processed_data = {
        'city': weather_data['name'],
        'avg_temp': weather_data['main']['temp'],  # Ensure it's in Celsius
        'max_temp': weather_data['main']['temp_max'],
        'min_temp': weather_data['main']['temp_min'],
        'dominant_weather': weather_data['weather'][0]['description'],
        'date': pd.to_datetime(weather_data['dt'], unit='s').strftime('%Y-%m-%d')
    }

    print("Processed data:", processed_data)  # Log the processed data
    return processed_data


def generate_daily_summary(data_frame):
    """Generate daily summaries from processed weather data."""
    
    # Check if the DataFrame is empty
    if data_frame.empty:
        return None
    
    # Assuming data_frame contains columns: 'date', 'avg_temp', 'max_temp', 'min_temp', 'dominant_weather'
    daily_summary = {
        'date': data_frame['date'].iloc[0],  # Assuming all entries are for the same day
        'avg_temp': data_frame['avg_temp'].mean(),  # Average temperature
        'max_temp': data_frame['max_temp'].max(),  # Maximum temperature
        'min_temp': data_frame['min_temp'].min(),  # Minimum temperature
        'dominant_weather': data_frame['dominant_weather'].mode()[0]  # Most common weather description
    }
    
    return daily_summary
