import matplotlib.pyplot as plt
import numpy as np

# 3D Axes
fig = plt.figure()
ax = plt.axes(projection="3d")

# 3D Line Plot
z = np.linspace(0, 1, 100)
x = z * np.sin(20*2)
y = z * np.cos(20*2)

ax.plot(x, y, z, color="red")
ax.set(title='Contoh 3D Line Plot',
       xlabel='Sumbu X',
       ylabel='Sumbu Y',
       zlabel='Sumbu Z',
       )
plt.show()
