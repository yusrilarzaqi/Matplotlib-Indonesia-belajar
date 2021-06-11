import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Sample Data
data = {
  'Item A' : 109438,
  'Item B' : 109472,
  'Item C' : 109438,
  'Item D' : 16838,
  'Item E' : 986438,
  'Item F' : 809438,
  'Item G' : 154438,
  'Item H' : 109860,
  'Item I' : 187438,
  'Item J' : 105438,}
item = tuple(data.keys())
count= tuple(data.values())

# Pengaturan Style
plt.style.use('seaborn')

# Pengaturan Format pada Ticker
def ribuan(x, pos):
    return f'{int(x/1000)}K'
formatter = FuncFormatter(ribuan)
ax.xaxis.set_major_formatter(formatter)

# Simple Plot
fig, ax = plt.subplots()
ax.barh(item, count)

plt.show()
