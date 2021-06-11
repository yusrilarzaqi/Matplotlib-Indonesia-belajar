import matplotlib.pyplot as plt
import numpy as np 

# Sample Data 
n = np.linspace(-3., 3., 100)
x, y = np.meshgrid(n, n)
z = np.sqrt(x**2 + y**2)

# 3D WireFrame
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(x, y, z, color='orange')
ax.set(title='3D Wire Frame',
        xlabel='X',
        ylabel='Y',
        zlabel='Z'
        )
plt.show()
