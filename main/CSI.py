import numpy as np
from scipy import stats
import sys
Sample = sys.argv[1]

f = open(f'./Input/{Sample}.txt')
a = f.readlines();f.close()
exp = [[],[]]
for i in range(len(a)):
	a[i] = a[i].split('\t')
	exp[0].append(a[i][0])
	exp[1].append(float(a[i][1]))

with open(f'Results/{Sample}/{Sample}_network.txt') as f:
	cutoff = float(f.readlines()[-1].split()[2])

f = open(f'Results/{Sample}/TFTG_score.txt')
data = f.readlines();f.close()
TG = data[0];TG = TG.strip('\n').split('\t')
del data[0];del TG[0]
TF = []
for i in range(len(data)):
	data[i] = data[i].strip('\n').split('\t')
	TF.append(data[i][0]);del data[i][0]

data1 = np.loadtxt(f'Results/{Sample}/TFTG_regulationScore.txt')
TFI = [];LTF= []
for i in range(data1.shape[0]):
	if np.max(data1[i]) > cutoff and exp[1][exp[0].index(TF[i])] > 0.5:
		LTF.append(TF[i])
		TFI.append(i)
TGI = [];LTG = []
data1 = data1.T
for i in range(data1.shape[0]):
	if np.max(data1[i]) > cutoff and exp[1][exp[0].index(TG[i])] > 0.5:
		LTG.append(TG[i])
		TGI.append(i)
TRS = []
for i in range(len(TFI)):
	s = []
	for j in range(len(TGI)):
		s.append(float(data[TFI[i]][TGI[j]]))
	TRS.append(s)
g = open(f'./Input/{Sample}_TFName.txt','w')
for i in range(len(LTF)):
	g.write(LTF[i]+'\n')
g.close()
g = open(f'./Input/{Sample}_TGName.txt','w')
for i in range(len(LTG)):
	g.write(LTG[i]+'\n')
g.close()

TRS = np.array(TRS)
data = np.log2(TRS+1)

data1 = data.copy()
for i in range(data1.shape[0]):
	if np.max(data1[i]) > 0:
		data1[i] = (data1[i]-np.mean(data1[i]))/np.std(data1[i])
data2 = data.copy();data2 = data2.T
for i in range(data2.shape[0]):
	if np.max(data2[i]) > 0:
		print(LTG[i],np.max(data2[i]),data2[i])
		data2[i] = (data2[i]-np.mean(data2[i]))/np.std(data2[i])
data2 = data2.T
data3 = (data1+data2)/2;data3[data3<0] = 0
g = open(f'./Input/{Sample}_TRS.txt','w')
for i in range(data3.shape[0]):
	s = []
	for j in range(data3.shape[1]):
		s.append(str(data3[i][j]))
	g.write('\t'.join(s)+'\n')
g.close()

data = np.loadtxt(f'./Input/{Sample}_TRS.txt')
f = open(f'./Input/{Sample}_TFName.txt')
TFName = f.readlines();f.close()
f = open(f'./Input/{Sample}_TGName.txt')
TGName = f.readlines();f.close()
nx = data.shape[0];ny = data.shape[1]

P = np.corrcoef(data)
C = np.zeros((nx,nx))
for i in range(nx):
	for j in range(nx):
		n = 0;cutoff = P[i][j] - 0.05
		for k in range(nx):
			if P[i][k] < cutoff and P[j][k] < cutoff:
				n += 1
		C[i][j] = n/nx

g = open(f'./Input/{Sample}_CSI.txt','w')
for i in range(C.shape[0]):
	st = ''
	for j in range(C.shape[1]):
		st += (str(C[i][j])+'\t')
	
	g.write(st.strip('\t')+'\n')
g.close()

