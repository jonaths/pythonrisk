#!/usr/bin/python

from math import sin,cos,exp

class Reward:
	
	def __init__(self):
		self.default = 1

	def reward(self,s,a,sprime):
		x = sprime[0]
		y = sprime[1]
		return (1-(x**2+y**3))*exp(-(x**2+y**2)/2)