import matplotlib.pyplot as plt
import numpy as np

#Data Sample
np.random.seed(2)
data = np.random.normal(loc=100,scale=10, size=100)

#Box Plot
plt.boxplot(data, labels=['data'])
plt.title('Contoeh Box Plot')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.grid()
plt.show()
