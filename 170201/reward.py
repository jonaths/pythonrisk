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

		# print "reward"
		# print s
		# print a
		# print sprime

		x = sprime[0]
		y = sprime[1]

		r = -0.0

		# if(x > 4):
		# 	r = -10
		# if(x < -4):
		# 	r = -10
		# if(y > 4):
		# 	r = -10
		# if(y < -4):
		# 	r = -10			

		# hole = [-2,0]
		# distance_to_hole = euclid(np.asarray(hole),np.asarray(sprime))

		# if distance_to_hole < 1:
		# 	r = (x-(-2))**2.0 + (y+0.0)**2.0 - 2

		hill = [0,0]
		distance_to_hill = euclid(np.asarray(hill),np.asarray(sprime))

		if distance_to_hill < 2**(1/2):
			r = - (x - 0.0)**2.0 - (y + 0.0)**2.0 + 1


		self.saveSample(s,a,sprime,r)
		return r - a[0]