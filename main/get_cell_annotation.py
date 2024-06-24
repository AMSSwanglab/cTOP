import numpy as np
import sys
 
sample = sys.argv[1]
K = sys.argv[2]
H = np.loadtxt(f'Results/{sample}/{K}/H1.txt')
H = H.T
anno = []
for i in range(H.shape[0]):
	max = H[i,:].max()
	anno.append(list(H[i,:]).index(max))
with open(f'Results/{sample}/GE.txt') as f:
	cells = f.readline().rstrip().split('\t')[1:]

with open(f'Results/{sample}/{K}/{sample}_{K}modules_cellanno.txt','w') as out:
	for i in range(len(cells)):
		print(f'{cells[i]}\t{anno[i]}',file=out)