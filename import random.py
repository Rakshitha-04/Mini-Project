import random
import math

class UAV:
    def __init__(self, uav_id, x, y, battery=100, processing_power=100):
        self.uav_id = uav_id
        self.x = x
        self.y = y
        self.battery = battery
        self.processing_power = processing_power

    def move(self):
        """Simulate UAV movement by updating its coordinates."""
        self.x += random.uniform(-1, 1)
        self.y += random.uniform(-1, 1)
        self.battery -= 0.1  # Battery consumption as the UAV moves

    def __str__(self):
        return f"UAV-{self.uav_id} [x: {self.x:.2f}, y: {self.y:.2f}, Battery: {self.battery:.2f}]"


class FANET:
    def __init__(self, num_uavs):
        self.uavs = [UAV(i, random.uniform(0, 10), random.uniform(0, 10)) for i in range(num_uavs)]

    def get_nearby_uavs(self, uav, max_distance=2):
        """Return a list of nearby UAVs for load balancing and resource allocation."""
        nearby_uavs = []
        for other_uav in self.uavs:
            if other_uav != uav:
                distance = math.sqrt((uav.x - other_uav.x) ** 2 + (uav.y - other_uav.y) ** 2)
                if distance <= max_distance:
                    nearby_uavs.append(other_uav)
        return nearby_uavs

    def simulate(self):
        """Simulate the movement and resource usage of all UAVs."""
        for uav in self.uavs:
            uav.move()
            print(uav)


# Example of FANET with 5 UAVs
fanet = FANET(num_uavs=5)

# Run a simulation
for _ in range(5):
    fanet.simulate()
    print()
