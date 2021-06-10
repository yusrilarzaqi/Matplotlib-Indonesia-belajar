import matplotlib.pyplot as plt
import numpy as np

# Sample Data
n = np.linspace(-3, 3, 100)
x, y = np.meshgrid(n, n)
z = np.sqrt(x**2 + y**2)

# Contoh contour plot
plt.contourf(x, y, z)
plt.colorbar()
plt.title("Contoh Filled Contour Plot")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
#plt.zlabel("Sumbu Z")

plt.show()
