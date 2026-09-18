import numpy as np
import matplotlib.pyplot as plt

# Initial conditions
v0 = 25.0                 # m/s
theta = np.radians(45)    # launch angle
g = 9.81                  # m/s^2

# Flight time
T = 2 * v0 * np.sin(theta) / g
t = np.linspace(0, T, 200)

# Trajectory
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

# Plot
plt.plot(x, y)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Projectile Motion")
plt.grid()

plt.savefig("trajectory_name.png", dpi=150)

print("Simulation complete! <name>")
print("Created trajectory_name.png")
