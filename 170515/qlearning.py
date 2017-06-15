import random
import warnings

import numpy as np
import sys


class QLearning:
    def __init__(self, alpha, gamma, epsilon):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        # Un array con una entrada por cada actualizacion de Q
        # [[s,a,sprime,r],[s,a,sprime,r],...]
        self.history = []
        self.state_counter = {}

    def setValues(self, num_states, num_actions, value):
        """
        Crea una matriz de cros
        :param num_states: 
        :param num_actions: 
        :param value: 
        :return: 
        """
        self.Q = np.empty(shape=(num_states, num_actions))
        self.Q.fill(np.nan)
        return self.Q

    def getQ(self):
        return self.Q

    def setQ(self, newQ):
        self.Q = newQ
        return self.newQ

    def setEpsilon(self, epsilon):
        self.epsilon = epsilon

    def getEpsilon(self):
        return self.epsilon

    def updateStateCounter(self, state_index):
        """
        Actualiza el contador de estados o lo crea para el estado si no existe
        :param state_index: el indice del contador de estados
        :return: 
        """

        if state_index not in self.state_counter:
            self.state_counter[state_index] = 1
        else:
            self.state_counter[state_index] += 1

    def resetStateCounter(self):
        print "reseting state_counter..."
        self.state_counter = {}

    def getStateCounter(self, state_index, action_index):
        if state_index not in self.state_counter:
            self.state_counter[(state_index, action_index)] = 1
        return self.state_counter[(state_index, action_index)]

    def updateQ(self, rsa, state, next_state, action):

        print "newQ Update -----------------------------------------------------------|"

        print "rsa:", rsa, ", state:", state, ", next_state:", next_state, ", action:", action

        qsa = self.Q[state][action]

        # Verifica si el qsa actual existe, si no existe asigna rsa
        if np.isnan(qsa):
            qsa = rsa
            print "qsa isnan!"

        print "qsa", qsa, ", alpha:", self.alpha

        # Copia el valor seteado de alpha
        real_alpha = self.alpha

        # Mira si existe el maximo del siguiente estado
        with warnings.catch_warnings():
            warnings.filterwarnings('error')
            try:
                # Si existe recuperalo
                maxNext = np.nanmax(self.Q[next_state, :])
            except Warning as e:
                # Si no existe ignoralo haciendo alpha = 0
                print "maxNext isnan!"
                real_alpha = 0
                maxNext = 0

        print "maxNext:", maxNext, ", realAlpha:", real_alpha

        # Actualiza el valor Q
        new_q = qsa + real_alpha * (rsa + self.gamma * maxNext - qsa)

        # Actualiza la tabla Q
        self.Q[state, action] = new_q
        print "Q[s,a]:", self.Q[state, action]

        # Guarda la historia
        self.history.append(dict(state=state, action=action, next_state=next_state, rsa=rsa))
        print "History:", self.history[:4]
        # Actualiza el contador de estados
        self.updateStateCounter((state, action))
        return new_q

    def getHistory(self):
        return self.history

    def getAccumulatedReward(self):
        acc_reward = 0
        for h in self.history:
            acc_reward += h['rsa']
        return acc_reward

    def clearHistory(self):
        print "clearing q history..."
        print "history", self.history;
        print "accumulated reward:", self.getAccumulatedReward()

        # Resetea el historial
        self.history = []

    def getAction(self, state):

        # Probabilidad de escoger una accion aleatoria
        prob = random.random()

        num_states = np.asarray(self.Q).shape[1]

        # Si epsilon = 1 siempre elige una aleatoria
        # Si epsilon = 0 nunca elige una aleatoria
        if prob < self.epsilon:
            # Escoge una accion aleatoria
            print "action random"

            action = random.randint(0, num_states - 1)
        else:
            # Si hay un maximo regresa el maximo, de lo contrario la accion aleatoria
            try:
                action = np.nanargmax(self.Q[state])
            except ValueError:
                action = random.randint(0, num_states - 1)

            print "action max " + str(action) + " " + str(self.Q[state])

        return action

    def getMaxVal(self):

        max = []
        for r in self.Q:
            max.append(np.amax(r))
        return max

    def getAvgVal(self):

        avg = []
        for r in self.Q:
            avg.append(np.average(r))
        return avg

        # def reMapQ(states,statesprime):
        # 	aqui voy... funcion para remapear Q
