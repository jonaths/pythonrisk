# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from listpolicymap import plotheatmap

class QTableAnalyzer:

	def __init__(self,qTableTxtFile,headers):
		self.file = qTableTxtFile
		self.headers = headers

	def read(self):
		# Lee las líneas a,b,c,;\n
		lines = [line.rstrip(',;\n') for line in open(self.file)] 

		q = []
		# Recupera las lineas y las convierte a float
		for l in lines:
			s = l.split(',')
			r = []
			for e in s:
				r.append(float(e))
			q.append(r)

		# Crea array
		self.qtable = np.array(q)

		# Crea pandas
		# df = pd.DataFrame.from_records(self.qtable,columns=self.headers)

	def filterByColumnValue(self,column_name,column_value):
		column_index = self.headers.index(column_name)
		filtered_table = np.array([i for i in self.qtable if i[column_index] == column_value])
		return filtered_table

	"""Crea un mapa de la politica seguida en un gridworld con cuatro acciones
	
	Asume una lista [[b,x,y,vright,vleft,vup,vdown],[]... ]
	"""

	def drawPolicyMap(self,label='label'):

		xlim = 19
		ylim = 17
		x = range(xlim)
		y = range(ylim)

		column_name = 'b'
		column_value = 3

		filtered_table = self.filterByColumnValue(column_name,column_value)

		avg_filtered_table = self.getNeighAvg(filtered_table)

		

		intensity = np.zeros((xlim,ylim))
		policy = np.zeros((xlim,ylim))
		for r in filtered_table:
			maxIntArg = self.getMaxIndexAndVal(r[-4:]);
			intensity[int(r[1])][int(r[2])] = maxIntArg[0]
			policy[int(r[1])][int(r[2])] = maxIntArg[1]


		
		plotheatmap(x,y,intensity.T,policy.T,self.headers,'heatmap-' + str(column_value) + '-' + str(label) + '.png')

	def getMaxIndexAndVal(self,r):
		print r,np.amax(r),np.argmax(r),self.headers[np.argmax(r)+3]
		return [np.average(r),np.argmax(r)]

	def getNeighAvg(self,filtered_table):
		print filtered_table
		for r in filtered_table:
			if x==0:

			elif x==xlim-1

			elif y==0:

			elif y==ylim-1:

			elif x==0 and y==0:
			
			elif x==0 and y==ylim-1:

			elif x==xlim-1 and y==ylim-1:
			
			else:
				vals = []
				vals.append(r)	
				aqui voy... 



		sys.exit()
			

