import numpy as np
import matplotlib.pyplot as plt

# Data points for pressure (P) and voltage (V)
pressure = np.array([0, 5, 15.5, 25, 28, 30]) * 98066.5 + 133.3 * 738  # in Pa
voltage = np.array([114, 118, 130, 140, 144, 146]) * 10**(-3)  # in V (no conversion to volts)

# Perform linear regression with the intercept fixed in mV
k, b = np.polyfit(pressure, voltage, 1)  # k is the slope, b is the intercept

print(f"Proportionality coefficient (k): {k} V per Pa")
print(f"Intercept (b): {b} V")

# Plotting
plt.plot(pressure, voltage, 'o', label="Data points")
plt.plot(pressure, k * pressure + b, label="Fit line")
plt.xlabel("Pressure (Pa)")
plt.ylabel("Voltage (mV)")
plt.legend()
plt.show()
