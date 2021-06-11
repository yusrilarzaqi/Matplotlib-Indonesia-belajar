import matplotlib.pyplot as plt
import numpy as np

# Sample data 2x2
siswa = ['Yusril', 'Adam', 'Bimo', 'Dimas']
uas = [93, 71, 81, 64]

fig, ax = plt.subplots(ncols=2, nrows=2, constrained_layout=True)

ax[0][0].bar(siswa, uas)
ax[0][1].pie(uas, labels=siswa)
ax[1][0].pie(uas, labels=siswa, explode=[0, 0, 0, .5])
ax[1][1].barh(siswa, uas)

plt.show()

