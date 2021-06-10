# Pengaturan Marker
import matplotlib.pyplot as plt
import numpy as np

x1 = [2, 4, 6, 8, 10, 11.5, 11.7]
y1 = np.arange(1, 5, .5)

x2 = np.arange(8, 11.5, .5)
# [8, 8.5, 9, 9.5, 10, 10.5, 11]
y2 =[3, 3.5, 3.7, 4, 4.5, 5, 5.2]

plt.scatter(x1, y1,
  color='cayn',
  linewidth=1,
  marker='s',
  edgecolor='red',
  s = 100
)

plt.scatter(x2, y2,
  color='#82e6ff',
  linewidth=1,
  marker='^',
  edgecolor='black',
  s = 200
)
plt.show()
