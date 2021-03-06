from gla import generate_codebook, distances, point_inside_polygon
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
    def __init__(self, states, actions):
        """Inicializacion
		
		Crea un agente con modelo MDP
		
		Arguments:
			states {numpy array} -- Un array con los prototipos de cada estado. Ej: [[1,2],[4,5],[3,7]]
			actions {[type]} -- Un array con los prototipos de cada accion. 
		"""
        self.states = np.array(states)
        self.actions = np.array(actions)
        self.position_history = []

    def setAgent(self, position):
        """Define el estado actual del agente
		
		Define en cual de los prototipos de self.states esta el agente mediante s indice
		
		Arguments:
			state_index {int} -- El indice del agente.
		"""
        self.position = position
        self.position_history.append(position)
        self.currentstate = np.argmin(distances(position, self.getStates()))
        return self.position

    def saveQ(self, filename='finalQ.txt'):

        for s in range(self.getStates().shape[0]):
            line = ""
            for c in self.getStates()[s]:
                line += str(c) + ','
            for d in self.getQ()[s]:
                line += str(d) + ','
            line += ';'
            with open(filename, 'a') as the_file:
                the_file.write(line + '\n')

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

    def setQLearning(self, alpha, gamma, epsilon):

        self.qlearning_shaped = QLearning(alpha, gamma, epsilon)
        self.qlearning_shaped.setValues(self.states.shape[0], self.actions.shape[0], 1)

        self.qlearning_real = QLearning(alpha, gamma, epsilon)
        self.qlearning_real.setValues(self.states.shape[0], self.actions.shape[0], 1)

    def clearQHistory(self):
        self.qlearning_shaped.clearHistory()
        self.qlearning_real.clearHistory()

    def resetStateCounter(self):
        self.qlearning_shaped.resetStateCounter()
        self.qlearning_real.resetStateCounter()

    def getStateCounter(self, state_index, action_index, qversion='shaped'):
        if qversion == 'shaped':
            return self.qlearning_shaped.getStateCounter(state_index, action_index)
        return self.qlearning_real.getStateCounter(state_index, action_index)

    def setEpsilon(self, epsilon):
        self.qlearning_shaped.setEpsilon(epsilon)
        self.qlearning_real.setEpsilon(epsilon)

    def getEpsilon(self, qversion='shaped'):
        if qversion == 'shaped':
            return self.qlearning_shaped.getEpsilon()
        return self.qlearning_real.getEpsilon()

    def updateQ(self, r, state, next_state, action, qversion='shaped'):
        if qversion == 'shaped':
            return self.qlearning_shaped.updateQ(r, state, next_state, action)
        return self.qlearning_real.updateQ(r, state, next_state, action)

    def getQ(self, qversion='shaped'):
        if qversion == 'shaped':
            return self.qlearning_shaped.getQ()
        return self.qlearning_real.getQ()

    def setQCell(self, state_index, action_index, qvalue, qversion='shaped'):
        if qversion == 'shaped':
            return self.qlearning_shaped.setQCell(state_index, action_index, qvalue)
        return self.qlearning_real.setQCell(state_index, action_index, qvalue)

    def getQHistory(self, qversion='shaped'):
        if qversion == 'shaped':
            return self.qlearning_shaped.getHistory()
        return self.qlearning_real.getHistory()

    def getAccumulatedReward(self, qversion='shaped'):
        if qversion == 'shaped':
            return self.qlearning_shaped.getAccumulatedReward()
        return self.qlearning_real.getAccumulatedReward();

    def getMaxQValPerState(self, qversion='shaped'):
        if qversion == 'shaped':
            return self.qlearning_shaped.getMaxVal()
        return self.qlearning_real.getMaxVal()

    def getAvgQValPerState(self, qversion='shaped'):
        if qversion == 'shaped':
            return self.qlearning_shaped.getAvgVal()
        return self.qlearning_real.getAvgVal()

    def getAction(self, selection_policy, qversion='shaped'):

        if selection_policy == 'random':
            action = self.getRandomAction()
        elif selection_policy == 'qlearning':
            if qversion == 'shaped':
                action = self.qlearning_shaped.getAction(self.currentstate)
            else:
                action = self.qlearning_real.getAction(self.currentstate)
        else:
            action = self.getRandomAction()

        return action

    def getRandomAction(self):
        """Selecciona una accion aleatoria
		
		Selecciona una accion aleatoria devolviendo el indice del arreglo de acciones
		
		Returns:
			[int] -- el indice de la accion
		"""
        action_index = randrange(0, len(self.actions))
        return action_index

    def getRandomActionValue(self):
        """Recupera el valor de una accion aleatoria
		
		Recupera un par [x,y] de una accion
		
		Returns:|
			[type] -- [x,y]
		"""
        return self.actions[self.getRandomAction()]

    def saveAgentHistoryToJson(self, filename='out.json'):
        print "Guardando informacion en ", filename
        dict = {}
        dict['action_history'] = self.action_history
        dict['position_history'] = self.position_history

        with open(filename, 'wb') as outfile:
            json.dump(dict, outfile)

    def plotTrajectory(self, plotname='trajectory.png'):

        with open('out.json') as json_data:
            data = json.load(json_data)

        data = np.array(data['position_history'])
        # Lines on top of scatter
        plt.figure()

        # Scatter plot on top of lines
        plt.plot(data[:, 0], data[:, 1], 'r', zorder=1, lw=2)
        plt.scatter(data[:, 0], data[:, 1], s=60, zorder=2)
        plt.title('Dots on top of lines')

        plt.savefig('Figures/' + plotname)

        plt.clf()
        plt.cla()
        plt.close()
