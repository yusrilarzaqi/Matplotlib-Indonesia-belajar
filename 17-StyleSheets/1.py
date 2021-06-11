import matplotlib.pyplot as plt
import numpy as np

plt.style.use('./style_ku.mplstyle')


# Sample Data
data = {
	'Item A' : 19438,
	'Item B' : 19352,
	'Item C' : 11641,
	'Item D' : 19414,
	'Item E' : 13219,
	'Item F' : 16518,
	'Item G' : 13161,
	'Item H' : 19641,
	'Item I' : 19196,
	'Item J' : 13512,
}
item = tuple(data.keys())
count = tuple(data.values())

# Simple Plot
fig, ax = plt.subplots()
ax.barh(item, count)

plt.show()
