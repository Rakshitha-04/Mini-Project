class IDS:
    def __init__(self):
        self.suspicious_patterns = [
            "DDOS",
            "Packet flooding",
            "Malicious routing"
        ]
        self.alerts = []

    def detect_intrusion(self, traffic_data):
        """Detect suspicious patterns in the given traffic data."""
        for pattern in self.suspicious_patterns:
            if pattern in traffic_data:
                self.alerts.append(f"Alert: {pattern} detected!")
                print(f"Intrusion Detected: {pattern}")

    def get_alerts(self):
        return self.alerts


# Simulate some traffic
traffic_data = [
    "Normal traffic",
    "DDOS attack detected",
    "Packet flooding occurred",
    "Normal routing"
]

# IDS monitor simulation
ids = IDS()
for traffic in traffic_data:
    ids.detect_intrusion(traffic)

print("\nIDS Alerts:", ids.get_alerts())
