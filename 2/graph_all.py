import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

for file_number in range(1, 4):
    # Set up path
    csv_file_path = f"2/csv/{file_number}.csv"
    df = pd.read_csv(csv_file_path, sep="\t", header=None)
    plt.style.use("seaborn-v0_8")
    plt.figure(figsize=(6, 4)) 
    x = df[0]  # Use the 0th column as x
    for col in df.columns[1:]:
        y = df[col] + 273.15  # Use the current column as y
        plt.plot(x, y, label=f"{col}")
    plt.legend(facecolor='white', framealpha=0.6, frameon=1)
    plt.show()
    plt.close()   