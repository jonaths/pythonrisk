from qtableanalyzer import QTableAnalyzer 
import numpy as np

print "XXXXXXXXXXXXXXX"

a = QTableAnalyzer('Output/qTableFinal-B240-RP0.0-EP00499.txt',['b','x','y','^','v','>','<'])
a.read()
a.drawPolicyMap()