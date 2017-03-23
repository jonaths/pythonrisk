import matplotlib.pyplot as plt
import numpy as np

def plotheatmap(x,y,intensity,filename='heatmap.png'):



	#setup the 2D grid with Numpy
	x, y = np.meshgrid(x, y)

	#convert intensity (list of lists) to a numpy array for plotting
	intensity = np.array(intensity)

	fig, ax = plt.subplots()
	# Using matshow here just because it sets the ticks up nicely. imshow is faster.
	ax.matshow(intensity, cmap='Greens')
	ax.invert_yaxis()

	for (i, j), z in np.ndenumerate(intensity):
	    ax.text(j, i, '{:0.4f}'.format(z), ha='center', va='center', fontsize=5, bbox=dict(boxstyle='round', facecolor='white', edgecolor='0.3'))

	# #now just plug the data into pcolormesh, it's that easy!
	# plt.pcolormesh(x, y, intensity)
	# plt.colorbar() #need a colorbar to show the intensity scale

	plt.savefig('Figures/'+filename)