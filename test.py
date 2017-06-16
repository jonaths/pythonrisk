from qlearning import *

qlearning = QLearning(0.3,0.8,1.0)
states = [0,1,2,3,4,5,6,7,8]
actions = [0,1,2,3]
qlearning.setValues(len(states),len(actions),1)	

qlearning.updateQ(1,0,1,0)

qlearning.updateQ(1,1,0,1)

qlearning.updateQ(1,0,3,2)

qlearning.updateQ(1,3,4,0)