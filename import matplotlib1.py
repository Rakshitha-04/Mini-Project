import matplotlib.pyplot as plt
import numpy as np

# Data for CPU utilization and battery autonomy (from image)
load_balancers = ["Random LB", "Round Robin LB", "$S_{URA}$ LB"]
cpu_static = [42.1, 40.2, 35.2]
cpu_dynamic = [39.3, 37.4, 28.2]
battery_static = [12.5, 14.3, 17.3]
battery_dynamic = [15.9, 16.2, 20.2]

# Width for bars
bar_width = 0.35
index = np.arange(len(load_balancers))

# Plot for CPU Utilization
plt.figure(figsize=(12, 5))

# Subplot 1 - CPU Utilization Comparison
plt.subplot(1, 2, 1)
plt.bar(index, cpu_dynamic, bar_width, label="Dynamic", color="blue")
plt.bar(index + bar_width, cpu_static, bar_width, label="Static", color="orange")
plt.xlabel("Load Balancer")
plt.ylabel("CPU [%]")
plt.title("CPU Comparison under Static and Dynamic Deployment")
plt.xticks(index + bar_width / 2, load_balancers)
plt.legend()

# Subplot 2 - Battery Autonomy Comparison
plt.subplot(1, 2, 2)
plt.bar(index, battery_dynamic, bar_width, label="Dynamic", color="blue")
plt.bar(index + bar_width, battery_static, bar_width, label="Static", color="orange")
plt.xlabel("Load Balancer")
plt.ylabel("Time [min]")
plt.title("Battery Autonomy Comparison under Static and Dynamic Deployment")
plt.xticks(index + bar_width / 2, load_balancers)
plt.legend()

# Display plots
plt.tight_layout()
plt.show()