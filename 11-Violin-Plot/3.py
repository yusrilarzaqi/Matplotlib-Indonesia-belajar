import matplotlib.pyplot as plt
import numpy as np

#Sample Data
np.random.seed(2)
data = np.random.normal(100, 10, 200)

#Simple Violin plot
# Pengaturan Horizontal violin plot
plt.violinplot(data, vert=False)
plt.title("Simple Violin Plot")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")

plt.show()

