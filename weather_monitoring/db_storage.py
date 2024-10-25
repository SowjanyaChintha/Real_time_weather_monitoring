import sqlite3

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_summary (
            city TEXT,
            date TEXT,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_weather TEXT,
            PRIMARY KEY (city, date)  -- Composite primary key
        )
    ''')
    conn.commit()
    conn.close()

# Store the daily summary in the database
def store_daily_summary(date, city, avg_temp, max_temp, min_temp, dominant_weather):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO daily_summary (city, date, avg_temp, max_temp, min_temp, dominant_weather)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (city, date, avg_temp, max_temp, min_temp, dominant_weather))
    conn.commit()
    conn.close()

# Fetch all daily summaries
def fetch_all_summaries():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT city, date, avg_temp, max_temp, min_temp, dominant_weather FROM daily_summary")
    results = cursor.fetchall()
    conn.close()
    return results
