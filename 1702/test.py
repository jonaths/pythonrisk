from gla import generate_codebook,distances
from voronoi import *
import random
import numpy as np
from meshgrid import Meshgrid
from reward import Reward
from random import uniform
from qlearning import *
import json	

print "Inicio..."

# Define estados iniciales

print "State Samples:"
state_samples = np.random.randint(-500,500,size=(100,2)) / 100.
print state_samples

sq,ap,sr = generate_codebook(state_samples,64,0.1);

print "State Centroids:"
states = np.asarray(sq)
print states

state_voronoi = VoronoiExtractor(states)
state_voronoi.plot('states.png')

# Define acciones iniciales

print "Action Samples:"
action_samples = np.random.randint(0,100,size=(100,2)) * 1.0
action_samples[:,0] *= 0.01 / 5
action_samples[:,1] *= 0.01 * 360
print action_samples

aq,ap,r = generate_codebook(action_samples,16,0.01);

print "Action Centroids:"
actions = np.asarray(aq)
print actions

action_voronoi = VoronoiExtractor(actions)
action_voronoi.plot('actions.png')

# Define al agente
agent = Agent(states,actions)
agent.setAgent([-1,0])
agent.setDomain(state_samples)
agent.setQLearning(0.1,0.3,0.2)

# Crea el meshworld
meshworld = Meshgrid()
reward = Reward()
endcondition = EndCondition()

# reward = Reward()
# reward.reward([0,0],[1,1],[2,0])
# reward.reward([0,0],[1,1],[3,0])
# reward.reward([0,0],[1,1],[4,0])
# print reward.getSamples()
# reward.saveToJson()
# reward.plotSprimeR2D()

# def isKnown(point):
# 	domain = [[0,4],[0,4]]

# 	if domain[0][0] <= point[0] & point[0] <= domain[0][1]:
# 		pass
# 	else:
# 		return False	

# 	if domain[1][0] <= point[1] & point[1] <= domain[1][1]:
# 		pass	
# 	else:
# 		return False

# 	return True		

# print isKnown([4,10])	

# def getAction(state):

# 	q = [[1,2,3],[14,5,6],[7,8,9]]
# 	epsilon = 1

# 	# Probabilidad de escoger una accion aleatoria
# 	prob = random.random()
# 	print prob

# 	# Si epsilon = 1 siempre elige una aleatoria
# 	# Si epsilon = 0 nunca elige una aleatoria
# 	if(prob < epsilon):
# 		print "random action"
# 		num_states = np.asarray(q).shape[1]
# 		print num_states;
# 		action = random.randint(0,num_states)
# 		print action
# 	else:	
# 		action = np.argmax(q[state])
# 	return action


# print "Start1:"

# q = [[1,2,3],[4,5,6],[7,8,9]]

# print getAction(1);



# s1 = np.random.randint(-300,300,size=(100,2)) / 100.


# print "State Samples:"
# print s1

# s1 = np.append(s1,[[7,3]],axis=0)

# print "State Samples:"
# print s1

# sq1,ap1,r1 = generate_codebook(s1,8,0.1);

# print "State Centroids:"
# print np.asarray(sq1)

# state_points1 = np.append(np.asarray(sq1),[[7,3]],axis=0)
# sq1,ap1,r1 = generate_codebook(state_points1,8,0.1);

# print "State Centroids:"
# print np.asarray(sq1)

# voronoi1 = VoronoiExtractor(np.asarray(sq1))
# voronoi1.getRegionsVertices()
# voronoi1.plot('test1.png')

# distances = distances([0,0],np.asarray(sq1))
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

# qlearning = QLearning(1,1)
# qlearning.setZeros(5,2)	 
# print qlearning.getQ()

# row = [1L,[0.1,0.2],[[1234L,1],[134L,2]]]

# dict = {}
# dict['test'] = row

# filename = 'out.json'
# with open(filename, 'wb') as outfile:
# 	json.dump(dict, outfile)