import matplotlib.pyplot as plt
import numpy as np

# Data from the image
ids_enabled = ["1 IDS-enabled", "2 IDS-enabled", "3 IDS-enabled", "4 IDS-enabled", "5 IDS-enabled"]
cpu_without_lb = [80, 75, 70, 65, 60]
cpu_random_lb = [70, 65, 60, 55, 50]
cpu_round_robin_lb = [65, 60, 55, 50, 45]
cpu_sura_lb = [60, 55, 50, 45, 40]

# Data for Coefficient Variation of CPU
cv_cpu_random_lb = 31.2
cv_cpu_round_robin_lb = 32.2
cv_cpu_sura_lb = 5.6

# Plot for CPU Comparison under Different LB Strategies
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
bar_width = 0.2
index = np.arange(len(ids_enabled))

plt.bar(index, cpu_without_lb, bar_width, label="Without LB", color="blue")
plt.bar(index + bar_width, cpu_random_lb, bar_width, label="Random LB", color="orange")
plt.bar(index + 2 * bar_width, cpu_round_robin_lb, bar_width, label="Round Robin LB", color="purple")
plt.bar(index + 3 * bar_width, cpu_sura_lb, bar_width, label=r"$S_{URA}$ LB", color="yellow")

plt.xlabel("IDS-enabled")
plt.ylabel("CPU [%]")
plt.title("CPU comparison under different LB strategies")
plt.xticks(index + 1.5 * bar_width, ids_enabled)
plt.legend()

# Plot for Coefficient Variation of CPU
plt.subplot(2, 2, 2)
cv_labels = ["Random LB", "Round Robin LB", r"$S_{URA}$ LB"]
cv_values = [cv_cpu_random_lb, cv_cpu_round_robin_lb, cv_cpu_sura_lb]

plt.bar(cv_labels, cv_values, color="blue")
plt.ylabel("Coefficient variation [%]")
plt.title("Coefficient variation of CPU")
for i, v in enumerate(cv_values):
    plt.text(i, v + 1, f"{v}%", ha="center")

# Data for Battery Autonomy Comparison (Example values)
battery_without_lb = [25, 23, 22, 21, 20]
battery_random_lb = [24, 22, 20, 18, 16]
battery_round_robin_lb = [23, 21, 19, 17, 15]
battery_sura_lb = [22, 20, 18, 16, 14]

# Plot for Battery Autonomy Comparison
plt.subplot(2, 2, 3)
plt.bar(index, battery_without_lb, bar_width, label="Without LB", color="blue")
plt.bar(index + bar_width, battery_random_lb, bar_width, label="Random LB", color="orange")
plt.bar(index + 2 * bar_width, battery_round_robin_lb, bar_width, label="Round Robin LB", color="purple")
plt.bar(index + 3 * bar_width, battery_sura_lb, bar_width, label=r"$S_{URA}$ LB", color="yellow")

plt.xlabel("IDS-enabled")
plt.ylabel("Battery Autonomy [min]")
plt.title("Battery autonomy comparison under different LB strategies")
plt.xticks(index + 1.5 * bar_width, ids_enabled)
plt.legend()

# Data for Coefficient Variation of Battery Autonomy (Example values)
cv_battery_random_lb = 12.3
cv_battery_round_robin_lb = 15.4
cv_battery_sura_lb = 5.1

# Plot for Coefficient Variation of Battery Autonomy
plt.subplot(2, 2, 4)
cv_battery_labels = ["Random LB", "Round Robin LB", r"$S_{URA}$ LB"]
cv_battery_values = [cv_battery_random_lb, cv_battery_round_robin_lb, cv_battery_sura_lb]

plt.bar(cv_battery_labels, cv_battery_values, color="blue")
plt.ylabel("Coefficient variation [%]")
plt.title("Coefficient variation of battery autonomy")
for i, v in enumerate(cv_battery_values):
    plt.text(i, v + 0.5, f"{v}%", ha="center")

# Display plots
plt.tight_layout()
plt.show()