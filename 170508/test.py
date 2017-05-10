from qtableanalyzer import QTableAnalyzer 
import numpy as np

a = QTableAnalyzer('Output/finalQ-B600-2.0.txt',['b','x','y','>','<','^','v'])
a.read()
a.drawPolicyMap()