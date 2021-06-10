import numpy as np
import matplotlib.pyplot as plt

data = [25, 45, 55, 125, 225]
kategori = ['A', 'B', 'C', 'D', 'E']

plt.bar(kategori, data)
plt.grid()
plt.xlabel('Katrgori')
plt.ylabel('Jumlah')
plt.title('Contoh Bar Plot')

plt.show()
