#!/usr/bin/python

from math import sin,cos,exp
from gla import euclid
import numpy as np
import json
from riskmapper import RiskMapper
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import sys

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

		b = sprime[0]
		x = sprime[1]
		y = sprime[2]

		reward = -1		

		if x==4 and y == 0:
			reward = 10

		# if x==5 and y==0:
		# 	reward = -20
		# elif x==5 and y==5:
		# 	reward = -20
		# elif x==5 and y==13:
		# 	reward = -20

		# elif x==10 and y==0:
		# 	reward = 10
		# elif x==14 and y==0:
		# 	reward = 22
		# elif x==18 and y==0:
		# 	reward = 34

		if b == 0:
			reward = reward - 20	
		
		return reward