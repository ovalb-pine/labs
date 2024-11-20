import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy.signal import find_peaks
import numpy as np


# Loop through file numbers from 13 to 27
for file_number in range(1, 28):
    # Set up the file path
    csv_file_path = f"labs/csv/1/NewFile{file_number}.csv"
    
    try:
        # Load the data
        df = pd.read_csv(csv_file_path)

        # Convert to numeric, handling non-numeric values
        for channel in ['CH1', 'CH2', 'CH3', 'CH4']:
            df[channel] = pd.to_numeric(df[channel], errors='coerce')

        # For files starting from the 15th, only use the first half of the data
        if file_number >= 14:
            half_index = len(df) // 3
            df = df.iloc[:half_index]
            
        hot_volume = 6.7 * 10**(-2) * math.pi * ((2.4 * 10**(-2)) / 2)**2
        cold_volume = 3.9 * 10**(-2) * math.pi * ((2.4 * 10**(-2)) / 2)**2
        parasite = 2.3 * 10**(-2) * math.pi * ((2.4 * 10**(-2)) / 2)**2

        volume = cold_volume + hot_volume/2*(1+math.cos(df['CH4'])) + parasite

        # Plot each channel with title and color
        channels = ['CH1', 'CH2', 'CH3', 'CH4']
        colors = ['blue', 'green', 'red', 'purple']
        plt.figure(figsize=(10, 8))
        plt.plot(df['CH4'], df['CH3'])
        # Set a common x-axis label
        plt.xlabel(f'PV for file {file_number}')
        
        # Save the figure
        output_path = f"labs/img/PV_NewFile{file_number}.png"
        plt.savefig(output_path)
        plt.close()  # Close the figure to free memory

        print(f"Saved plot for NewFile{file_number} as {output_path}")

    except FileNotFoundError:
        print(f"File NewFile{file_number}.csv not found, skipping.")

"""длина 6.7 см
диаметр 2.4
паразитный длина 2.3

холодный
длина 3.9
диаметр 2.4"""


