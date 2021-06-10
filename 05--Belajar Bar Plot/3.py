import matplotlib.pyplot as plt

data = [25, 45, 55, 125, 225]
kategori = ['A', 'B', 'C', 'D', 'E']

# Horizontal Bar Plot
# plt.barh(kategori, data)
plt.barh(kategori[::-1], data[::-1])

plt.grid(linestyle='--', linewidth=1, axis='x', alpha=.75)
plt.xlabel('Jumlah')
plt.ylabel('Kategori')
plt.title('Contoh Bar Plot')
plt.show()
