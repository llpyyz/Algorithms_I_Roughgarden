p = "C:/Users/David/Documents/TechStuff/OnlineCourses/Coursera/Algos_DesignAndAnalysis_PartI_Roughdarden_sp2015/Week5/"
#fn = "dijkstrasmall1_input.txt"
fn = "dijkstra_input.txt"

data = open(p+fn,"r")
vertex_count = 0
nodes2 = []
distances2 = {}
g = {}
lst = []
for line in data:
    l = line.split()
    #print "l:",l
    g[int(l[0])] = {}
    #print g.items()
    for i in range(1,len(l)):
        e = l[i].split(',')
        #print "e:",e
        g[int(l[0])][int(e[0])] = int(e[1])
    lst.append(line.split())
    vertex_count += 1
    
print g

for i in range(vertex_count):
    nodes2.append(lst[i][0])
    distances2[lst[i][0]] = {}
    #print "i:",i
    for j in range(1,len(lst[i])):
        #pass
        s = lst[i][j].split(',')
        #print s[0], s[1]
        distances2[lst[i][0]][s[0]] = int(s[1])
        distances2[s[0]] = {}
        distances2[s[0]][str(i+1)] = int(s[1])
    #print
    for k, v in distances2.items():
        for kk,vv in v.items():
            distances2[kk][k] = vv


def popmin(pqueue):
    # A (ascending or min) priority queue keeps element with
    # lowest priority on top. So pop function pops out the element with
    # lowest value. It can be implemented as sorted or unsorted array
    # (dictionary in this case) or as a tree (lowest priority element is
    # root of tree)
    lowest = 1000000
    keylowest = None
    for key in pqueue:
        if pqueue[key] < lowest:
            lowest = pqueue[key]
            keylowest = key
    del pqueue[keylowest]
    return keylowest
    
def dijkstra(graph, start):
    # Using priority queue to keep track of minium distance from start
    # to a vertex.
    pqueue = {} # vertex: distance to start
    dist = {}   # vertex: distance to start
    pred = {}   # vertex: previous (predecesor) vertex in shortest path
 
    # initializing dictionaries
    for v in graph:
        dist[v] = 1000000
        pred[v] = -1
    dist[start] = 0
    for v in graph:
        pqueue[v] = dist[v] # equivalent to push into queue
 
    while pqueue:
        u = popmin(pqueue) # for priority queues, pop will get the element with smallest value
        for v in graph[u].keys(): # for each neighbor of u
            w = graph[u][v] # distance u to v
            newdist = dist[u] + w
            if (newdist < dist[v]): # is new distance shorter than one in dist?
                # found new shorter distance. save it
                pqueue[v] = newdist
                dist[v] = newdist
                pred[v] = u
 
    return dist, pred


graph = {0 : {1:6, 2:8},
1 : {4:11},
2 : {3: 9},
3 : {},
4 : {5:3},
5 : {2: 7, 3:4}}
 
dist, pred = dijkstra(g, 1)

pl1 = [7,37,59,82,99,115,133,165,188,197]
pl2 = [10,30,50,80,90,110,130,160,180,190]

for elt in pl1:
    print elt, dist[elt]

#print "Predecesors in shortest path:"
#for v in pred: 
#    print "%s: %s" % (v, pred[v])
#
#print "Shortest distance from each vertex:"
#
#for v in dist: 
#    print "%s: %s" % (v, dist[v])
#    
