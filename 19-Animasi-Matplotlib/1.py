import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from IPython import display

## Khusus Jupyter nootbook
# Review Figure
fig = plt.figure()

plt.xlim(0, 4)
plt.ylim(-2, 2)

# Animasi
line = plt.plot([])[0]

def animated(i):
	x = np.linspace(0, 4, 1000)
	y = np.sin(2 * np.pi *(x-.1*i))
	line.set_data(x,y)
	return line

anim = FuncAnimation(fig, animated, frames=200, interval=20)
video = anim.to_html5_video()
html = display.HTML(video)

display.display(html)

plt.close()

