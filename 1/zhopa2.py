import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy.signal import find_peaks
import numpy as np

# This file is for data that starts from the second peak which breaks the zhopa.py code
for file_number in [15,27]:
    # Set up the file path
    csv_file_path = f"labs/csv/1/NewFile{file_number}.csv"
    
    try:
        # Load the data
        df = pd.read_csv(csv_file_path)

        # Convert to numeric, handling non-numeric values
        for channel in ['CH1', 'CH2', 'CH3', 'CH4']:
            df[channel] = pd.to_numeric(df[channel], errors='coerce')

        # Detect peaks in 'CH4' data to analyze the rotation cycles
        peaks, _ = find_peaks(df['CH4'], height=0.54)  # Adjust height threshold if needed

        # Calculate phase angles, skipping every second peak, STARTING FROM THE SECOND ONE
        phase_angles = np.zeros(len(df['CH4']))
        for i in range(2, len(peaks) - 1, 2):  # Skip every second peak
            start, end = peaks[i - 1], peaks[i + 1]  # Use only odd-indexed peaks
            cycle_length = end - start
            # Linearly interpolate phase from 0 to 2π within each cycle
            phase_angles[start:end] = np.linspace(0, 2 * np.pi, cycle_length, endpoint=False)

        # Volume calculation using the phase angle in place of the original cosine argument
        hot_volume = 6.7 * 10**(-2) * math.pi * ((2.4 * 10**(-2)) / 2)**2
        cold_volume = 3.9 * 10**(-2) * math.pi * ((2.4 * 10**(-2)) / 2)**2
        parasite = 2.3 * 10**(-2) * math.pi * ((2.4 * 10**(-2)) / 2)**2
        volume = cold_volume + hot_volume / 2 * (1 + np.cos(phase_angles)) + parasite

        # Calculate the pressure
        pressure = df['CH3'] / (1.17*10**(-2))

        # Plotting CH4 vs CH3 for each file
        plt.figure(figsize=(10, 8))
        plt.plot(volume, pressure, color='purple')
        plt.xlabel('Volume, m^3')
        plt.ylabel('Pressure, kPa')
        plt.title(f'PV diagram for file {file_number}')
        # Save the figure
        output_path = f"labs/img/PV/PV_NewFile{file_number}.png"
        plt.savefig(output_path)
        plt.close()  # Close the figure to free memory

        print(f"Saved plot for NewFile{file_number} as {output_path}")

    except FileNotFoundError:
        print(f"File NewFile{file_number}.csv not found, skipping.")

