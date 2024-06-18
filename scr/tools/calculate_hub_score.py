import networkx as nx
import sys
import pandas as pd 
inf = sys.argv[1]

df = pd.read_csv(inf,sep='\t',names=['TF','TG','Score','RE'])
#print(df)
df = df[~df['TG'].str.startswith('RPS')]
df = df[~df['TG'].str.startswith('RPL')]
df = df[~df['TG'].str.startswith('MT-')]
#print(df)
edges =df[['TF','TG','Score']].to_records(index=False)
edges=list(edges)
G=nx.Graph()
G=G.to_directed()
G.add_weighted_edges_from(edges)


#G = nx.from_pandas_edgelist(df, 'TF', 'TG', 'Score',create_using=nx.DiGraph)
h, a = nx.hits(G,max_iter=1000,normalized=False)

h = pd.Series(h).sort_values(ascending=False)
a = pd.Series(a).sort_values(ascending=False)

h = h[h>0]
a = a[a>0]

a.to_csv(f'{inf}.authority_score.txt',sep='\t',header=False)
h.to_csv(f'{inf}.hub_score.txt',sep='\t',header=False)
