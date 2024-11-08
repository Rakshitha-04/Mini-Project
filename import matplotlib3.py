import matplotlib.pyplot as plt
import numpy as np

# Data for the first plot (CPU usage under different attack scenarios)
attackers = ['0 attackers', '2 attackers', '4 attackers', '6 attackers', '8 attackers', '10 attackers']
cpu_random_lb = [30, 38, 45, 48, 50, 52]
cpu_round_robin_lb = [30, 36, 42, 46, 49, 51]
cpu_sura_lb = [30, 35, 40, 44, 47, 49]

# Convert attackers to x-axis locations
x = np.arange(len(attackers))

# Plot settings
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot for CPU usage under attack
ax1.plot(x, cpu_random_lb, marker='o', linestyle='-', color='blue', label='Random LB')
ax1.plot(x, cpu_round_robin_lb, marker='o', linestyle='-', color='navy', label='Round Robin LB')
ax1.plot(x, cpu_sura_lb, marker='o', linestyle='-', color='black', label=r'$S_{URA}$ LB')

# Labels and formatting for the first plot
ax1.set_xlabel('Number of Attackers')
ax1.set_ylabel('CPU [%]')
ax1.set_title('CPU comparison - Under Attack')
ax1.set_xticks(x)
ax1.set_xticklabels(attackers)
ax1.legend()
ax1.grid(True)

# Data for the second plot (Coefficient variation of CPU usage)
lb_strategies = ['Random LB', 'Round Robin LB', r'$S_{URA}$ LB']
coefficient_variation_cpu = [27.0, 22.6, 12.4]

# Plot for Coefficient Variation of CPU
ax2.bar(lb_strategies, coefficient_variation_cpu, color='blue')
for i, v in enumerate(coefficient_variation_cpu):
    ax2.text(i, v + 1, f"{v}%", ha='center', color='black', fontweight='bold')

# Labels and formatting for the second plot
ax2.set_ylabel('Coefficient variation [%]')
ax2.set_title('Coefficient variation of CPU')

# Display plots
plt.tight_layout()
plt.show()
