#!/usr/bin/python

import sys

class RiskMapper:

	def __init__(self):
		self.riskmap = []


	@staticmethod	
	def getMap(state):

		# Hacer esto bien. Las minas las deberia recibir del constructor
		# y el constructor se deberia de generar en el programa principal para
		# poder almacenar el mapa. 

		mineReward = 20

		b = state[0]
		x = state[1]
		y = state[2]

		mines = [[5,0],[5,5],[5,13]]
		for m in mines:
			if RiskMapper.manhattan_distance(m,[x,y]) == 1:
				return mineReward / 2
			if RiskMapper.manhattan_distance(m,[x,y]) == 2:
				return mineReward / 4

		return 0

	@staticmethod		
	def manhattan_distance(start, end):
	    sx, sy = start
	    ex, ey = end
	    return abs(ex - sx) + abs(ey - sy)
			




