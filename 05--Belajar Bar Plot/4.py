import matplotlib.pyplot as plt

data1 = [25, 85, 75, 40, 60]
data2 = [40, 35, 20, 55, 10]
kategori = ["A", "B", "C", "D", "E"]

# Stacked Bar Plot
plt.bar(kategori, data1, label = 'Data1')
plt.bar(kategori, data2, label = 'Data2', bottom = data1)
plt.legend()
plt.grid(linestyle='--',
         linewidth=1,
         axis='y',
         alpha=.75)

plt.xlabel('Katrgori')
plt.ylabel('Jumlah')
plt.title('Contoh Stacked Bar Plot')
plt.legend()
plt.show()


