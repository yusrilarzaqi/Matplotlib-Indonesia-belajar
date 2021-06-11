import matplotlib.pyplot as plt
import numpy as np

#Sample Data
np.random.seed(2)
data = np.random.normal(loc=100, size=100, scale=10)

#notched Box Plot
plt.boxplot(data, labels=['data'], notch=True)
plt.title('Contoh Notched Box plot')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.grid()
plt.show()
