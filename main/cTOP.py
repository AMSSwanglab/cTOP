import sys,os
import numpy as np
from sklearn.decomposition import NMF
from numpy import linalg as LA
sample = sys.argv[1]
C = np.loadtxt('./Input/'+sample+'_CSI.txt')
R = np.loadtxt('./Input/'+sample+'_TRS.txt')
R = R/(np.max(R,1).reshape(R.shape[0],1))
f = open(f'./Results/{sample}/GE.txt')
E = f.readlines();f.close()
ECell = E[0];del E[0]
ECell = ECell.strip('\n').split('\t');del ECell[0]
for i in range(len(E)):
    E[i] = E[i].split('\t')
    del E[i][0]
    for j in range(len(E[i])):
        E[i][j] = float(E[i][j])
E = np.array(E)

# Setting Number of Clusters
K = int(sys.argv[2]);

### Initiation

rep = 50
print("Initializing X for TF-TF CSI Matrix...")
err1 = np.zeros(rep)
for i in range(0, rep):
    model = NMF(n_components=K, init='random', random_state=i, solver='cd', max_iter=50)
    X0 = model.fit_transform(C)
    X1 = model.components_
    err1[i] = LA.norm(C - np.dot(X0, X1), ord='fro')
model = NMF(n_components=K, init='random', random_state=np.argmin(err1), solver='cd', max_iter=1000)
X0 = model.fit_transform(C)
X1 = model.components_

print("Initializing non-negative matrix factorization for E...")
E = np.log(1 + E);E = E / np.max(E)
err1 = np.zeros(rep)
for i in range(0, rep):
    model = NMF(n_components=K, init='random', random_state=i, solver='cd', max_iter=50)
    W10 = model.fit_transform(E)
    H10 = model.components_
    err1[i] = LA.norm(E - np.dot(W10, H10), ord='fro')
model = NMF(n_components=K, init='random', random_state=np.argmin(err1), solver='cd', max_iter=1000)
W10 = model.fit_transform(E)
H10 = model.components_

print("Initializing hyperparameters lambda1, lambda2 and mu...")

mu1 = np.sum(C*np.dot(X0,X1)) / pow(LA.norm(C - np.dot(X0, X0.T), ord='fro'), 2)
mu2 = 2 * pow(LA.norm(E - np.dot(W10, H10), ord='fro'), 2) / pow(LA.norm(C - np.dot(X0, X0.T), ord='fro'), 2)
mu4 = np.trace(np.dot(np.dot(X1,R),W10)) / pow(LA.norm(C - np.dot(X0, X0.T), ord='fro'), 2)


err = 1000;eps = 0.001;maxiter = 5000000000;it = 0
def Loss(x0,w1,h1):
    t1 = pow(LA.norm(C - np.dot(x0, x0.T), ord='fro'), 2)
    t2 = mu1 * np.sum(C * np.dot(x0,x0.T))
    t3 = mu2 * pow(LA.norm(E - np.dot(w1, h1), ord='fro'), 2)
    t5 = mu4 * np.trace(np.dot(np.dot(x0.T,R),w1))
    return t1 - t2 + t3 - t5
def Norm(X):
    X = X/np.sqrt(np.sum(X**2,0).reshape(1,X.shape[1]))
    X = X/(np.sum(X,1).reshape(X.shape[0],1)+eps)
    return X
X = X0.copy();W1 = W10.copy();H1 = H10.copy()
loss1 = Loss(X, W1, H1)
while err > 1e-4 and it < maxiter-1:
    XNext = X * ((1+mu1/2)*np.dot(C,X)+mu4/4*np.dot(R,W1)) / (eps + np.dot(np.dot(X,X.T),X))
    W1Next = W1 * (np.dot(E,H1.T)+mu4/mu2*np.dot(R.T,X)) / (eps + np.dot(np.dot(W1,H1),H1.T))
    H1Next = H1 * np.dot(W1.T,E) / (eps + np.dot(np.dot(W1.T,W1),H1))
    M1 = np.zeros((K, K));M2 = np.zeros((K, K));
    for z in range(K):
        M1[z, z] = LA.norm(H1Next[z, :])
    XNext = Norm(XNext)
    W1Next = W1Next/(np.sum(W1Next,1).reshape(W1Next.shape[0],1)+eps)
    H1Next = np.dot(LA.inv(M1), H1Next);
    loss2 = Loss(XNext,W1Next,H1Next)
    err = np.abs(loss2-loss1)
    loss1 = loss2
    X = XNext.copy();W1 = W1Next.copy();H1 = H1Next.copy()
    print(f'{it}th step,err = {err}')
    it += 1


if not os.path.exists(f'./Results/{sample}'):
    os.mkdir(f'./Results/{sample}')
if not os.path.exists(f'./Results/{sample}/{K}'):
    os.mkdir(f'./Results/{sample}/{K}')
np.savetxt(f'./Results/{sample}/{K}/X0.txt',X0,delimiter='\t')
np.savetxt(f'./Results/{sample}/{K}/W10.txt',W10,delimiter='\t')
np.savetxt(f'./Results/{sample}/{K}/H10.txt',H10,delimiter='\t')
np.savetxt(f'./Results/{sample}/{K}/X.txt',X,delimiter='\t')
np.savetxt(f'./Results/{sample}/{K}/W1.txt',W1,delimiter='\t')
np.savetxt(f'./Results/{sample}/{K}/H1.txt',H1,delimiter='\t')
