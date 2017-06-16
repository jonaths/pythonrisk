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
from agent import Agent
from riskmapper import RiskMapper


class BudgetAgent(Agent):
    def __init__(self, states, actions, blim):
        Agent.__init__(self, states, actions)
        base = self.states
        shape = np.shape(base)
        temp = np.zeros((blim * shape[0], shape[1] + 1))

        c = 0
        for b in range(blim):
            for p in base:
                temp[c] = [b, p[0], p[1]]
                c += 1

        self.states = temp

    def saveHistoryToJson(self, prefix, budget, rp, episode):

        filename = prefix + str(budget) + '-RP' + str(rp) + '-EP' + str(format(episode, "05d")) + '.json '

        print "Guardando informacion en ", filename

        historyDict = {'q_history': self.getQHistory(),
                       'position_history': self.position_history}

        with open(filename, 'wb') as outfile:
            json.dump(historyDict, outfile)

        # aqi voy... guardar una linea de json por cada experimento

    def setBudget(self, budget, max):
        """
        Mapea un numero budget a un estado con 4 posibles niveles. El ultimo nivel es 0. Los demas se distribuyen 
        proporcionalmente en tercios. 
        :param budget: el presupuesto actual
        :param max: la referencia maxima que divide entre 3
        :return: 
        """

        self.budget = budget

        if budget <= 0:
            self.budgetstate = 0

        elif 0 < budget <= max / 3:
            self.budgetstate = 1

        elif max / 3 < budget <= max / 3 * 2:
            self.budgetstate = 2
            # self.budgetstate = 1

        else:
            self.budgetstate = 3
            # self.budgetstate = 1



        return self.budget

    def getShapedReward(self, reward, sprime, risk_profile):
        risk = RiskMapper.getMap(sprime)

        budget_level = sprime[0]

        # c = 0
        # if reward < 0:
        #     if budget_level == 3:
        #         c = + 0.5
        #     elif budget_level == 2:
        #         c = 0
        #     elif budget_level == 1:
        #         c = - 0.5

        # shaped_reward = 1.0 * (reward - c) - risk_profile * risk

        c = 1
        if reward < 0:
            if budget_level == 3:
                c = + 2.0
            elif budget_level == 2:
                c = 1
            elif budget_level == 1:
                c = + 0.5

        shaped_reward = (reward - risk_profile * risk) / c

        print sprime, reward, c, budget_level, risk_profile, risk, shaped_reward

        return shaped_reward

    def getBudget(self):
        return self.budget

    def getBudgetState(self):
        return self.budgetstate
