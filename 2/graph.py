import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

for file_number in range(1, 4):
    # Set up path
    csv_file_path = f"2/csv/{file_number}.csv"
    df = pd.read_csv(csv_file_path, sep="\t", header=None)

    # Change row number
    row = 210

    # Get desired row
    row_data = df.iloc[80, 1:] + 273.15  # Extract the 250th row excluding the first column and add 273


    # Generate x and multiply by the mean distance between sensors (cm)
    x = np.array(range(1, len(row_data) + 1)) * 0.011

    # Perform linear fit (degree=1)
    coefficients = np.polyfit(x, row_data, 1)
    slope, intercept = coefficients
    print(f"Linear Fit for File {file_number}: Slope = {slope}, Intercept = {intercept}")
    ws = [1.407 , 3.751 , 5.684]
    # Generate y values for the linear fit
    y_fit = slope * x + intercept
    print(ws[file_number - 1] / (2.4e-5 * 3 * slope))
    print(ws[file_number - 1]/(slope*238))
    # Plot
    plt.style.use("seaborn-v0_8")
    matplotlib.rcParams.update({'font.size': 30})
    plt.figure(figsize=(6, 4))
    plt.plot(x, row_data, label='Данные', marker='o')
    plt.plot(x, y_fit, label=f'Линейное приближение (y={slope:.2f}x + {intercept:.2f})', linestyle='--', color='red')
    plt.xlabel('Длина, м')
    plt.ylabel('Температура, К')
    plt.title(f'Измерение {file_number}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'2/img/{file_number}.png')
    plt.show()
    plt.close()
