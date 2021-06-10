# Exploded Pie Plot
import matplotlib.pyplot as plt

kategori = ['A', 'B', 'C', 'D', 'E']
data = [215, 130, 245, 210, 255]
my_exploded = [0., 0., .2, 0., .08]

plt.pie(data,
        labels = kategori,
        autopct = '%1.1f%%',
        startangle = 90,
        explode = my_exploded
        )
plt.title('Contoh Exploded Pie Plot')
plt.show()
