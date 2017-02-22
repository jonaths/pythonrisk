from gla import generate_codebook,distances
from voronoi import *
import random
import numpy as np
from meshgrid import Meshgrid
from reward import Reward
from random import uniform
from qlearning import *
import json	

def getAction(state):
	q = [[1,2,3],[14,5,6],[7,8,9]]
	action = np.argmax(q[state])
	return action


print "Start1:"

q = [[1,2,3],[4,5,6],[7,8,9]]

print getAction(1);



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