# Pyplot style
import matplotlib.pyplot as plt

data_uas = [['Bejo', 70],
            ['Tejo', 83],
            ['Cecep', 62],
            ['Wati', 74],
            ['Karti', 71]
            ]

table = plt.table(cellText = data_uas, loc = 'center')
table.set_fontsize(14)
table.scale(1, 4)
ax = plt.gca()
ax.axis(False)

plt.show()

