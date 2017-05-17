import numpy as np
import random
import sys

class QLearning:	

	def __init__(self,alpha,gamma,epsilon):
		self.alpha = alpha
		self.gamma = gamma
		self.epsilon = epsilon
		# Un array con una entrada por cada actualizacion de Q
		# [[s,a,sprime,r],[s,a,sprime,r],...]
		self.history = []
				

	def setValues(self,num_states,num_actions,value):
		"""Crea una matriz de cros
		
		[description]
		
		Arguments:
			num_states {int} -- el numero de estados (filas)
			num_actions {int} -- el numero de acciones (columnas)
		
		Returns:
			[numpy] -- tabla Q
		"""
		self.Q = np.empty(shape=(num_states,num_actions))
		self.Q.fill(np.nan)
		return self.Q		

	def getQ(self):
		return self.Q 	

	def setQ(self,newQ):
		self.Q = newQ
		return self.newQ	

	def setEpsilon(self,epsilon):
		self.epsilon = epsilon	

	def getEpsilon(self):
		return self.epsilon	

	def updateQ(self, r, state, next_state, action):

		qsa = self.Q[state][action]

		if(np.isnan(qsa)):
			new_q = r
		else:
			rsa = r
			new_q = qsa + self.alpha * (rsa + self.gamma * np.nanmax(self.Q[next_state, :]) - qsa)
				
		self.Q[state, action] = new_q
		self.history.append([state,action,next_state,r])
		return new_q

	def getAccumulatedReward(self):
		acc_reward = 0
		for h in self.history:
			acc_reward += h[3]
		return acc_reward	

	def clearHistory(self):
		print "clearint q history..."
		print "history",self.history;
		print "accumulated reward:",self.getAccumulatedReward()
		self.history = []    

	def getAction(self,state):

		# Probabilidad de escoger una accion aleatoria
		prob = random.random()

		# Si epsilon = 1 siempre elige una aleatoria
		# Si epsilon = 0 nunca elige una aleatoria
		if(prob < self.epsilon):
			print "action random"
			num_states = np.asarray(self.Q).shape[1]
			action = random.randint(0,num_states-1)
		else:	
			action = np.nanargmax(self.Q[state])
			print "action max " + str(action) + " " + str(self.Q[state])

		return action   

	def getMaxVal(self):

		max = []
		for r in self.Q:
			max.append(np.amax(r))
		return max

	def getAvgVal(self):

		avg = []
		for r in self.Q:
			avg.append(np.average(r))
		return avg	

	# def reMapQ(states,statesprime):
	# 	aqui voy... funcion para remapear Q	 

