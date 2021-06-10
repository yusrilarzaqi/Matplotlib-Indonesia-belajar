# simple pie plot
import matplotlib.pyplot as plt

kategori = ['A', 'B', 'C', 'D', 'E']
data = [215, 130, 245, 210, 255]

plt.pie(data,
        labels = kategori,
        autopct = '%1.1f%%',
        startangle = 90
        )
plt.title('Contoh Pie Plot Sederhana')
plt.show()

