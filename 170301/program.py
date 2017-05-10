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
	


	

print "Inicio..."

xlim = 16
ylim = 7
initial_position = [0,3]


gridworld = GridWorld(xlim,ylim)
states = np.asarray(gridworld.getStates())
actions = np.asarray(gridworld.getActions())


# Define al agente
agent = Agent(states,actions)
agent.setAgent(initial_position)

# alpha,gamma,epsilon
agent.setQLearning(0.1,0.8,1.0)

reward = Reward()
endcondition = EndCondition()

episodes = 5000
maxsteps = 40
end_counter = 0

log = {}
log['rewards'] = []
log['steps'] = []


for i in range(0,episodes):

	currentstate_index = agent.getCurrentState();

	print "Nuevo episodio " + str(i) + "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

	for j in range(0, maxsteps):

		print "Nueva iteracion " + str(j) + " ==========================================================="

		print "currentstate"
		currentstate = agent.getStates()[currentstate_index]
		currentposition = agent.getCurrentPosition()
		print currentstate_index, currentstate

		print "currentposition"
		print currentposition

		# Solo para debugear, si es true la condicion la decision se hara a mano
		if i > (episodes + 5):
			print "Q:"
			print agent.getQ()[currentstate_index]
			print "Accion recomendada:"
			print agent.getAction('qlearning')
			action_index = input('Accion: ')
			print "selected action_index:"
			print action_index
		else:
			action_index = agent.getAction('qlearning')	

		# action_index = agent.getAction('qlearning');	
		action = agent.getActions()[action_index]
		print "newaction"
		print action_index, action

		# Recupera el nuevo estado a traves de ejecutar una accion
		print "newposition"
		newposition = gridworld.move(agent.getCurrentPosition(),action)
		print newposition

		print "reward"
		current_reward = reward.reward(currentposition,action,newposition)
		print current_reward

		agent.setAgent(newposition)

		print "newstate"
		newstate_index = agent.getCurrentState()
		print newstate_index

		print "Q epsilon: " + str(agent.getEpsilon())

		print "newQ: " + str(agent.updateQ(current_reward, currentstate_index, newstate_index, action_index))

		# Verifica si debe terminar el episodio
		if endcondition.verify(currentposition,action,newposition,current_reward):
			print "endingposition: " + str(newposition)
			end_counter = end_counter + 1
			print "Ending ------------------------------------------------------------------"
			break

		# Determina el nuevo estado
		currentstate_index = newstate_index


	# Imprime la politica solo en el ultimo episodio
	if(i == episodes - 1):	
		print "printing trajectory"
		agent.saveAgentHistoryToJson()
		agent.plotTrajectory();

	# Si se cumple la condicion elimina la exploracion
	if end_counter > 30:
		agent.setEpsilon(0)	


	log['rewards'].append(agent.getAccumulatedReward())	
	log['steps'].append(j+1)

	agent.clearPositionHistory()
	agent.clearActionHistory()
	agent.clearQHistory()
	agent.setAgent(initial_position)


# Crea informacion para graficar mapa de politica	
intensity = np.zeros((xlim,ylim))
for i in range(len(agent.getStates())):
	# print str(agent.getStates()[i]) + str(agent.getMaxQValPerState()[i])
	intensity[agent.getStates()[i][0]][agent.getStates()[i][1]] = agent.getMaxQValPerState()[i]

x = range(xlim)
y = range(ylim)

# Imprime heatmap
plotheatmap(x,y,intensity.T)

print "Resultados Finales ########################################################"

# print "Q"
# print agent.getQ()
# print "Q[0]:"
# print agent.getQ()[0]
# print "Q[0][1]:"
# print agent.getQ()[0][1]
print "Q Num States:"
print len(agent.getQ())

print "end_counter:"
print str(end_counter) + "/" + str(episodes)

analysis = AgentAnalyzer(log)
analysis.plotRewardsAndSteps()
