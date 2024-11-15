import matplotlib.pyplot as plt
# Data extracted from the tables for each resistor value

# Data for R = 470 Ω
voltages_470 = [1, 2, 3, 4, 5, 6, 7, 8]
currents_470 = [2.40, 4.23, 6.24, 8.67, 10.83, 13.02, 15.26, 17.40]

# Data for R = 2.2 kΩ
voltages_2_2k = [1, 2, 3, 4, 5, 6, 7, 8]
currents_2_2k = [0.38, 0.85, 1.32, 1.76, 2.20, 2.67, 3.13, 3.61]

# Data for R = 10 kΩ
voltages_10k = [1, 2, 3, 4, 5, 6, 7, 8]
currents_10k = [0.04, 0.14, 0.23, 0.34, 0.43, 0.56, 0.64, 0.75]

# Plotting the graphs
plt.figure(figsize=(14, 10))

# Plot for R = 470 Ω
plt.subplot(3, 1, 1)
plt.plot(currents_470, voltages_470, marker='o', color='blue', linestyle='-', linewidth=1.5)
plt.title("Voltage (V) vs Current (I) for R = 470 Ω")
plt.xlabel("Current (mA)")
plt.ylabel("Voltage (V)")
plt.grid(True)

# Plot for R = 2.2 kΩ
plt.subplot(3, 1, 2)
plt.plot(currents_2_2k, voltages_2_2k, marker='o', color='green', linestyle='-', linewidth=1.5)
plt.title("Voltage (V) vs Current (I) for R = 2.2 kΩ")
plt.xlabel("Current (mA)")
plt.ylabel("Voltage (V)")
plt.grid(True)

# Plot for R = 10 kΩ
plt.subplot(3, 1, 3)
plt.plot(currents_10k, voltages_10k, marker='o', color='red', linestyle='-', linewidth=1.5)
plt.title("Voltage (V) vs Current (I) for R = 10 kΩ")
plt.xlabel("Current (mA)")
plt.ylabel("Voltage (V)")
plt.grid(True)

# Adjust layout to avoid overlap
plt.tight_layout()
plt.show()

