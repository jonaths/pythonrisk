from gla import generate_codebook,distances,point_inside_polygon
from voronoi import *
import random
from random import randrange
import numpy as np
from gridworld import GridWorld
from reward import Reward
from endcondition import EndCondition
from random import uniform
from qlearning import *
from tools import Tools
import json
from qlearning import *
from listheatmap import plotheatmap
from agentanalyzer import AgentAnalyzer
import sys

class Agent(object):	

	def __init__(self,states,actions):
		"""Inicializacion
		
		Crea un agente con modelo MDP
		
		Arguments:
			states {numpy array} -- Un array con los prototipos de cada estado. Ej: [[1,2],[4,5],[3,7]]
			actions {[type]} -- Un array con los prototipos de cada accion. 
		"""
		self.states = np.array(states)
		self.actions = np.array(actions)
		self.position_history = []
		self.action_history = []

	def setAgent(self,position):
		"""Define el estado actual del agente
		
		Define en cual de los prototipos de self.states esta el agente mediante s indice
		
		Arguments:
			state_index {int} -- El indice del agente.
		"""
		self.position = position
		self.position_history.append(position)
		self.currentstate  = np.argmin(distances(position,self.getStates()))
		return self.position

	def getStates(self):
		return self.states

	def getActions(self):
		return self.actions	

	def getCurrentState(self):
		return self.currentstate
		
	def getCurrentPosition(self):
		return self.position	

	def clearPositionHistory(self):
		self.position_history = []	

	def clearActionHistory(self):
		self.action_history = []					

	def setQLearning(self,alpha,gamma,epsilon):
		"""Inicializa el algoritmo Q Learning
		
		Arguments:
			alpha {[type]} -- [description]
			gamma {[type]} -- [description]
		"""
		self.qlearning = QLearning(alpha,gamma,epsilon)
		self.qlearning.setValues(self.states.shape[0],self.actions.shape[0],1)	

	def clearQHistory(self):
		self.qlearning.clearHistory()		

	def setEpsilon(self,epsilon):
		self.qlearning.setEpsilon(epsilon)	

	def getEpsilon(self):
		return self.qlearning.getEpsilon()	

	def updateQ(self, r, state, next_state, action):
		return self.qlearning.updateQ(r, state, next_state, action)

	def getQ(self):
		return self.qlearning.getQ()	

	def getAccumulatedReward(self):
		return self.qlearning.getAccumulatedReward();		

	def getMaxQValPerState(self):
		return self.qlearning.getMaxVal()	

	def getAvgQValPerState(self):
		return self.qlearning.getAvgVal()			

	def getAction(self,selection_policy):
		"""Selecciona una accion
		
		Selecciona una accion en funcion de una politica
		
		Arguments:
			selection_policy {string} -- el nombre de la politica
		
		Returns:
			[int] -- El id de la accion
		"""

		if selection_policy == 'random':
			action = self.getRandomAction()
		if selection_policy == 'qlearning':
			action = self.qlearning.getAction(self.currentstate)	
		else: 
			action = self.getRandomAction()

		# Para poder serializar y guardar en json	
		self.action_history.append(np.asarray(self.getActions()[action]).tolist())	
		
		return action	

	def getRandomAction(self):
		"""Selecciona una accion aleatoria
		
		Selecciona una accion aleatoria devolviendo el indice del arreglo de acciones
		
		Returns:
			[int] -- el indice de la accion
		"""
		action_index = randrange(0,len(self.actions))
		return action_index

	def getRandomActionValue(self):
		"""Recupera el valor de una accion aleatoria
		
		Recupera un par [x,y] de una accion
		
		Returns:|
			[type] -- [x,y]
		"""
		return self.actions[self.getRandomAction()]	

	def saveAgentHistoryToJson(self, filename = 'out.json'):
		print "Guardando informacion en " , filename
		dict = {}
		dict['action_history'] = self.action_history
		dict['position_history'] = self.position_history

		with open(filename, 'wb') as outfile:
			json.dump(dict, outfile)	

	def plotTrajectory(self,plotname = 'trajectory.png'):

		with open('out.json') as json_data:
			data = json.load(json_data)

		data = np.array(data['position_history'])
		# Lines on top of scatter
		plt.figure()

		# Scatter plot on top of lines
		plt.plot(data[:,0], data[:,1], 'r', zorder=1, lw=2)
		plt.scatter(data[:,0], data[:,1], s=60, zorder=2)
		plt.title('Dots on top of lines')

		plt.savefig('Figures/'+plotname)

		plt.clf()
		plt.cla()
		plt.close()							