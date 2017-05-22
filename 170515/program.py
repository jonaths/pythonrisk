import sys

from agentanalyzer import AgentAnalyzer
from budgetagent import BudgetAgent
from endcondition import EndCondition
from gridworld import GridWorld
from qlearning import *
from reward import Reward

print "Inicio..."

# xlim = 16
# ylim = 7
# initial_position = [0,3]

xlim = 11
ylim = 6
blim = 4
initial_position = [3, 0, 0]

reward = Reward()
endcondition = EndCondition()

# El numero de episodios
episodes = 6

# El numero de pasos de cada episodio
maxsteps = 5

# Cuantas veces ha encontrado una salida
end_counter = 0

# El presupuesto inicial (igual al numero de pasos)
init_budget = maxsteps - 2

risk_profile = [0.0, 1.0]

for rp in risk_profile:
    print "#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#"
    print "RP " + str(rp) + " ------------------------------------------------------------------------------"

    gridworld = GridWorld(xlim, ylim)
    grid_states = np.asarray(gridworld.getStates())
    actions = np.asarray(gridworld.getActions())

    # Define al agente
    agent = BudgetAgent(grid_states, actions, blim)
    agent.setAgent(initial_position)

    # alpha,gamma,epsilon
    agent.setQLearning(0.3, 0.8, 1.0)

    log = {}
    log['rewards'] = []
    log['steps'] = []

    for i in range(0, episodes):
        print "---------------------------------------------------------------------------------------------"
        print "START EPISODE"

        currentstate_index = agent.getCurrentState()
        agent.setBudget(init_budget, maxsteps)
        print "currentstate_index:", currentstate_index
        print "budget:", agent.getBudget()

        print "Nuevo episodio " + str(i) + "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

        for j in range(0, maxsteps):

            print "Nueva iteracion " + str(i) + "," + str(
                j) + " ==========================================================="

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
            while not validMove:

                action_index = agent.getAction('qlearning')
                action = agent.getActions()[action_index]
                print "newaction:", action_index, action

                # Recupera la nueva posicion a traves de ejecutar una accion
                newposition = gridworld.move(agent.getCurrentPosition()[-2:], action)
                print "newposition:", newposition

                if newposition:
                    validMove = True
                    print "+ valid move"

            # Incluye el presupuesto en la posicion
            newposition = np.append([agent.getBudgetState()], newposition)
            print "newposition with budget:", newposition

            # Calcula la recompensa que devuelve el ambiente
            current_reward = reward.reward(currentposition, action, newposition)
            print "reward:", current_reward

            # Calcula la shaped_reward que considera el riesgo inherente, la recompensa real y el perfil de riesgo
            shaped_reward = agent.getShapedReward(current_reward, newposition, rp)
            print "shaped_reward:", shaped_reward

            # Actualiza el budget con la ultima recompensa real (le pasa maxsteps para calcular automaticamente las
            # divisiones en tres tercios)
            agent.setBudget(agent.getBudget() + current_reward, maxsteps)

            # Convierte newposition de numpy a lista
            agent.setAgent(newposition.tolist())

            newstate_index = agent.getCurrentState()
            print "newstate:", newstate_index

            print "Q epsilon:", str(agent.getEpsilon())

            # Actualiza la tabla Q con la shaped reward, no con la recompensa real
            newQ = agent.updateQ(shaped_reward, currentstate_index, newstate_index, action_index)
            print "newQ:", str(newQ)

            # Verifica si debe terminar el episodio
            if endcondition.verify(currentposition, action, newposition, current_reward):
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

        # Si se cumple la condicion elimina la exploracion
        # if end_counter > 10:
        # 	agent.setEpsilon(0)

        log['rewards'].append(agent.getAccumulatedReward())
        log['steps'].append(j + 1)

        if i != 0 and i % 2 == 0 or i == episodes - 1:
            name = 'B' + str(maxsteps) + '-RP' + str(rp) + '-EP' + str(format(i, "05d"))

            # Guarda un avance parcial de la tabla Q
            agent.saveQ('Output/qTable-' + name + '.txt')
            # Guarda el historial de los episodios
            agent.saveHistoryToJson('Output/history-' + name + '.json')

        agent.clearPositionHistory()
        agent.clearQHistory()

        agent.setAgent(initial_position)
        print "END EPISODE"
        print "---------------------------------------------------------------------------------------------"

    name = 'B' + str(maxsteps) + '-RP' + str(rp) + '-EP' + str(format(i, "05d"))

    print "Resultados Finales ########################################################"

    print "Q Num States:"
    print len(agent.getQ())

    print "End Reasons:"
    print endcondition.getReasons()

    print "end_counter:"
    print str(end_counter) + "/" + str(episodes)

    analysis = AgentAnalyzer(log)
    # analysis.plotRewardsAndSteps()
    analysis.plotEndReasons(endcondition.getReasons(), 'reasonsend-B' + str(maxsteps) + '-' + str(rp) + '.png')
