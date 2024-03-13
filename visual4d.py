import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from main_easy import utility

# Vectorize the utility function
utility_vec = np.vectorize(utility)

# Generate data
x = np.linspace(1, 100, 20)  # Adjust the number of points if necessary
y = np.linspace(1, 100, 20)  # Adjust the number of points if necessary
z = np.linspace(0, 2, 20)  # Adjust the number of points if necessary

# Create a 3D grid
X, Y, Z = np.meshgrid(x, y, z)

# Calculate utility for each point in the grid
U = utility_vec(X, Y, Z)

# Create a color map based on the utility values
colors = plt.cm.viridis(U.flatten() / np.max(U))

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(X, Y, Z, c=U.flatten(), cmap=plt.cm.viridis, vmin=np.min(U), vmax=np.max(U))

# Add a color bar
fig.colorbar(sc)

# Add labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()