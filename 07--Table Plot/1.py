# OO style 
import matplotlib.pyplot as plt

data_uas = [['Bejo', 70],
            ['Tejo', 83],
            ['Cecep', 62],
            ['Wati', 74],
            ['Karti', 71]
            ]

fig, ax = plt.subplots()
table = plt.table(cellText = data_uas, loc = 'center')
table.set_fontsize(14)
table.scale(.5, 2) # ukuran kolom, baris
ax.axis(False)
plt.title('OO Style')
plt.show()
