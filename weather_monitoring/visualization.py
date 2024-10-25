import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_daily_summary(daily_summaries):
    # Replace None values in the DataFrame
    df = pd.DataFrame(daily_summaries, columns=['date', 'city', 'avg_temp', 'max_temp', 'min_temp', 'dominant_weather']).fillna('N/A')

    plt.figure(figsize=(10, 6))
    
    # Handle cases where the data might not be valid
    try:
        plt.bar(df['date'], df['avg_temp'], color='skyblue', label='Avg Temp')
        plt.bar(df['date'], df['max_temp'], color='lightcoral', label='Max Temp')
        plt.bar(df['date'], df['min_temp'], color='lightgreen', label='Min Temp')
    except TypeError as e:
        print(f"Plotting error: {e}")
    
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()

    plot_path = os.path.join('static', 'summary_plot.png')
    plt.savefig(plot_path)
    plt.close()

    return plot_path
