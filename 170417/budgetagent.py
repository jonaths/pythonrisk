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
from agent import Agent

class BudgetAgent(Agent):	

	def __init__(self,states,actions,blim):
		Agent.__init__(self,states,actions)
		base = self.states
		shape = np.shape(base)
		temp = np.zeros((blim*shape[0],shape[1]+1))
		
		c = 0
		for b in range(blim):
			for p in base:
				temp[c] = [b,p[0],p[1]]
				c+=1

		self.states = temp

	def saveAgentHistoryToJson(self, filename = 'out.json'):
		print "Guardando informacion en " , filename
		
		dict = {}
		dict['action_history'] = self.action_history
		dict['position_history'] = self.position_history

		with open(filename, 'wb') as outfile:
			json.dump(dict, outfile)

	def setBudget(self,budget):
		self.budget = budget	
		# TO-DO: poner codigo para mapear budget a budgetstate	

		if budget <= 0:
			self.budgetstate = 0

		elif budget	> 0 and budget <= 180:
			self.budgetstate = 1

		elif budget	> 180 and budget <= 360:
			self.budgetstate = 2	

		else:
			self.budgetstate = 3

			# pasa algo con maxtesps=900 y pasos en 300 y 600. El mapa para presupuesto 2 y 1 apaece todo negro?

		# self.budgetstate = 0
		return self.budget

	def getBudget(self):
		return self.budget

	def getBudgetState(self):
		return self.budgetstate	
