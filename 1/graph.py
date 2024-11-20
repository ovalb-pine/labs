import pandas as pd
import matplotlib.pyplot as plt

# Loop through file numbers from 13 to 27
for file_number in range(1, 28):
    # Set up the file path
    csv_file_path = f"labs/csv/1/NewFile{file_number}aa.csv"
    
    try:
        # Load the data
        df = pd.read_csv(csv_file_path)

        # Convert to numeric, handling non-numeric values
        for channel in ['CH1', 'CH2', 'CH3', 'CH4']:
            df[channel] = pd.to_numeric(df[channel], errors='coerce')

        # # For files starting from the 15th, only use the first half of the data
        # if file_number >= 14:
        #     half_index = len(df) // 3
        #     df = df.iloc[:half_index]

        # Create a figure and set of subplots
        fig, axs = plt.subplots(4, 1, figsize=(10, 8), sharex=True)

        # Plot each channel with title and color
        channels = ['CH1', 'CH2', 'CH3', 'CH4']
        colors = ['blue', 'green', 'red', 'purple']
        
        for i, channel in enumerate(channels):
            axs[i].plot(df[channel], color=colors[i])
            axs[i].set_title(f'Channel {i+1}')
            axs[i].set_ylabel('Amplitude')

        # Set a common x-axis label
        plt.xlabel(f'File {file_number}')

        # Adjust layout to prevent overlap
        plt.tight_layout()
        
        # Save the figure
        output_path = f"labs/img/data/NewFile{file_number}aa.png"
        plt.savefig(output_path)
        plt.close(fig)  # Close the figure to free memory

        print(f"Saved plot for NewFile{file_number} as {output_path}")

    except FileNotFoundError:
        print(f"File NewFile{file_number}.csv not found, skipping.")

"""длина 6.7 см
диаметр 2.4
паразитный длина 2.3

холодный
длина 3.9
диаметр 2.4"""


