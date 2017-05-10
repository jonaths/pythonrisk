#!/usr/bin/python

from math import sin,cos

class GridWorld:

	def __init__(self, xlim, ylim):
		self.xlim = xlim
		self.ylim = ylim
		self.getStates()

	def getStates(self):
		self.states = []
		for x in range(self.xlim):
			for y in range(self.ylim):
				self.states.append([x,y])	
		return self.states		

	def getActions(self):
		# 0: arriba
		# 1: abajo
		# 2: derecha
		# 3: izquierda
		self.actions = [[0,1],[0,-1],[1,0],[-1,0]]	
		return self.actions
		

	def move(self,state,action):
		"""Meve al agente
		
		Mueve al agente en funcion de la accion y regresa la posicion siguiente
		
		Arguments:
			state {[type]} -- Un par [x,y]
			action {[type]} -- Una accion [pasos en x, pasos en y]
		"""

		newx = state[0] + action[0]
		newy = state[1] + action[1]

		invalid = False

		if( newx < 0 ):
			invalid = True
		if( newx > self.xlim ):
			invalid = True
		if( newy < 0 ):
			invalid = True
		if( newy > self.ylim):
			invalid = True

		if(invalid):
			newx = state[0]
			newy = state[1]
		
		return [newx,newy]
		





