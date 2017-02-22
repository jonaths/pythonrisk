#!/usr/bin/python

from math import sin,cos,exp
from gla import euclid
import numpy as np

class EndCondition:
	
	def __init__(self):
		self.default = 1

	def verify(self,state,action,stateprime,reward):
		"""Verifica si debe terminar o no
		
		Considera el estado actual del agente y determina si se cumple 
		alguna condicion de paro. 
		
		Arguments:
			state {[type]} -- el estado actual
			action {[type]} -- una accion
			stateprime {[type]} -- el siguiente estado despues de ejecutar una accion
			reward {[type]} -- si termina o no
		
		Returns:
			bool -- [description]
		"""

		print "verify"

		print state,action,stateprime,reward
		hole = [0,2]
		goal = [0,-1.5]

		distance_to_hole = euclid(np.asarray(hole),np.asarray(stateprime))
		distance_to_goal = euclid(np.asarray(goal),np.asarray(stateprime))

		print distance_to_hole
		print distance_to_goal

		if distance_to_hole < 0.5:
			print "End hole: " , hole, distance_to_hole
			return True

		if distance_to_goal < 0.5:
			print "End goal: " , hole, distance_to_goal
			return True	
	
		return False

	