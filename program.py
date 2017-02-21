from gla import generate_codebook,distances,point_inside_polygon
from voronoi import *
import random
import numpy as np
from meshgrid import Meshgrid
from reward import Reward
from random import uniform
from qlearning import *
from tools import Tools

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

	def setState(self,state_index):
		"""Define el estado actual del agente
		
		Define en cuál de los prototipos de self.states está el agente mediante s índice
		
		Arguments:
			state_index {int} -- El índice del agente.
		"""
		self.currentstate = state_index	

	def setQLearning(self,alpha,gamma):
		self.qlearning = QLearning(alpha,gamma)
		self.qlearning.setZeros(self.states.shape[0],self.actions.shape[0])	


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
# state_voronoi.getRegionsVertices()
state_voronoi.plot('states.png')

# Define acciones iniciales

print "Action Samples:"
action_samples = np.random.randint(0,100,size=(100,2)) * 1.0
action_samples[:,0] *= 0.01
action_samples[:,1] *= 0.01 * 360
print action_samples

aq,ap,r = generate_codebook(action_samples,16,0.01);

print "Action Centroids:"
actions = np.asarray(aq)
print actions

action_voronoi = VoronoiExtractor(actions)
# print action_voronoi.getRegionsVertices()
action_voronoi.plot('actions.png')

# Define al agente

agent = Agent(states,actions)
agent.setState(0)
agent.setQLearning(1,1)

# distances = distances([0,0],np.asarray(sq))
# print distances
# print distances.argmin()

# # Genera 100 muestras de vectores de 2 elemento entre -3 y 3
# a = np.random.randint(0,100,size=(100,2)) * 1.0
# a[:,0] *= 0.01
# a[:,1] *= 0.01 * 360


# aq,ap,r = generate_codebook(a,16,0.01);

# print "Action Samples:"
# print a

# print "State Centroids:"
# print np.asarray(aq)

# action_points = np.asarray(aq);
# plotVoronoi(action_points)

# meshworld = Meshgrid()
# print meshworld.move(0,0,0,1)

# reward = Reward()
# print reward.reward([0,0],[0,0],[0,2])


# print qlearning.getQ()