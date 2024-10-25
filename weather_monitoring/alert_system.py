import time
from datetime import datetime

class WeatherAlert:
    def __init__(self, temperature_threshold, consecutive_updates):
        self.temperature_threshold = temperature_threshold
        self.consecutive_updates = consecutive_updates
        self.violation_count = 0

    def check_alert(self, current_temp):
        if current_temp > self.temperature_threshold:
            self.violation_count += 1
            if self.violation_count >= self.consecutive_updates:
                print(f"ALERT: Temperature exceeds {self.temperature_threshold}°C for {self.consecutive_updates} consecutive updates!")
        else:
            self.violation_count = 0  # Reset count if the threshold is not breached

def monitor_weather(alert_system):
    # Simulated weather data for testing
    weather_data = [
        {"date": "2024-10-21", "city": "Delhi", "temperature": 36},
        {"date": "2024-10-22", "city": "Delhi", "temperature": 37},
        {"date": "2024-10-23", "city": "Delhi", "temperature": 34},
        {"date": "2024-10-24", "city": "Delhi", "temperature": 38},
        {"date": "2024-10-25", "city": "Delhi", "temperature": 39},
    ]

    for data in weather_data:
        current_temp = data["temperature"]
        alert_system.check_alert(current_temp)
        time.sleep(1)  # Simulate time delay between updates

if __name__ == "__main__":
    # Define your temperature threshold and number of consecutive updates
    temperature_threshold = 35  # Example threshold in Celsius
    consecutive_updates = 2  # Example consecutive count for alert

    weather_alert = WeatherAlert(temperature_threshold, consecutive_updates)
    monitor_weather(weather_alert)
