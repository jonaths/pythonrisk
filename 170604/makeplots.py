from qtableanalyzer import QTableAnalyzer
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt


# print "Generating policy maps"

# root = 'Output/qTableFinal'
# files = os.listdir(root)

# print "Files found:", len(files)

# for f in files:
#     print "Processing:", f
#     fullname = root + '/' + f
#     print "Fullname: " + fullname
#     print fullname
#     budget = [1, 2, 3]
#     for b in budget:
#         a = QTableAnalyzer(fullname, ['b', 'x', 'y', '^', 'v', '>', '<'])
#         a.read()
#         # # xlim, ylim, budget_value
#         a.drawPolicyMap(11, 7, b, f.replace('.txt', '') + '-' + str(b))

print "Generating reward plots..."

print "Reading CSV..."

df = pd.read_csv('rewards.csv', names=['b', 'rp', 'ep', 'r', 'steps', 'final'])
df['label'] = df.b.astype(str).str.cat(df.rp.astype(str), sep='-')


b = '30'
#rp = '2.0'
# labels = df.label.unique()
# labels = ['30-' + rp, '60-' + rp, '120-' + rp, '180-' + rp]
labels = [b + '-0.0', b + '-2.0', b + '-4.0']
window = 100

f, axarr = plt.subplots(2, sharex=True)

for l in labels:
    print l
    filtered = df[df['label'] == l][['label', 'ep', 'r', 'steps']]
    filtered['r_rm'] = pd.rolling_mean(filtered['r'], window)
    # plt.scatter([1,2,3],[1,2,3])
    print filtered.r.head()
    #plt.scatter(filtered['ep'], filtered['r_rm'], '-.')
    axarr[0].plot(filtered['ep'], filtered['r_rm'], '-', label=l)
    axarr[0].set_title('Reward')

for l in labels:
    print l
    filtered = df[df['label'] == l][['label', 'ep', 'r', 'steps']]
    filtered['steps_rm'] = pd.rolling_mean(filtered['steps'], window)
    # plt.scatter([1,2,3],[1,2,3])
    print filtered.r.head()
    #plt.scatter(filtered['ep'], filtered['r_rm'], '-.')
    axarr[1].plot(filtered['ep'], filtered['steps_rm'], '-', label=l)  
    axarr[1].set_title('Timesteps')  

plt.legend(loc=0, borderaxespad=0.,fontsize="xx-small")
plt.savefig('Figures/b-' + b + '.png')
#plt.savefig('Figures/rp-' + rp + '.png')
plt.show()

f, axarr = plt.subplots(2, sharex=True)
axarr[0].set_title('Sharing X axis')
axarr[1].scatter(x, y)



