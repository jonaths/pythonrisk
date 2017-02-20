#!/usr/bin/python

from math import sin,cos

class Meshgrid:

	def __init__(self):
		# x va desde 0 hasta 1
		self.xmax = 10
		# y va desde 0 hasta 1
		self.ymax = 10
		# posicion inicial 0,0
		self.x = 0
		self.y = 0
		self.azimuthmax = 360
		self.rmax = 1

	def move(self,x,y,azimuth,r):

		if(x >= self.xmax):
			return False
		if(y >= self.ymax):
			return False	

		if(azimuth >= self.azimuthmax):
			return False
		if(r > self.rmax):
			return False

		newx = x + cos(azimuth) * r
		newy = y + sin(azimuth) * r

		if(newx >= self.xmax):
			return False
		if(newy >= self.ymax):
			return False

		return [newx,newy]
		





