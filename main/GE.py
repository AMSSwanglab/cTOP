import numpy as np
import sys
Sample = sys.argv[1]
f = open(f'Input/{Sample}.csv')
data = f.readlines();f.close()

#d_gene={}
#with open('/public/home/wangwen_lab/lizihe/project/lurong/05.anno/13.v4.regine/id_conver/mhl.v4.refined.namepair.tsv') as f:
#	for line in f:
#		l = line.strip().split()
#		d_gene[l[0]] = l[1]


g = open(f'Results/{Sample}/GE.txt','w')
data[0] = '\t'.join(data[0].split(','))
g.write(data[0]);del data[0]
gene = []

for i in range(len(data)):
	l = data[i].split(',')
	lenth = len(l) -1 
#	lenth =  len(data[i].split(',')) - 1 
#	l[0] = d_gene[l[0]]
	data[i] = '\t'.join(l)
	gene.append(l[0])	
#print(gene)

f = open(f'Input/{Sample}_TGName.txt')
a = f.readlines();f.close()
for i in range(len(a)):
	a[i] = a[i].strip()
	if a[i] in gene:
		indel = gene.index(a[i])
		g.write(data[indel])
	else:
		value = np.zeros(lenth).tolist()
		word = a[i] + '\t' + '\t'.join(str(x) for x in value) + '\n'
		g.write(word)
g.close()

#import numpy as np

f = open(f'Results/{Sample}/GE.txt')
data = f.readlines();f.close()
g = open(f'Results/{Sample}/GE.txt','w')
g.write(data[0]);del data[0]
gene = []
for i in range(len(data)):
#	print(data[i])
	data[i] = data[i].split('\t')
	gene.append(data[i][0]);del data[i][0]
	for j in range(len(data[i])):
		data[i][j] = float(data[i][j])
data = np.array(data).T
for i in range(data.shape[0]):
	data[i] = data[i]/np.sum(data[i])*1000000
data = data.T
for i in range(len(gene)):
	g.write(gene[i])
	for j in range(data.shape[1]):
		g.write('\t'+str(data[i][j]))
	g.write('\n')
g.close()
