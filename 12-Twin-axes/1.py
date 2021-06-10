import matplotlib.pyplot as plt
import numpy as np

# Kasus 1
x = np.linspace(1, 10, 25)

fig, ax1 = plt.subplots()
ax1.plot(x, np.exp(x), 'gs-', label='Exp')
ax1.set_xlabel("Sumbu X")
ax1.set_ylabel("Exp")

ax2=ax1.twinx()
ax2.plot(x, np.log(x), 'ro-',label='Log')
ax1.set_ylabel("Exp")

fig.suptitle("Contoh Twin Axes")
fig.legend(loc='upper left')
plt.show()
