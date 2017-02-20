import numpy as np

class QLearning:	

	def __init__(self,alpha,gamma):
		self.alpha = 0.1
		self.gamma = 0.1
		

	def setZeros(self,num_states,num_actions):
		"""Crea una matriz de cros
		
		[description]
		
		Arguments:
			num_states {int} -- el numero de estados (filas)
			num_actions {int} -- el numero de acciones (columnas)
		
		Returns:
			[numpy] -- tabla Q
		"""
		self.Q = np.zeros(shape=(num_states,num_actions))
		return self.Q		

	def getQ(self):
		return self.Q 	

	def setQ(self,newQ):
		self.Q = newQ
		return self.newQ	

