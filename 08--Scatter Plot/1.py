# simple data
import matplotlib.pyplot as plt
import numpy as np

x = [2, 4, 6, 8, 10, 11.5, 11.7]
y = np.arange(1, 5, .5)

plt.scatter(x, y,
           label = 'Data1',
           color = 'red'
           )
plt.xlabel('Submu X')
plt.ylabel('Submu Y')
plt.title('Contoh Scatter plot')
plt.show()

