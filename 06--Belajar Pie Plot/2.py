# Pengaturan Legend Dan Color
import matplotlib.pyplot as plt

kategori = ['A', 'B', 'C', 'D', 'E']
data = [215, 130, 245, 210, 255]
warna = ['pink', 'cyan', '#e03364', 'yellowgreen', 'skyblue']

plt.pie(data,
        labels = kategori,
        colors = warna,
        autopct = '%1.1f%%',
        startangle = 90
        )
plt.legend()
plt.title('Pengaturan legend dan color')
plt.show()
