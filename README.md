# Wi-Fi Signal Strength Mapping

## Overview
This project analyzes Wi-Fi signal strength at different locations within a home using NetSpot. The collected data helps in optimizing router placement for better connectivity.

## Methodology
1. **Tool Used**: NetSpot (Free Version)
2. **Locations Tested**: Hall (two positions), Kitchen, Bedroom 1, and Bedroom 2.
3. **Process**:
   - Open NetSpot and scan available networks.
   - Walk to each location and record the signal strength in dBm.
   - Take screenshots of the signal readings for reference.
   - Analyze variations in signal strength.

## Data Collected
| Location         | Signal Strength (dBm)|
|------------------|----------------------|
| Hall (Entrence)  | -46                  |
| Hall (Other End) | -53                  |
| Kitchen          | -60                  |
| Bedroom 1        | -55                  |
| Bedroom 2        | -70                  |


## Signal Strength Visualization
![Hall (Entrence) Signal Strength](https://github.com/user-attachments/assets/eade7f44-4a13-448e-abb6-e949289af3fb)
![Hall (other-end) Signal strength](https://github.com/user-attachments/assets/b5592e34-5983-4202-9357-493c65667d87)
![Kitchen Signal Strength](https://github.com/user-attachments/assets/bc949fe2-dc40-4154-86ad-de20dfe76093)
![Bedroom-1 Singal Strength](https://github.com/user-attachments/assets/616c0e6f-819b-4aa9-9aff-97d0dd156cff)
![Bedroom-2 Signal Strength](https://github.com/user-attachments/assets/b8a5b010-34b1-40fd-8b33-95d3bab3f0c7)


### Graph Representation
```python
import matplotlib.pyplot as plt

locations = ["Hall (Entrence)",  "Hall (Other End)", "Kitchen", "Bedroom 1", "Bedroom 2"]
signal_strength = [-46,-53,-60,-55,-70]

plt.figure(figsize=(8,5))
plt.bar(locations, signal_strength, color=['blue', 'red', 'green', 'purple', 'orange'])
plt.xlabel("Locations")
plt.ylabel("Signal Strength (dBm)")
plt.title("Wi-Fi Signal Strength at Different Locations")
plt.show()
```

## Conclusion
- The best signal strength was found in the **Hall (Entrence) (-46 dBm)**.
- The weakest signal was in **Bedroom 2 (-70 dBm)**.
- Adjusting the router position towards the center may help in improving coverage.
