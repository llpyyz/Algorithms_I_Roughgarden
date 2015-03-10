#https://codehiker.wordpress.com/2012/04/06/kosarajus-scc/

import sys
import resource

sys.setrecursionlimit(3000000)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

p = "C:/Users/David/Documents/TechStuff/OnlineCourses/Coursera/Algos_DesignAndAnalysis_PartI_Roughdarden_sp2015/Week4/SCC/"
p1 = "C:/Users/David/Documents/TechStuff/OnlineCourses/Coursera/Algos_DesignAndAnalysis_PartI_Roughdarden_sp2015/Week4/"

tf = 1
if tf == 0:
    N=875714 #big file
    source = p + 'SCC.txt'
else:
    N=19 #small test file
    source = p + 'sccsmall.txt'

#globals
visited={}
finish={}
leader={}
t = 0
s = 0

def getG():
    G={}
    Grev={}
    for i in range(1,N+1):
        G[i]=[]
        Grev[i]=[]
    fin=open(source)
    for line in fin:
        v1=int(line.split()[0])
        v2=int(line.split()[1])
        G[v1].append(v2)
        Grev[v2].append(v1)
    fin.close()
    return G, Grev

def init():
    for i in range(1,N+1):
        visited[i]=0
        finish[i]=0
        leader[i]=0

def dfs(G, i):
    global t
    visited[i]=1
    leader[i]=s
    for j in G[i]:
        if(visited[j]==0): dfs(G,j)
    t=t+1
    finish[i]=t
    
def dfs_loop(G):
    global t
    global s
    t=0 #number of nodes processed so far
    s=0 #current source vertex
    i=N
    while(i>0):
        if(visited[i]==0):
            s=i
            dfs(G,i)
        i=i-1
        
#if __name__ == "__main__":
def begin():
    init()
    g, grev=getG()
    dfs_loop(grev) #THE FIRST LOOP ON REVERSE GRAPH

    # construct new graph
    newGraph={}
    for i in range(1,N+1):
        temp=[]
        for x in g[i]: temp.append(finish[x])
        newGraph[finish[i]]=temp

    init()    
    dfs_loop(newGraph) #THE SECOND LOOP 

    # statistics
    lst= sorted(leader.values())
    stat=[]
    pre=0
    for i in range(0,N-1):
        if lst[i]!=lst[i+1]:
            stat.append(i+1-pre)
            pre=i+1
    stat.append(N-pre)
    L= sorted(stat)
    L.reverse()
    print(L[0:5])

begin()