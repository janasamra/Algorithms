#import liberary for int_max
from sys import maxsize 
INT_MAX = maxsize
V = 5
def isValidEdge(u, v, inMST):
    if u == v:
        return False
    if inMST[u] == False and inMST[v] == False:
        return False
    elif inMST[u] == True and inMST[v] == True:
        return False
    return True
 
def prim(weight):
    inMST = [False] * V
 
    # Include first vertex in MST
    inMST[0] = True

    edge_count = 0
    mincost = 0
    while edge_count < V - 1:
 
        # Find minimum weight valid edge.
        minn = INT_MAX
        a = -1
        b = -1
        for i in range(V):
            for j in range(V):
                if weight[i][j] < minn:
                    if isValidEdge(i, j, inMST):
                        minn = weight[i][j]
                        a = i
                        b = j
 
        if a != -1 and b != -1:
            print("Edge %d: (%d, %d) weight: %d" %
                 (edge_count, a, b, minn))
            edge_count += 1
            mincost += minn
            inMST[b] = inMST[a] = True
    print("Minimum weight = %d" % mincost)
if __name__ == "__main__":    
    weight = [[INT_MAX, 2, INT_MAX, 6, INT_MAX],
            [2, INT_MAX, 3, 8, 5],
            [INT_MAX, 3, INT_MAX, INT_MAX, 7],
            [6, 8, INT_MAX, INT_MAX, 9],
            [INT_MAX, 5, 7, 9, INT_MAX]]
 
    # Print the solution
    prim(weight)



    