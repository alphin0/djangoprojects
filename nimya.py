import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the differential equations
def model(y, t, k1, k2, k3):
    cA, cB, cC = y
    dcAdt = k2 * cB - k1 * cA
    dcBdt = k1 * cA - (k2 + k3) * cB
    dcCdt = k3 * cB
    return [dcAdt, dcBdt, dcCdt]

# Initial conditions
y0 = [1.0, 0.0, 0.0]  # cA=1, cB=0, cC=0

# Rate constants
k1 = 0.103
k2 = 0.0214
k3 = 0.0197

# Time points from 0 to 100
t = np.linspace(0, 100, 1000)

# Solve the ODEs
solution = odeint(model, y0, t, args=(k1, k2, k3))

# Extract concentrations
cA = solution[:, 0]
cB = solution[:, 1]
cC = solution[:, 2]

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, cA, label='$c_A$ (mmol/L)')
plt.plot(t, cB, label='$c_B$ (mmol/L)')
plt.plot(t, cC, label='$c_C$ (mmol/L)')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.title('Concentration vs. Time')
plt.legend()
plt.grid(True)
plt.show()