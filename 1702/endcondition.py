#!/usr/bin/python

from math import sin,cos,exp
from gla import euclid
import numpy as np

class EndCondition:
	
	def __init__(self):
		self.counter = 0

	def getCounter(self):
		return self.counter	

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

		# print "verify"
		# print state,action,stateprime,reward

		# IMPORTANTE: asegurarse que la condicion de paro tenga alguna relacion con la funcion de recompensa en reward.py

		# hole = [0,2]
		goal = [0,0]

		# distance_to_hole = euclid(np.asarray(hole),np.asarray(stateprime))
		distance_to_goal = euclid(np.asarray(goal),np.asarray(stateprime))

		# if distance_to_hole < 0.5:
		# 	print "End hole: " , hole, distance_to_hole
		# 	return True

		if distance_to_goal < 0.5:
			print "End goal: " , goal, distance_to_goal , "###########################################################"
			self.counter = self.counter + 1
			return True	
	
		return False

	