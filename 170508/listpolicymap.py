import matplotlib.pyplot as plt
import numpy as np

def plotheatmap(x,y,intensity,policy,headers,filename='heatmap.png'):

	headers = headers[-4:]

	#setup the 2D grid with Numpy
	x, y = np.meshgrid(x, y)

	#convert intensity (list of lists) to a numpy array for plotting
	intensity = np.array(intensity)

	fig, ax = plt.subplots()
	# Using matshow here just because it sets the ticks up nicely. imshow is faster.
	ax.imshow(intensity, cmap='Greens')
	ax.invert_yaxis()

	for (i, j), z in np.ndenumerate(intensity):
		#print i,j,z,intensity[i][j],headers[int(policy[i][j])]
		#ax.text(j, i, '{:0.2f}'.format(z)+headers[int(policy[i][j])], ha='center', va='center', fontsize=5, bbox=dict(boxstyle='round', facecolor='white', edgecolor='0.3'))
		ax.text(j, i, '{:0.2f}'.format(z), ha='center', va='center', fontsize=6, bbox=dict(boxstyle='round', facecolor='white', edgecolor='0.3'))

	# #now just plug the data into pcolormesh, it's that easy!
	# plt.pcolormesh(x, y, intensity)
	# plt.colorbar() #need a colorbar to show the intensity scale

	plt.savefig('Figures/'+filename)
	plt.close()