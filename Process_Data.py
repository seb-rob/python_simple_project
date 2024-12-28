import matplotlib.pyplot as plt
import pandas as pd

# function to read log_generator_errors.py
def read_data(filename):
    """
        function reads specified file for analysis
    """
    try:
        df = pd.read_csv(filename, delimiter=' - ', header=None, names=["Datetime", "LogLevel", "Actions", "Users"])
        # Extract log levels and count their occurrences
        log_levels = df["LogLevel"].value_counts()
        print("Log Levels:")
        print(log_levels)

        # Plotting the pie chart
        plt.figure(figsize=(7, 7))
        plt.pie(log_levels, labels=log_levels.index, autopct='%1.1f%%', startangle=90, colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"])
        plt.title("Distribution of Log Levels")
        plt.axis('equal')
        plt.show()

    except pd.errors.ParserError:
        print(f"Error: Couldn't parse {filename}. Ensure it's a CSV or compatible format.")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


read_data("./log_generator_errors.txt")