from qtableanalyzer import QTableAnalyzer
import numpy as np
import os

# a = QTableAnalyzer('Output/qTableFinal-B60-RP1.0-EP09998.txt',['b','x','y','^','v','>','<'])
# a.read()
# # xlim, ylim, budget_value
# a.drawPolicyMap(11,6,2)

root = 'Output/qTableFinal'
files = os.listdir(root)

print "Files found:", len(files)

for f in files:
    print "Processing:", f
    fullname = root + '/' + f
    print "Fullname: " + fullname
    print fullname
    budget = [1, 2, 3]
    for b in budget:
        a = QTableAnalyzer(fullname, ['b', 'x', 'y', '^', 'v', '>', '<'])
        a.read()
        # # xlim, ylim, budget_value
        a.drawPolicyMap(11, 7, b, f.replace('.txt', '') + '-' + str(b))
