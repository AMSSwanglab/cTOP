import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import sys
Sample = sys.argv[1]
K = int(sys.argv[2])
f = open(f'./Input/{Sample}_TGName.txt')
TG = f.readlines();f.close()
TG = [TG[i].strip('\n') for i in range(len(TG))]

f = open(f'Results/{Sample}/{Sample}_network.txt')
net = f.readlines();f.close()
del net[0]
for i in range(len(net)):
    net[i] = net[i].strip('\n').split('\t')
    net[i][4] = net[i][4].split(';')

W1 = np.loadtxt(f"./Results/{Sample}/{K}/W1.txt").T
#W2 = np.loadtxt(f"./Results/{Sample}/{Sample}_W2.txt").T
#W0 = 0.9*W1 + 0.1*W2
W0 = W1
module = list()
for t in range(W0.shape[0]):
    #module[t] = []
    W = W0[t]
    me = np.mean(W);sd = np.std(W)
    cTG = []
    TGs = []
    for i in range(len(TG)):
        x = (W[i]-me)/sd
        p = 1-stats.norm.cdf(x)
        if p <= 0.05 or W[i]>=0.95:
            cTG.append([TG[i],W[i],p])
            TGs.append(TG[i])
    #        module[t].append(TG[i])
    g = open(f'./Results/{Sample}/{K}/{Sample}_module{t}.txt','w')
    cTG.sort(key = lambda x:-x[1])
    cTG = [f'{i[0]}\t{i[1]}\t{i[2]}' for i in cTG]
    g.write('\n'.join(cTG))
    g.close()
#    for k in range(W0.shape[0]):
    f = open(f'./Results/{Sample}/{K}/{Sample}_tf{t}_TFs.txt')
    cTF = f.readlines();f.close()
    cTF = [cTF[i].split('\t')[0] for i in range(len(cTF))]
    g = open(f'./Results/{Sample}/{K}/{Sample}_tf{t}_module{t}_SubNetwork.txt','w')
    cRE = []
    for i in range(len(net)):
        if net[i][0] in cTF and net[i][1] in TGs:
            g.write(net[i][0]+'\t'+net[i][1]+'\t'+net[i][2]+'\t')
            RE1 = []
            for j in range(len(net[i][4])):
                if net[i][4][j] != "":
                    RE1.append(net[i][4][j])
            cRE += RE1
            g.write(';'.join(RE1)+'\n')
    g.close()

