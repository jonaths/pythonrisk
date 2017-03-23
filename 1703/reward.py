#!/usr/bin/python

from math import sin,cos,exp
from gla import euclid
import numpy as np
import json
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class Reward:
	
	def __init__(self):
		self.samples = []

	def saveSample(self,s,a,sprime,r):
		row = dict()
		row['s'] = s
		row['a'] = a
		row['sprime'] = sprime
		row['r'] = r		
		self.samples.append(row)

	def getSamples(self):
		return self.samples

	def saveToJson(self, filename = 'rewards.json'):
		print "Guardando informacion en " , filename
		with open(filename, 'wb') as outfile:
			json.dump(self.getSamples(), outfile)		

	def plotSprimeR2D(self,filename = 'reward.png'):
		"""Grafica la funcion de recompensa en un plano z = f(x,y)
		
		"""
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		matrix = np.array([]).reshape(0,3)
		for sample in self.samples:
			matrix = np.vstack([matrix, [sample['sprime'][0],sample['sprime'][1],sample['r']]])
			

		ax.scatter(matrix[:,0], matrix[:,1], matrix[:,2], c='r', marker='o')
		ax.set_xlabel('X Label')
		ax.set_ylabel('Y Label')
		ax.set_zlabel('Z Label')

		plt.show()
		plt.savefig('Figures/'+filename)


	def reward(self,s,a,sprime):

		x = sprime[0]
		y = sprime[1]

		reward = -1		

		if y == 6:
			reward = -6
		elif y == 5:
			reward = -4
		elif y == 4:
			reward = -2
		elif x==3 and y==0:
			reward = 6
		elif x==7 and y==0:
			reward = 11		
		
		return reward