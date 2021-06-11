import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(16, 40, size=30)

def C2F(celcius=0):
  return (celcius*1.8)+32
  
def konversi_sumbu(ax1):
  y1, y2 = ax1.get_ylim()
  ax2.set_ylim(C2F(y1), C2F(y2))
  ax2.figure.canvas.draw()
  
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.callbacks.connect('ylim_changed', konversi_sumbu)
ax1.plot(x)
ax1.set_xlabel('Hari')
ax1.set_ylabel("Celcius")
ax2.set_ylabel("Fahrenheit")

fig.suptitle("Temperatur Udara")

plt.show()


