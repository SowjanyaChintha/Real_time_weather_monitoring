from flask import Flask, render_template
import weather_processing as wp
import db_storage as db
import visualization as viz
import weather_api as api  # Import your weather API module
import datetime
import pandas as pd
from alert_system import WeatherAlert  # Import the WeatherAlert class

app = Flask(__name__)
db.init_db()

# Define the temperature threshold and number of consecutive updates
temperature_threshold = 35  # Example threshold in Celsius
consecutive_updates = 2  # Example consecutive count for alert
weather_alert = WeatherAlert(temperature_threshold, consecutive_updates)

@app.route('/')
def index():
    # Define the cities to monitor
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

    for city in cities:
        weather_data = api.get_weather_data(city)
        if weather_data:
            processed_data = wp.process_weather_data(weather_data)
            date = datetime.datetime.now().strftime('%Y-%m-%d')

            # Generate daily summary
            daily_summary = wp.generate_daily_summary(pd.DataFrame([processed_data]))

            # Store the summary in the database
            db.store_daily_summary( 
                date, 
                city, 
                daily_summary['avg_temp'], 
                daily_summary['max_temp'], 
                daily_summary['min_temp'], 
                daily_summary['dominant_weather']
            )
            
            # Check alert for the current temperature
            current_temp = daily_summary['avg_temp']  # Assuming avg_temp is in Celsius
            weather_alert.check_alert(current_temp)

    daily_summaries = db.fetch_all_summaries()
    for summary in daily_summaries:
        if None in summary:
            print(f"Found None in summary: {summary}")
    cleaned_summaries = [
        [elem if elem is not None else 'N/A' for elem in summary]
        for summary in daily_summaries
    ]
    
    # Generate the daily summary visualization
    plot_path = viz.plot_daily_summary(daily_summaries)
    
    return render_template('index.html', summaries=cleaned_summaries, plot_path=plot_path)

if __name__ == '__main__':
    app.run(debug=True)
