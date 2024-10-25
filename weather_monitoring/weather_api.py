import requests

def get_weather_data(city):
    """Fetch weather data for a specified city from the OpenWeatherMap API."""
    api_key = 'e6050d78cd49459562a9d2b94bbae8ac'  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'  # 'units=metric' for Celsius
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        weather_data = response.json()
        
        # Log the retrieved weather data
        print(f"Weather data for {city}: {weather_data}")
        
        return weather_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {city}: {str(e)}")
        return None
