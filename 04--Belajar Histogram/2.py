import numpy as np
import matplotlib.pyplot  as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10_000)

fix, ax = plt.subplots()
ax.hist(x,
		bins = 50,
		facecolor = 'r',
		alpha = 0.75
		)
ax.set(xlabel = 'Sumbu X',
       ylabel = 'Sumbu Y',
       title = 'Contoh Histogram'
	   )

plt.grid()
plt.show()
