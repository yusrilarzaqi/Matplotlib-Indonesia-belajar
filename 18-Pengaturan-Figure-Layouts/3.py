import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

# Sample data 2x2
siswa = ['Yusril', 'Adam', 'Bimo', 'Dimas']
uas = [93, 71, 81, 64]

fig = plt.figure(constrained_layout=True)

gs = gridspec.GridSpec(ncols=3, nrows=3, figure=fig)

ax1 = fig.add_subplot(gs[0, :])
ax1.set_title('ax1[0,:]')

ax2 = fig.add_subplot(gs[1, :-1])
ax2.set_title('ax2[1, :-1]')

ax3 = fig.add_subplot(gs[1:, -1])
ax3.set_title('ax3[1:, -1]')

ax4 = fig.add_subplot(gs[-1, 0])
ax4.set_title('ax4[-1, 0]')

ax5 = fig.add_subplot(gs[-1, -2])
ax5.set_title('ax5[-1, -2]')

plt.show()