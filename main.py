import numpy as np
import matplotlib.pyplot as plt


# Generate random temperature data (e.g., for 30 days)
# Mean temperature: 22°C, Standard deviation: 3°C
np.random.seed(42)
num_days = 30
temperatures = np.random.normal(loc=22, scale=3, size=num_days)


mean_temp = np.mean(temperatures)
min_temp = np.min(temperatures)
max_temp = np.max(temperatures)

#Print results
print(f"Average temperature is: {mean_temp:.2f}°C")
print(f"Minimum temperature is: {min_temp:.2f}°C")
print(f"Maximum temperature is: {max_temp:.2f}°C")

#Plot the temperature graph
days = np.arange(1, num_days+1)
plt.figure(figsize=[12, 8])
plt.plot(days, temperatures, marker='o', linestyle='-', color='blue', label=' Daily Temperature')
plt.axhline(mean_temp, color='pink', linestyle='--', label=' Average Temperature')
plt.title('30- Day Temperature')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()











