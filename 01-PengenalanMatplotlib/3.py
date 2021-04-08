import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0., 2., 100)
fig, ax = plt.subplots()
ax.plot(x, x, label='Linear') 
ax.plot(x, x**2, label='Quadratic')
ax.plot(x, x**3, label='Cubic')

# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_title('Simple Data')
ax.set(xlabel = 'x',
       ylabel = 'y',
       title = 'Simple Data')
ax.legend()
plt.show()

