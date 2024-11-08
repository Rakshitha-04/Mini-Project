import matplotlib.pyplot as plt
import numpy as np

# Data for the first plot (Packet Loss using different load balancing strategies)
ids_enabled = ['1 IDS-enabled', '2 IDS-enabled', '3 IDS-enabled', '4 IDS-enabled', '5 IDS-enabled']
packet_loss_without_lb = [0, 4.2, 3.4, 2.3, 1.6]
packet_loss_random_lb = [0, 3.5, 2.7, 1.8, 1.2]
packet_loss_round_robin_lb = [0, 3.2, 2.5, 1.7, 1.1]
packet_loss_sura_lb = [0, 2.8, 1.9, 1.4, 0.9]

x = np.arange(len(ids_enabled))  # the label locations
width = 0.2  # the width of the bars

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot for Packet Loss using different load balancing strategies
ax1.bar(x - 1.5*width, packet_loss_without_lb, width, label='Without LB', color='blue')
ax1.bar(x - 0.5*width, packet_loss_random_lb, width, label='Random LB', color='orange')
ax1.bar(x + 0.5*width, packet_loss_round_robin_lb, width, label='Round Robin LB', color='yellow')
ax1.bar(x + 1.5*width, packet_loss_sura_lb, width, label=r'$S_{URA}$ LB', color='purple')

# Labels and formatting for first plot
ax1.set_xlabel('Number of IDS-enabled')
ax1.set_ylabel('Packet Loss [%]')
ax1.set_title('Packet Loss using different load balancing strategies')
ax1.set_xticks(x)
ax1.set_xticklabels(ids_enabled)
ax1.legend()

# Data for the second plot (Coefficient variation of packet loss)
lb_strategies = ['Random LB', 'Round Robin LB', r'$S_{URA}$ LB']
coefficient_variation = [13.0, 12.0, 5.3]

# Plot for Coefficient Variation of Packet Loss
ax2.bar(lb_strategies, coefficient_variation, color='blue')
for i, v in enumerate(coefficient_variation):
    ax2.text(i, v + 0.5, f"{v}%", ha='center', color='black', fontweight='bold')

# Labels and formatting for second plot
ax2.set_ylabel('Coefficient variation [%]')
ax2.set_title('Coefficient variation of packet loss')

# Show plots
plt.tight_layout()
plt.show()
