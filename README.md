# Real-Time Weather Monitoring System

This project is a real-time weather monitoring system designed to gather, process, and display weather data using data from the OpenWeatherMap API. The application provides data aggregation, dynamic alerting, and visualizations, supporting continuous tracking of weather conditions and summary insights for various cities in India.

# Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Weather Monitoring](#weather-monitoring)
- [API Endpoints](#api-endpoints)

# Features

- Data Aggregation: Collects and stores real-time weather data, providing daily summaries.
- Dynamic Alerts: User-configurable thresholds for weather conditions like temperature and specific weather patterns trigger alerts.
- Data Visualization: Displays weather summaries and historical data for cities in India.
- Responsive Interface: Enables users to choose city and date for detailed weather insights.

# Project Structure

weather_monitoring/
│
├── app.py                 # Main application
├── weather_data.py        # Data retrieval and processing from OpenWeatherMap API
├── models.py              # SQLite models for data storage
├── alert_system.py        # Threshold-based alerting system
├── templates/
│   └── index.html         # Frontend interface
├── static/
│   └── style.css          # CSS styling
├── requirements.txt       # Project dependencies
└── database.db            # SQLite database file

Key Files
app.py: Initializes the application and configures the endpoints.
weather_data.py: Fetches and processes weather data.
alert_system.py: Monitors weather conditions and triggers alerts based on set thresholds.
index.html: User interface to interact with the application.
Setup Instructions
Prerequisites
Python 3.8+
Flask and SQLAlchemy
Installation
Clone the Repository:

git clone https://github.com/your-username/weather_monitoring.git
cd weather_monitoring
Create a Virtual Environment:
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
Install Dependencies:
pip install -r requirements.txt
Set Up Environment Variables:

Create a .env file and add your OpenWeatherMap API key:
OPENWEATHERMAP_API_KEY=your_api_key_here

Set Up the Database:
Run the following commands in a Python shell to initialize the database:
python
Copy code
from app import db
db.create_all()
Run the Application:

flask run
Access the application at http://127.0.0.1:5000.

Usage
Once the application is running, visit the app URL to access the user interface. You can:

View weather summaries.
Configure alert thresholds.
Select cities and dates for specific weather data.
Weather Monitoring
The system continuously retrieves weather data from OpenWeatherMap for various cities, storing it in the SQLite database. Weather summaries include:

Temperature: Average, max, and min temperatures.
Conditions: Dominant weather condition summaries (e.g., sunny, cloudy, etc.).

API Endpoints
1. GET /
Description: Renders the main HTML interface.
2. POST /update_weather_data
Description: Updates weather data for monitored cities in the database.
3. POST /set_alert_thresholds
Description: Configures alert thresholds for specified conditions.
Request Body:
{
  "city": "Mumbai",
  "temperature_threshold": 35,
  "condition": "Rain"
}
4. GET /weather_summary/<city>/<date>
Description: Retrieves weather summary for a specific city and date.
5. POST /check_alerts
