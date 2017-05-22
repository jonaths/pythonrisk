#!/usr/bin/python

from math import sin, cos


class GridWorld:
    def __init__(self, xlim, ylim):
        self.xlim = xlim
        self.ylim = ylim
        self.getStates()

    def getStates(self):
        self.states = []
        for x in range(self.xlim):
            for y in range(self.ylim):
                self.states.append([x, y])
        return self.states

    def getActions(self):
        # 0: arriba
        # 1: abajo
        # 2: derecha
        # 3: izquierda
        self.actions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        return self.actions

    def move(self, state, action):
        """
        Mueve al agente en funcion de la accion y regresa la posicion siguiente
        :param state: Un par [x,y]
        :param action: Una accion [pasos en x, pasos en y]
        :return: un par con las nuevas coordenadas despues de moverse
        """

        newx = state[0] + action[0]
        newy = state[1] + action[1]

        if newx < 0:
            return False
        if newx > self.xlim - 1:
            return False
        if newy < 0:
            return False
        if newy > self.ylim - 1:
            return False

        return [newx, newy]
