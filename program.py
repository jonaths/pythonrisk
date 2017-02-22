from gla import generate_codebook,distances,point_inside_polygon
from voronoi import *
import random
from random import randrange
import numpy as np
from meshgrid import Meshgrid
from reward import Reward
from endcondition import EndCondition
from random import uniform
from qlearning import *
from tools import Tools
import json


class Agent:

	def __init__(self,states,actions):
		"""Inicializacion
		
		Crea un agente con modelo MDP
		
		Arguments:
			states {numpy array} -- Un array con los prototipos de cada estado. Ej: [[1,2],[4,5],[3,7]]
			actions {[type]} -- Un array con los prototipos de cada accion. 
		"""
		self.states = states
		self.actions = actions
		self.domain = Tools.getArrayMinMax(states)
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

	def getCurrentPosition(self):
		return self.position

	def getCurrentState(self):
		return self.currentstate	

	def getCurrentStateValue(self):
		return self.states[self.getCurrentState()]	

	def setQLearning(self,alpha,gamma):
		"""Inicializa el algoritmo Q Learning
		
		Arguments:
			alpha {[type]} -- [description]
			gamma {[type]} -- [description]
		"""
		self.qlearning = QLearning(alpha,gamma)
		self.qlearning.setZeros(self.states.shape[0],self.actions.shape[0])	

	def updateQ(self, r, state, next_state, action):
		return self.qlearning.updateQ(r, state, next_state, action)

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
		
		Returns:
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
			print(data)

		data = np.array(data['position_history'])
		# Lines on top of scatter
		plt.figure()

		# Scatter plot on top of lines
		plt.plot(data[:,0], data[:,1], 'r', zorder=1, lw=2)
		plt.scatter(data[:,0], data[:,1], s=60, zorder=2)
		plt.title('Dots on top of lines')

		plt.savefig('Figures/'+plotname)


			

	

print "Inicio..."

# Define estados iniciales

print "State Samples:"
state_samples = np.random.randint(-300,300,size=(100,2)) / 100.
print state_samples

sq,ap,sr = generate_codebook(state_samples,16,0.1);

print "State Centroids:"
states = np.asarray(sq)
print states

state_voronoi = VoronoiExtractor(states)
state_voronoi.plot('states.png')

# Define acciones iniciales

print "Action Samples:"
action_samples = np.random.randint(0,100,size=(100,2)) * 1.0
action_samples[:,0] *= 0.01 / 2
action_samples[:,1] *= 0.01 * 360
print action_samples

aq,ap,r = generate_codebook(action_samples,8,0.01);

print "Action Centroids:"
actions = np.asarray(aq)
print actions

action_voronoi = VoronoiExtractor(actions)
action_voronoi.plot('actions.png')

# Define al agente
agent = Agent(states,actions)
agent.setAgent([0,0])
agent.setQLearning(1,1)

# Crea el meshworld
meshworld = Meshgrid()
reward = Reward()
endcondition = EndCondition()

# Recupera el estado actual desde su indice
print "currentstate"
currentstate_index = agent.getCurrentState();

for x in range(0, 20):

	currentstate = agent.getStates()[currentstate_index]
	currentposition = agent.getCurrentPosition()
	print currentstate_index, currentstate

	print "currentposition"
	print currentposition

	# Recupera una accion aleatoria
	action_index = agent.getAction('random');
	action = agent.getActions()[action_index]
	print "newaction"
	print action_index, action

	# Recupera el nuevo estado a traves de ejecutar una accion
	print "newposition"
	newposition = meshworld.move(agent.getCurrentPosition(),action)
	print newposition

	print "reward"
	current_reward = reward.reward(currentposition,action,newposition)
	print current_reward

	agent.setAgent(newposition)

	print "newstate"
	newstate_index = agent.getCurrentState()
	print newstate_index

	print agent.updateQ(current_reward, currentstate_index, newstate_index, action_index)

	# Verifica si debe terminar el episodio
	if endcondition.verify(currentposition,action,newposition,current_reward):
		break

	# Determina el nuevo estado
	currentstate_index = newstate_index

	
agent.saveAgentHistoryToJson()
agent.plotTrajectory();



# distances = distances([0,0],np.asarray(sq))
# print distances
# print distances.argmin()

