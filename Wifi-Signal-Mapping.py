import matplotlib.pyplot as plt

locations = ["Hall(entrence)", "Hall(Other End)", "Kitchen", "Bedroom - 1", "Bedroom - 2"]
signal_strength = [-53, -46, -60, -55, -70]

plt.figure(figsize=(8,5))
plt.bar(locations, signal_strength, color=['blue','red','green','purple','orange'])
plt.xlabel("Locations")
plt.ylabel("Signal Strength (dBm)")
plt.title("Wi-Fi Signal Strength at Different Locations")
plt.show()
