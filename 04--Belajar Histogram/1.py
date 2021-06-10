import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10_00)
print(x)
print(x.shape)

plt.hist(x,
         bins=50,
         facecolor='g',
         alpha=0.75)

plt.xlabel('Sudut X')
plt.ylabel('Sudut Y')
plt.title('Contoh Histogram')
plt.text(45, 500, r'$\mu=100,\ \sigma=15$')
plt.grid()
plt.show()
