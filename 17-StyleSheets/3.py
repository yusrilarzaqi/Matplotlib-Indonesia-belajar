import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'ro-')

with plt.style.use('dark_background'):
	plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'ro-')
	
plt.show()