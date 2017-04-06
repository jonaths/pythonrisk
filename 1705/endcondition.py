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

		print stateprime

		bprime = stateprime[0]
		xprime = stateprime[1]
		yprime = stateprime[2]

		if bprime == 0:
			return True

		if(xprime == 3 and yprime == 0):
			return True

		if(xprime == 7 and yprime == 0):
			return True	

		if(xprime == 11 and yprime == 0):
			return True	
			
		if(xprime == 15 and yprime == 0):
			return True			
	
		return False

	