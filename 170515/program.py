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
from budgetagent import BudgetAgent




	

print "Inicio..."

# xlim = 16
# ylim = 7
# initial_position = [0,3]

xlim = 5
ylim = 3
blim = 4
initial_position = [1,0,0]

gridworld = GridWorld(xlim,ylim)
grid_states = np.asarray(gridworld.getStates())
actions = np.asarray(gridworld.getActions())


# Define al agente
agent = BudgetAgent(grid_states,actions,blim)
agent.setAgent(initial_position)

# alpha,gamma,epsilon
agent.setQLearning(0.3,0.8,1.0)

reward = Reward()
endcondition = EndCondition()

# El numero de episodios
episodes = 500

# El numero de pasos de cada episodio
maxsteps = 240

# Cuantas veces ha encontrado una salida
end_counter = 0

# El presupuesto inicial (igual al numero de pasos)
init_budget = maxsteps - 2

risk_profile = [0.0]

for rp in risk_profile:

	log = {}
	log['rewards'] = []
	log['steps'] = []

	for i in range(0,episodes):
		print "---------------------------------------------------------------------------------------------"
		print "START EPISODE"

		currentstate_index = agent.getCurrentState();
		agent.setBudget(init_budget,maxsteps)
		print "currentstate_index:",currentstate_index
		print "budget:",agent.getBudget()

		print "Nuevo episodio " + str(i) + "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

		for j in range(0, maxsteps):

			print "Nueva iteracion " + str(i) + "," + str(j) + " ==========================================================="

			# Presupuesto
			print "budget:", agent.getBudget()

			# Epsilon
			# epsilon = agent.getBudget() * 1.0 / init_budget
			# agent.setEpsilon( epsilon )
			# print "epsilon:", epsilon	

			# Estado actual
			currentstate = agent.getStates()[currentstate_index]
			currentposition = agent.getCurrentPosition()
			print "currentstate:", currentstate_index, currentstate

			# Posicion actual (considerando todo el vector de estado)
			# Realmente la posicion son la columna 1 y 2
			print "currentposition:", currentposition

			# Se asegura de que el movimiento sea valido
			validMove = False 
			while (validMove == False):

				action_index = agent.getAction('qlearning');	
				action = agent.getActions()[action_index]
				print "newaction:", action_index, action

				# Recupera la nueva posicion a traves de ejecutar una accion
				newposition = gridworld.move(agent.getCurrentPosition()[-2:],action)
				print "newposition:", newposition

				if newposition:
					validMove = True
					print "+ valid move"

			# Incluye el presupuesto en la posicion
			newposition = np.append([agent.getBudgetState()],newposition)
			print "newposition with budget:",newposition

			# Calcula la recompensa que devuelve el ambiente
			current_reward = reward.reward(currentposition,action,newposition)
			print "reward:", current_reward

			# Calcula la shaped_reward que considera el riesgo inherente, la recompensa real y el perfil de riesgo
			shaped_reward = agent.getShapedReward(current_reward,newposition,rp)
			print "shaped_reward:", shaped_reward

			# Actualiza el budget con la ultima recompensa real (le pasa maxsteps para calcular automaticamente las divisiones en tres tercios)
			agent.setBudget(agent.getBudget()+current_reward,maxsteps)
			
			# Convierte newposition de numpy a lista
			agent.setAgent(newposition.tolist())
			
			newstate_index = agent.getCurrentState()
			print "newstate:", newstate_index

			print "Q epsilon:",str(agent.getEpsilon())

			# Actualiza la tabla Q con la shaped reward, no con la recompensa real
			newQ = agent.updateQ(shaped_reward, currentstate_index, newstate_index, action_index)
			print "newQ:",str(newQ)

			# Verifica si debe terminar el episodio
			if endcondition.verify(currentposition,action,newposition,current_reward):
				print "endingposition:" + str(newposition)
				end_counter = end_counter + 1
				print "Ending ------------------------------------------------------------------"
				break

			# Determina el nuevo estado
			currentstate_index = newstate_index

			# name = input('Enter para continuar... ')
			# print('Hello ', name)

			# Si ya no tiene presupuesto termina
			# if agent.getBudget() <= 0:
			# 	print "Out of budget------------------------------------------------------------"
			# 	break

			if newposition[0] < 0:
				sys.exit(0)

		# Imprime la politica solo en el ultimo episodio
		if(i == episodes - 1):	
			print "printing trajectory"
			agent.saveAgentHistoryToJson()
			agent.plotTrajectory();

		# Si se cumple la condicion elimina la exploracion
		# if end_counter > 10:
		# 	agent.setEpsilon(0)		

		log['rewards'].append(agent.getAccumulatedReward())	
		log['steps'].append(j+1)

		# Guarda un avance parcial de la tabla Q
		if(i != 0 and 100 % i == 0):
			agent.saveQ('Output/qTable-' + 'B' + str(maxsteps) + '-RP' + str(rp) + '-EP' + str(format(i, "05d")) + '.txt')

		agent.clearPositionHistory()
		agent.clearActionHistory()
		agent.clearQHistory()
		agent.setAgent(initial_position)
		print "END EPISODE"
		print "---------------------------------------------------------------------------------------------"


	# Datos para generar heatmaps para cada nivel de budget
	n = xlim * ylim
	m = 3
	b = blim

	# Recupera lista de los estados
	agent_states = agent.getStates()
	valQPerState = agent.getAvgQValPerState()

	agent.saveQ('Output/qTableFinal-' + 'B' + str(maxsteps) + '-RP' + str(rp) + '-EP' + str(format(i, "05d")) + '.txt')

	x = range(xlim)
	y = range(ylim)
	intensity = np.zeros((xlim,ylim))
	for bi in range(b):
		print "Processing states for b",bi
		len_a = len(agent_states[bi*n:bi*n+n,1:m])
		for s in range(len_a):
			current_index = bi * len_a + s
			# print str(agent_states[current_index]) ,str(maxQPerState[current_index])
			intensity[agent_states[current_index][1]][agent_states[current_index][2]] = valQPerState[current_index]
		plotheatmap(x,y,intensity.T,'heatmap-' + str(bi) + '-B' + str(maxsteps) + '-' + str(rp) + '.png')


		print "Resultados Finales ########################################################"

		# print "Q"
		# print agent.getQ()
		# print "Q[0]:"
		# print agent.getQ()[0]
		# print "Q[0][1]:"
		# print agent.getQ()[0][1]
		print "Q Num States:"
		print len(agent.getQ())

		print "End Reasons:"
		print endcondition.getReasons()

		print "end_counter:"
		print str(end_counter) + "/" + str(episodes)

		analysis = AgentAnalyzer(log)
		# analysis.plotRewardsAndSteps()
		analysis.plotEndReasons(endcondition.getReasons(),'reasonsend-B' + str(maxsteps) + '-' + str(rp) + '.png')
