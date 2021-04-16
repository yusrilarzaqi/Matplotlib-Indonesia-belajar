import matplotlib.pyplot as plt
import numpy as np

# Simple Line Plot
x = np.arange(0.,2.,0.01)
s = np.sin(2 * np.pi * x)

fig, ax = plt.subplots()
ax.plot(x, s, 'r-')
ax.set(xlabel='Nilai $x$',
       ylabel='nilai $sin(x)$',
       title='Visualisasi Nilai $sin$')
ax.grid()
plt.show()
