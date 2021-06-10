import matplotlib.pyplot as plt
import numpy as np

data1 = [25, 85, 75, 40, 60]
data2 = [40, 35, 20, 55, 10]
kategori = ["A", "B", "C", "D", "E"]
x = np.arange(len(kategori))

# Grouped Bar Plot
width = .35

plt.bar(x-width/2, data1, width, label='Data1')
plt.bar(x+width/2, data2, width, label='Data2')

plt.xticks(x, kategori)
plt.grid(linestyle='--', linewidth=1, axis='y', alpha=.75)

plt.xlabel('Katrgori')
plt.ylabel('Jumlah')
plt.title('Contoh Grouped Bar Plot')
plt.legend()
plt.show()


