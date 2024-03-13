import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from main_easy import utility
# Generate a mesh grid of x and y values (toast and wait durations)
x = np.arange(1, 101)  # Toast duration
y = np.arange(1, 101)  # Wait duration
X, Y = np.meshgrid(x, y)

# Calculate utility values for each point on the grid
Z = np.zeros_like(X)
for i in range(len(x)):
    for j in range(len(y)):
        Z[j, i] = utility(X[j, i], Y[j, i])  # Calculate Z value for each (x, y) pair

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis')
fig.colorbar(surf)

# Set labels and title
ax.set_xlabel('Toast Duration')
ax.set_ylabel('Wait Duration')
ax.set_zlabel('Utility')
ax.set_title('Utility Function Visualization')

# Show plot
plt.show()
