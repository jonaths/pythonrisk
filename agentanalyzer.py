import numpy as np
import random
import matplotlib.pyplot as plt


class AgentAnalyzer:
    def __init__(self, info):
        self.info = info
        self.folder = 'Figures/'

    def movingaverage(self, interval, window_size):
        window = np.ones(int(window_size)) / float(window_size)
        return np.convolve(interval, window, 'same')

    def plotRewardsAndSteps(self, filename='rewardandplot.png', w=5):
        x = range(len(self.info['rewards']))

        plt.figure(1)
        plt.subplot(211)
        plt.plot(x, self.movingaverage(self.info['rewards'], w), 'b-')

        plt.subplot(212)
        plt.plot(x, self.movingaverage(self.info['steps'], w), 'r-')
        plt.savefig(self.folder + filename)

    def plotEndReasons(self, reasons, filename='reasonsend.png'):
        reasons_keys = list(reasons.keys())
        print reasons
        print reasons_keys
        data = []
        for r in reasons_keys:
            data.append(reasons[r])

        # Plot
        plt.pie(data, labels=reasons_keys, autopct='%1.1f%%', startangle=140)

        plt.axis('equal')
        plt.savefig(self.folder + filename)
        plt.close()
