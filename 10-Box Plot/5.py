import matplotlib.pyplot as plt
import numpy as np

#Data Sample
np.random.seed(2)
data1 = np.random.normal(loc=100,scale=10, size=200)
data2 = np.random.normal(loc=80,scale=30, size=200)
data3 = np.random.normal(loc=90,scale=20, size=200)
data4 = np.random.normal(loc=70,scale=25, size=200)

data = [data1, data2, data3, data4]
label = ['Data 1', 'Data 2', 'Data 3', 'Data 4']

#Box Plot
plt.boxplot(data, labels=label)
plt.title('Contoh Multiple Box plot')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.grid()
plt.show()
