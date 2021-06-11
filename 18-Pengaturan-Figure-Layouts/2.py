import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

# Sample data 2x2
siswa = ['Yusril', 'Adam', 'Bimo', 'Dimas']
uas = [93, 71, 81, 64]

fig = plt.figure(constrained_layout=True)

gs = gridspec.GridSpec(ncols=2, nrows=2, figure=fig)

ax1 = fig.add_subplot(gs[0, :])
# ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])

ax1.bar(siswa, uas)
# ax2.pie(uas, labels=siswa)
ax3.pie(uas, labels=siswa, explode=[0, 0, 0, .2])
ax4.barh(siswa, uas)

plt.show()