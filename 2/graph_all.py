import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

for file_number in range(1, 4):
    # Set up path
    csv_file_path = f"2/csv/{file_number}.csv"
    df = pd.read_csv(csv_file_path, sep="\t", header=None)
    plt.figure(figsize=(6, 4)) 
    for i in range (1, 15):
        plt.plot(df[1: i], df[0])
    plt.show()
    plt.close()   