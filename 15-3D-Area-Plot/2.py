import matplotlib.pyplot as plt
import numpy as np

# Sample Data
n = np.linspace(-3., 3., 100)
x, y = np.meshgrid(n, n)
z = np.sqrt(x**2 + y**2)

# 3D Surface Plot
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z, cmap='viridis')
ax.set_title('3D Suface Plot')

plt.show()
