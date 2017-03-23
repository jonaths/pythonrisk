import numpy as np
import random

class QLearning:	

	def __init__(self,alpha,gamma,epsilon):
		self.alpha = alpha
		self.gamma = gamma
		self.epsilon = epsilon
		

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

	def setEpsilon(epsilon):
		this.epsilon = epsilon	

	def updateQ(self, r, state, next_state, action):
	    rsa = r
	    qsa = self.Q[state][action]
	    new_q = qsa + self.alpha * (rsa + self.gamma * max(self.Q[next_state, :]) - qsa)
	    self.Q[state, action] = new_q
	    # renormalize row to be between 0 and 1
	    # rn = q[state][q[state] > 0] / np.sum(q[state][q[state] > 0])
	    # q[state][q[state] > 0] = rn
	    return self.Q

	def getAction(self,state):

		# Probabilidad de escoger una accion aleatoria
		prob = random.random()

		# Si epsilon = 1 siempre elige una aleatoria
		# Si epsilon = 0 nunca elige una aleatoria
		if(prob < self.epsilon):
			print "action max"
			num_states = np.asarray(self.Q).shape[1]
			action = random.randint(0,num_states-1)
		else:	
			print "action random"
			action = np.argmax(self.Q[state])
		print action

		return action   

	def getMaxVal(self):

		max = []
		for r in self.Q:
			max.append(np.amax(r))
		return max

	# def reMapQ(states,statesprime):
	# 	aqui voy... funcion para remapear Q	 

