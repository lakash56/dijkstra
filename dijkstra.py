g = {
    'a':{'b':10,'c':3},
    'b':{'c':1,'d':2},
    'c':{'b':4,'d':8,'e':12},
    'd':{'e':7},
    'e':{'d':9}
    }
def dijkstra(g,start,end):
    short_path = {} #store the weight of path when going through the graph
    predecessor = {} #stors the weight of the previous path.
    unseenNodes = g
    infinity = 999999999999 #just a large number
    path = []
    for node in unseenNodes:
        short_path[node] = infinity
    short_path[start]=0
   #print(short_path)
   
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
               minNode = node
            elif short_path[node] < short_path [minNode]:
                minNode = node       
        for childNode, weight in g[minNode].items():
            if weight + short_path[minNode] < short_path[childNode]:
                short_path[childNode] =weight +short_path[minNode]
                predecessor[childNode] =minNode
        unseenNodes.pop(minNode)
    #print(short_path)
    currentNode = end
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode =predecessor[currentNode]
        except KeyError:
            print('No Path')
            break
    if short_path[end] !=infinity:
        print('shortest path is ' + str(short_path[end]))
        print('Path = ' + str(path))

     
dijkstra(g,'a','d')