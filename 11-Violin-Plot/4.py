import matplotlib.pyplot as plt
import numpy as np

#Sample Data
np.random.seed(10)
data1 = np.random.normal(100, 10, 200)
data2 = np.random.normal(80, 30, 200)
data3 = np.random.normal(90, 20, 200)
data4 = np.random.normal(70, 25, 200)
data = [data1, data2, data3, data4]

#Simple Violin plot
#Multiple violin plot
plt.violinplot(data)
plt.title("Simple Violin Plot")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")

plt.show()
