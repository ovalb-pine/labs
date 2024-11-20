import pandas as pd
import matplotlib.pyplot as plt

# Load your data
# Assuming 'pressure_data.csv' contains columns 'Time', 'Pressure', and 'Volume'
# Replace this with your actual data file and column names
data = pd.read_csv("pressure_volume_data.csv")

# Plot p-V diagram
plt.figure(figsize=(8, 6))
plt.plot(data['Volume'], data['Pressure'], color='b', linewidth=2)
plt.title('p-V Diagram of the Stirling Engine Cycle')
plt.xlabel('Volume (m³)')
plt.ylabel('Pressure (Pa)')
plt.grid(True)
plt.show()
