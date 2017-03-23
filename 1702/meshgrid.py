#!/usr/bin/python

from math import sin,cos

class Meshgrid:

	def __init__(self):
		# Setear limites de x y y
		self.xmax = 4.0
		self.xmin = -4.0
		self.ymax = 4.0
		self.ymin = -4.0

		# Setear limites de r y azimuth
		self.azimuthmax = 360.0
		self.azimuthmin = 0.0
		self.rmax = 1.0
		self.rmin = 0.0

		# posicion inicial 0,0
		self.x = 0
		self.y = 0
		

	def move(self,state,action):

		# print "move"
		# print state
		# print action

		x = state[0]
		y = state[1]

		r = action[0]
		azimuth = action[1]

		if(x >= self.xmax):
			raise ValueError("x >= self.xmax",x,self.xmax)
		if(x <= self.xmin):
			raise ValueError("x <= self.xmin",x,self.xmin)
		if(y >= self.ymax):
			raise ValueError("y >= self.ymax",y,self.ymax)
		if(y <= self.ymin):
			raise ValueError("y <= self.ymin",y,self.ymin)

		if(azimuth >= self.azimuthmax):
			raise ValueError("azimuth >= self.azimuthmax",azimuth,self.azimuthmax)
		if(azimuth < self.azimuthmin):
			raise ValueError("azimuth < self.azimuthmin",azimuth,self.azimuthmin)	
		if(r > self.rmax):
			raise ValueError("r > self.rmax",r,self.rmax)
		if(r < self.rmin):
			raise ValueError("r < self.rmin",r,self.rmin)	

		newx = x + cos(azimuth) * r
		newy = y + sin(azimuth) * r

		# if(newx >= self.xmax):
		# 	raise ValueError("newx >= self.xmax",newx,self.xmax)
		# if(newx <= self.xmin):
		# 	raise ValueError("newx <= self.xmin",newx,self.xmin)	
		# if(newy >= self.ymax):
		# 	raise ValueError("newy >= self.ymax",newy,self.ymax)
		# if(newy <= self.ymin):
		# 	raise ValueError("newy <= self.ymin",newy,self.ymin)	

		if(newx >= self.xmax):
			return [x,y]
		if(newx <= self.xmin):
			return [x,y]
		if(newy >= self.ymax):
			return [x,y]
		if(newy <= self.ymin):
			return [x,y]

		return [newx,newy]
		





